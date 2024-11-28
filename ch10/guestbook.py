#!/usr/bin/env python3
#
# As with the first web service (ch05), we need Flask, then run as:
#
#   (venv) $ flask --app ./code/ch10/guestbook --debug run
#
import os
import re

from flask import Flask, render_template, request, session
from guest import Guest

guestfile = "code/ch10/guests.csv"
app = Flask(__name__)

# This will be used as the cryptographic key for session data, which
# must be encrypted to be safe. You can generate a good key using:
#   python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = b'9cb65f4971c6853a00ffae876fdcd2b7b67fd3a4f8966bc237437c176ab4ce83'

# Make sure that the guestbook exists and is read-write.
def init():
    if not os.path.exists(guestfile):
        print("INFO: Creating new, empty, guestfile.")
        gf = open(guestfile, "w"); gf.close()
    elif not (os.stat(guestfile).st_mode & 0o600) == 0o600:
        raise FileExistsError("Guest book exists but is not read/write.")

# Use a generator in a nested function to search records one by one,
# until we find the matching one. Return a new Guest, or None.
def find_user(user: Guest):
    print("INFO: Searching for {}".format(str(user)))
    def get_customers():
        with open(guestfile, "r") as gb:
            for customer in gb.readlines():
                yield customer.strip().split(",")

    for customer in get_customers():
        if customer[0] == user.firstname and customer[1] == user.middlename and customer[2] == user.lastname:
            print("INFO: Search found {}".format(customer))
            return Guest(*customer)

    print("INFO: Search found nothing.")
    return None

# For now, there is no smart way to do this. Just copy the entire
# file into a new one, looking at each record to see if this is our
# current user. If so, write the new data instead, if not, just copy
# the record and move on. When finished, if there was no update, add
# our current user at the end of the file, and replace the old file
# with the new one.
def store_user_data(user: Guest):
    print("INFO: Storing user data for {}".format(str(user)))
    def get_customers():
        with open(guestfile, "r") as gb:
            for customer in gb.readlines():
                yield customer.strip().split(",")

    updated = False
    with open(guestfile + ".tmp", "w") as wb:
        for customer in get_customers():
            if customer[0] == user.firstname and customer[1] == user.middlename and customer[2] == user.lastname:
                print("INFO: Updating existing record: {}".format(customer))
                updated = True
                # Could work this way, but is clumsy and error-prone.
                # print(user.firstname, user.middlename, user.lastname,
                #         user.address, user.city, user.state, user.country,
                #         user.email, user.greeting, user.visits,
                #         sep=",", file=wb)
                # Much better to delegate list creation to the class.
                print(*user.as_list(), sep=",", file=wb)
            else:
                print(*customer, sep=",", file=wb)

    # Replace the old guest file with new one.
    os.replace(guestfile + ".tmp", guestfile)

    # Our job is done if we updated an existing record.
    if updated:
        return

    # If we did not update a record, append it at the end.
    with open(guestfile, "a") as ab:
        print("INFO: Appending new user to guest book.")
        print(*user.as_list(), sep=",", file=ab)

# Everything happens at the root URL. The user could land here:
#  - opening the page for the first time, with no session
#       -> we need to present them with a "login" form
#  - after creating a session by sending their login data
#       -> we need to find the user in the guest book or add them
@app.route("/", methods=['GET', 'POST'])
def index():
    # The request is GET and no session exists. Show login form.
    if request.method == 'GET' and not 'firstname' in session:
        return render_template("login_form.html")

    # The request is POST and no session exists. Expect login data.
    if request.method == 'POST' and not 'firstname' in session:
        # Store login data in session, but also to create a Guest.
        user_param = []
        errors = []
        for param in ['firstname', 'middlename', 'lastname']:
            # Middle name is optional, but we search the other two
            # to make sure they contain at least one letter of the
            # alphabet.
            if param != 'middlename' and not re.search("^[a-zA-Z]+$", request.form[param].strip()):
                errors.append("{} is a mandatory parameter".format(param))
                continue
            # Any of the three parameters is checked that they only
            # contain letters.
            if not re.search("^[a-zA-Z]*$", request.form[param].strip()):
                errors.append("{} contains non-word characters".format(param))
                continue
            session[param] = request.form[param].strip()
            user_param.append(session[param])

        # If there were errors, clear the session data and go again.
        if errors:
            for param in ['firstname', 'middlename', 'lastname']:
                session.pop(param, None)
            return render_template("login_form.html", errors = errors)

        # Try to find the user in our guestbook.
        user = find_user(Guest(*user_param))

        # If the user is not found, ask for more info.
        if not user:
            user = Guest(session['firstname'], session['middlename'], session['lastname'])
            return render_template("user_data.html", user = user)

        # User was found, increase visit count.
        user.visits += 1

        # Store additional user data in session.
        session['address'] = user.address
        session['city'] = user.city
        session['state'] = user.state
        session['country'] = user.country
        session['email'] = user.email
        session['greeting'] = user.greeting
        session['visits'] = user.visits
        store_user_data(user)

        # Greet the user.
        return render_template("greet_user.html", user = user)

    # The request is POST and session exists. We got more user data.
    if request.method == 'POST':
        user_param = []
        errors = []
        # Store additional data in session.
        for param in ['firstname', 'middlename', 'lastname',
                        'address', 'city', 'state', 'country',
                        'email', 'greeting']:
            # Middle name and state are optional in this expanded
            # form, but we validate the other parameters to make sure
            # they at least contain some value.
            if not param in ('state', 'middlename') and not re.search("^.+$", request.form[param].strip()):
                errors.append("{} is a mandatory parameter".format(param))
                user_param.append('')
                continue
            # Email must adhere to a specific format. The real-life
            # regular expression for email validation is quite a bit
            # more horrifying - feel free to google it. :)
            if param == 'email' and not re.search("^\w+[\.\w]+@\w+\.\w+$", request.form[param]):
                errors.append("{} is not a valid email".format(param))
                user_param.append('')
                continue
            # If it's not an email, again, we just check that the
            # parameter consists of alphanumeric characters and
            # spaces.
            elif param != 'email' and not re.search("^[\w\s]*$", request.form[param].strip()):
                errors.append("{} contains non-word characters".format(param))
                user_param.append('')
                continue
            session[param] = request.form[param]
            user_param.append(session[param])

        # Construct a user with whatever we have.
        user = Guest(*user_param)

        # If there were errors, ask for user data again.
        if errors:
            return render_template("user_data.html",
                        user = user,
                        errors = errors)

        # This is the first visit, so append "1" to parameter list.
        user_param.append(1)
        session['visits'] = 1

        # Store additional user data.
        user = Guest(*user_param)
        store_user_data(user)

        # Welcome the user.
        return render_template("new_user.html", user = user)

    # The request is neither of the above. Just show a greeting page.
    user_param = []
    for param in ['firstname', 'middlename', 'lastname',
                    'address', 'city', 'state', 'country',
                    'email', 'greeting', 'visits']:
        if param in session:
            user_param.append(session[param])
        else:
            user_param.append('')
    user = Guest(*user_param)

    return render_template("greet_user.html", user = user)

# Return a custom message upon an HTTP error.
@app.errorhandler(404)
def url_not_found(error):
    return "ERROR: This URL is not recognised.\n", 404

if __name__ == "__main__":
    print("ERROR: Run me as a Flask application.")
    exit(1)
elif __name__ == "guestbook":
    init()
else:
    print("ERROR: Can only be used as a Flask app.")
    exit(1)
