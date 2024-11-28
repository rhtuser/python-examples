#!/usr/bin/env python3
#
# To run this example, you need two things. First, you need to create
# a python virtual environment and activate it. For this, you do:
#
#   $ python3 -m venv venv
#   $ . ./venv/bin/activate
#
# Having activated it, simply use pip3 to install flask.
#
#   (venv) $ pip3 install flask
#
# You don't need to do this more than once. If you want to return to
# this example later, simply open a terminal window again, and
# reactivate the virtual environment, then proceed with whatever you
# wanted to try:
#
#   $ . ./venv/bin/activate
#
# To run the application, after you have activated the environment,
# simply run:
#
#   (venv) $ flask --app ./code/ch05/friendly-service run
#
# You can also run it in debug mode, which means any code changes
# will be automatically reloaded, and additional information will be
# provided in the case of an error, like this:
#
#   (venv) $ flask --app ./code/ch05/friendly-service --debug run
#
# You can test it from a web browser, or using curl, in a new
# terminal window:
#
#   $ curl http://localhost:5000/
#   This is a simple web service. It has four endpoints:
#       - GET /hello
#       - GET /hello/{name}
#       - GET /quote
#       - GET /quote/{number}
#   Have fun using them!
#
# NOTE: Have a look at these two modules, just to see what they do.
import quotes
import greetings

# NOTE: This makes our application a web service!
from flask import Flask

# NOTE: This makes it safe to accept parameters in URLs.
from markupsafe import escape

# NOTE: This creates everything we need to answer requests.
app = Flask(__name__)

# NOTE: This function becomes the default response if we get a
#       request, since it is registered to activate at root URI.
@app.get("/")
def info():
    return """This is a simple friendly web service. It has four endpoints:
    - GET /hello
    - GET /hello/{name}
    - GET /quote
    - GET /quote/{number}
Have fun using them!
"""

# This function just returns the default greeting to a "stranger"
# as we do not have any useful information.
@app.get("/hello")
def say_hello():
    return greetings.greet() + ", stranger!\n"

# This function returns the default greeting if the user is not
# recognised, or a personalised greeting to our friends.
@app.get("/hello/<name>")
def say_hello_named(name):
    # NOTE: The best place to make sure our program does not crash
    #       due to invalid input, and ensure the rest of our
    #       application can work correctly, is to sanitise the input
    #       data at its source, where it is coming into our program.
    #       So what we are doing here is safeguarding against web
    #       attacks (escape() function) and making sure the name is
    #       properly formatted (a capital initial and small letters).
    name = escape(name).capitalize()
    return greetings.greet(name) + ", " + name + "\n"

# This function just returns a random quote.
@app.get("/quote")
def get_random_quote():
    return quotes.get_quote() + "\n"

# This function allows users to ask for a specific quote, but it
# requires that the parameter in the URL is a number.
#
# NOTE: Another trick for input validation, this time it is performed
#       by the Flask module instead of us doing it manually.
@app.get("/quote/<int:which>")
def get_a_quote(which):
    return quotes.get_quote(which) + "\n"
