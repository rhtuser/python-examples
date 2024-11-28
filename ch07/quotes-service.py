#!/usr/bin/env python3
#
# As with the first web service (ch05), we need Flask, then run as:
#
#   (venv) $ flask --app ./code/ch07/quotes-service --debug run
#
# As opposed to the previous example, this service only deals with
# quotes, so it only has two endpoints:
#
#   - GET /quote
#   - GET /quote/{number}
#
# The purpose is to demonstrate exception handling.
import quotes
from flask import Flask

# Create the web service context.

app = Flask(__name__)

# Default (index) response.
@app.get("/")
def info():
    return """This is a quote generator. It has two endpoints:
    - GET /quote           returns a random quote
    - GET /quote/{number}  returns a specific quote
"""

# This function just returns a random quote.
@app.get("/quote")
def get_random_quote():
    return quotes.get_quote() + "\n"

# This function allows users to ask for a specific quote, but it
# requires that the parameter in the URL is a number.
#
# NOTE: We have modified quotes.py to not check whether the number
#       is too large, so we will receive an IndexError if the user
#       requests a quote that does not exist, and we can handle it
#       here by catching that exception.
@app.get("/quote/<int:which>")
def get_a_quote(which):
    try:
        response = quotes.get_quote(which)
        assert response, "ERROR: Quote is empty!"
    except IndexError:
        return "ERROR: No such quote (value too large).\n", 404
    except AssertionError as err:
        return "INTERNAL " + str(err) + "\n", 500

    return response + "\n"

# NOTE: With Flask, you use a different mechanism if you want to
#       handle HTTP errors.
@app.errorhandler(404)
def url_not_found(error):
    return "ERROR: This endpoint is not registered.\n", 404
