# Bangazon Orientation Advanced Python Exercises

## The Family Dictionary

### Instructions

1. Define a dictionary that contains information about several members of your family. Use the following example as a template.
    ```
    my_family = {
        'sister': {
            'name': 'Krista',
            'age': 42
        },
        'mother': {
            'name': 'Cathie',
            'age': 70
        }
    }
    ```
2. Using a dictionary comprehension, produce output that looks like the following example.

    `Krista is my sister and is 42 years old`

    > **Helpful hint:** To convert an integer into a string in Python, it's `str(integer_value)`


## Kill Nickelback

In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

### Instructions

1. Define a set that contains tuples. Each tuple should contain two strings:
    1. The name of an artist
    1. A song by that artist
    _Make sure that some of the songs are from the band Nickelback. You can see a [list of their greatest hits](https://www.amazon.com/Best-Nickelback-1/dp/B00FFERTUK/) on Amazon._
1. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.


## Squared Randoms

## References

* [Random module](https://docs.python.org/3.6/library/random.html)
* [Python Lists](https://docs.python.org/3.6/tutorial/datastructures.html)

### Instructions

1. Using the `random` module and the `range` method, generate a list of 20 random numbers between 0 and 49.
1. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is `[2, 5]`, the final list will be `[4, 25]`.


## Testing the Animals

1. Copy the contents of [animals.py](../resources/animal.py) into the file you just created.

### Overview

As a team, we'll be building unit test coverage for all the functionality of the code in the `animal` module. We'll discuss how writing tests often affect the implementation code, and how to think bout covering edge cases in your test suit.

### Instructions

Write test cases to verify the I/O of the following methods of `Animal` and `Dog`.

1. In the test class' `setUpClass()` method, create an instance of `Animal` and `Dog`.
1. Animal object has the correct `name` property.
1. Set a species and verify that the object property of `species` has the correct value.
1. Invoking the `walk()` method set the correct speed on the both objects.
1. The animal object is an instance of `Animal`.
1. The dog object is an instance of `Dog`.

#### Test Discovery

Read the [Test Discovery section](https://docs.python.org/3.3/library/unittest.html#unittest-test-discovery) of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.


## Calculator Unit Tests

Just like you did in JavaScript when you learned about Jasmine, you're going to create a class that test the functionality of a Calculator class.


## Advanced Challenge: Matching Makes & Models

### Overview

This is an advanced challenge because it requires multiple layers of iteration. It is also an introduction to database relationships because there are four unique collections that are all related to each other.

In the `makes` and `colors` collections, each item has a numeric identifier, and then a string representation.

In the `models` collection, each item also has a numeric identifier, but also stores the numeric identifier of a model

Finally, the `available_car_colors` collection is storing the relationships between items in two foreign collections. The first number represents the corresponding model, and the second number represents the corresponding color.

### Instructions

#### Part I: Reporting Object

You must first build a new dictionary that follows the format below. 

1. Each key in the dictionary should be the name of a make, and its value will be a dictionary.
1. The keys in the make dictionary will be the models, and the value will be a list of colors in which that the model is available.

#### Part II - Command Line Report

Output a report on the command line that looks like this.

```
Ford
------------------
F150 available in Black, Blue, Ivory
Thunderbird available in Black, Red, White

etc...
```

# Black Hat Hacker Challenge

Rewrite your nested `for` loops as nested comprehensions.