#!/usr/bin/env python3
from json import JSONEncoder

class Guest:
    def __init__(self, firstname, middlename, lastname,
                address = '', city = '', state = '', country = '',
                email = '', greeting = '', visits = 0):
        self._firstname = str(firstname).strip().capitalize()
        self._middlename = str(middlename).strip().capitalize()
        self._lastname = str(lastname).strip().capitalize()
        self._address = str(address).strip().capitalize()
        self._city = str(city).strip().capitalize()
        self._state = str(state).strip().capitalize()
        self._country = str(country).strip().capitalize()
        self._email = str(email).strip().lower()
        self._greeting = str(greeting).strip()
        self._visits = int(visits)

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = str(firstname).capitalize()

    @property
    def middlename(self):
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        self._middlename = str(middlename).capitalize()

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = str(lastname).capitalize()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = str(address).capitalize()

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = str(city).capitalize()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = str(state).capitalize()

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = str(country).capitalize()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = str(email).capitalize()

    @property
    def greeting(self):
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        self._greeting = str(greeting).capitalize()

    @property
    def visits(self):
        return self._visits

    @visits.setter
    def visits(self, visits):
        self._visits = int(visits)

    # Improving serialization by delegating conversion to list here.
    def as_list(self):
        return [self._firstname, self._middlename, self._lastname,
                    self._address, self._city, self._state, self._country,
                    self._email, self._greeting, self._visits]

    # A convenient way of generating string representations of objects.
    def __str__(self):
        return "Guest[First: {}, Middle: {}, Last: {}, Address: {}, {}, {}, {}, Email: {}, Greeting: {}, Visits: {}".format(
                    self._firstname, self._middlename, self._lastname,
                    self._address, self._city, self._state, self._country,
                    self._email, self._greeting, self._visits
                )

    # A test for equality - all attributes need the same values.
    def __eq__(self, obj):
        if type(obj) != Guest:
            return False
        return (self._firstname == obj.firstname and self._middlename == obj.middlename and
                self._lastname == obj.lastname and self._address == obj.address and
                self._city == obj.city and self._state == obj.state and
                self._country == obj.country and self._email == obj.email and
                self._greeting == obj.greeting and self._visits == obj.visits)

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "email": self.email,
            "greeting": self.greeting,
            "visits": self.visits
        }

    @staticmethod
    def from_dict(thedict):
        return Guest(thedict['firstname'],
                        thedict['middlename'],
                        thedict['lastname'],
                        thedict['address'],
                        thedict['city'],
                        thedict['state'],
                        thedict['country'],
                        thedict['email'],
                        thedict['greeting'],
                        thedict['visits'])

class GuestEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Guest):
            return obj.to_dict()
        return JSONEncoder.default(self, obj)

def main():
    print("This is a class module. Import it.")

if __name__ == "__main__":
    main()
