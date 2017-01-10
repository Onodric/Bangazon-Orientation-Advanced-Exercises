#--------|---------|---------|---------|---------|---------|---------|---------
# Testing the Animals

# > **Note:** This code exercise will be part of a live coding session with the instructor. Feel free to try it on your own beforehand and come to class with questions, or just wait until live coding starts.

## Overview

# As a team, we'll be building unit test coverage for all the functionality of the code in the `animal` module. We'll discuss how writing tests often affect the implementation code, and how to think bout covering edge cases in your test suit.

## Instructions

# Write test cases to verify the I/O of the following methods of `Animal` and `Dog`.

# 1. In the test class' `setUpClass()` method, create an instance of `Animal` and `Dog`.
# 1. Animal object has the correct `name` property.
# 1. Set a species and verify that the object property of `species` has the correct value.
# 1. Invoking the `walk()` method set the correct speed on the both objects.
# 1. The animal object is an instance of `Animal`.
# 1. The dog object is an instance of `Dog`.

## Test Discovery

# Read the [Test Discovery section](https://docs.python.org/3.3/library/unittest.html#unittest-test-discovery) of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

# python -m unittest discover -s . -p "Test*.py" -v

# animals.py follows:

class Animal:
    
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def get_name(self):
        """Returns the animal's name"""
        return self.name

    def walk(self):
        """Sets the speed of the animal"""
        if isinstance(self.legs, int) and self.legs > 0:
            self.speed = self.speed + (0.1 * self.legs)
        else:
            raise ValueError('Legs property must contain a number greater than 0')

    def set_legs(self, number_of_legs):
        """Sets the species of the animal"""
        self.legs = number_of_legs

    def set_species(self, species):
        """Sets the species of the animal"""
        self.species = species

    def get_species(self):
        """Returns the species of the animal"""
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")

    def walk(self):
        """Sets the speed of the dog"""
        self.speed = self.speed + (0.2 * self.legs)
