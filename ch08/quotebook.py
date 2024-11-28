#!/usr/bin/env python3
#
# As with the first web service (ch05), we need Flask, then run as:
#
#   (venv) $ flask --app ./code/ch08/quotebook --debug run
#
import os
import random

from flask import Flask, appcontext_tearing_down, request

quotefile = "code/ch08/quotes.txt"
quotes = []
app = Flask(__name__)

def init():
    global quotes

    if not os.path.exists(quotefile):
        raise FileNotFoundError("Quote file not found.")

    print("Loading quotes from {}...".format(quotefile))

    with open(quotefile, "r") as quote_source:
        for new_quote in quote_source.readlines():
            quotes.append(new_quote.strip())

# TODO: Why every request?
@app.teardown_appcontext
def shutdown(exception):
    with open(quotefile, "w") as quote_file:
        for quote_record in quotes:
            quote_file.write(quote_record + "\n")

# Default (index) response.
@app.get("/")
def info():
    return """This is a quote generator. It has four endpoints:
    - GET /quote           returns a random quote
    - GET /quote/{number}  returns a specific quote
    - GET /quote/count     returns the number of available quotes
    - POST /quote          adds a quote to the library
"""

# This function just returns a random quote.
@app.get("/quote")
def get_random_quote():
    return quotes[random.randint(0, len(quotes) - 1)] + "\n"

# This function allows users to ask for a specific quote, but it
# requires that the parameter in the URL is a number.
@app.get("/quote/<int:which>")
def get_a_quote(which):
    try:
        response = quotes[which]
        assert response, "ERROR: Quote is empty!"
    except IndexError:
        return "ERROR: No such quote (value too large).\n", 404
    except AssertionError as err:
        return "INTERNAL " + str(err) + "\n", 500

    return response + "\n"

# Returns the number of quotes.
@app.get("/quote/count")
def get_quote_count():
    return str(len(quotes)) + "\n"

# Add a new quote to the library, if it does not exist yet.
@app.post("/quote")
def add_a_quote():
    try:
        assert request.content_type == "text/plain", "Only accepting plaintext data."
        new_quote = request.data.decode().strip()
        quotes.append(new_quote)
    except AssertionError as ae:
        return str(ae), 400
    return "OK\n"

# Return a custom message upon an HTTP error.
@app.errorhandler(404)
def url_not_found(error):
    return "ERROR: This endpoint is not registered.\n", 404

if __name__ == "__main__":
    print("ERROR: Run me as a Flask application.")
    exit(1)
elif __name__ == "quotebook":
    init()
else:
    print("ERROR: Can only be used as a Flask app.")
    exit(1)
