# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''

# Example so that you can see a passing test


def f():
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################

# Define a function named add that takes two numbers and returns the sum.


def add(a, b):
    """
    The sum of two numbers.

    Parameters
    ----------
    a: int, float
        First number to add.
    b: int, float
        Second number to add.

    Returns
    -------
    sum: int, float
       Sum of the two arguments.
    """
    return a + b

# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.


def to_tuple(a, b, c):
    """
    Return arguments as tuple.

    Parameters
    ----------
    a: object
        Any object.
    b: object
        Any object.
    c: object
        Any object.

    Returns
    -------
    t: tuple
       Contains the three function arguments.
    """
    return a, b, c

# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.


def check5(x):
    """
    Check if a number is greater than 5.

    Parameters
    ----------
    x: int, float
        Number to check.

    Returns
    -------
    status: bool
       Boolean indicating if the number was greater than 5.
    """
    return check_n(x, 5)

# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second


def check_n(x, n):
    """
    Check if a number is greater than another number.

    Parameters
    ----------
    x: int, float
        Number to check.
    n: int, float
        Number to check against.

    Returns
    -------
    status: bool
        Boolean indicating if the number was greater than
        the second argument.
    """
    return x > n

#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.


def check_list(li, n):
    """
    Check if numbers in a list are >= to another number.

    Parameters
    ----------
    li: list of int or float
        List of number to check.
    n: int or float
        Number to check against.

    Returns
    -------
    r: list of bool
       Results of the check.
    """
    return check_list_nth(li, n, 1)

# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.


def check_list_nth(li, n, nth):
    """
    Check if every nth number in a list is >= another number.

    Parameters
    ----------
    li: list of int or float
        List of number to check.
    n: int or float
        Number to check against.
    nth: int
        Every nth number of the list will be taken.

    Returns
    -------
    r: list of bool
       Results of the check.
    """
    return [x >= n for x in li[::nth]]

# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.


def add_new_list(li, x):
    """
    Add element to new list.

    Parameters
    ----------
    li: list
        Original list to add to.
    x: object
        Any object to add to the list.

    Returns
    -------
    ln: list
        New list with x as the last element.
    """
    # this is just one way to copy a list which I use here since most of you
    # used the copy command. Another would be ln = li[:].
    # It is mainly a matter of taste which one to use.
    ln = list(li)
    ln.append(x)
    return ln


# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(li, nth=2):
    """
    Remove every n-th element from a list.

    Parameters
    ----------
    li: list
        List to remove elements from.
    nth: int, optional
        Every n-th element will be removed.

    Returns
    -------
    ln: list
        List with elements removed.
    """
    # In this way not the whole list has to be copied but it might be slower.
    return [x for i, x in enumerate(li) if i % nth != 0]

# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values


def search_n(li, x):
    """
    Search for element in a list.

    Parameters
    ----------
    li: list
        List to search in.
    x: object
        Object to search for in the list.

    Returns
    -------
    index: int or None
        Index at which x was found or None if it was not found.
    xr: object or None
        The found object or None if nothing was found
    """
    try:
        return li.index(x), x
    except ValueError:
        return None, None

################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.


def args_to_dict(a, b, c):
    """
    Convert arguments to dictionary.

    Parameters
    ----------
    a: object
        First argument.
    b: object
        Second argument.
    c: object
        Third argument.

    Returns
    -------
    d: dict
        Dictionary of arguments with the number of the argument as the keys.
    """
    return args_to_dict_general(a, b, c)

# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments


def args_to_dict_general(*args):
    """
    Convert arguments to dictionary.

    Parameters
    ----------
    args: object
        Any number of arguments.

    Returns
    -------
    d: dict
        Dictionary of arguments with the number of the argument as the keys.
    """
    return {i: k for i, k in enumerate(args)}

# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.


def lists_to_dict(keys, values):
    """
    Convert two lists to a dictionary.

    Parameters
    ----------
    keys: list
        Keys to use in the dictionary.
    values: list
        Values to use in the dictionary.

    Returns
    -------
    d: dict
        Dictionary combined from the input lists.
    """
    return {k: v for k, v in zip(keys, values)}

# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.


def search_list(a, b):
    """
    Search elements of b in a.

    Parameters
    ----------
    a: list
        List to search in.
    b: list
        List of elements to search in a.

    Returns
    -------
    d: dict
       Keys are the indices of found elements of b in a.
       Values are the found values of b.
       Empty dictionary if nothing was found.
    """
    return {i: v for i, v in enumerate(a) if v in b}


# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(d, sep):
    """
    Extract string out of dictionary and join using the seperator.

    Parameters
    ----------
    d: dict
        Dictionary to extract string values out of.
    sep: string
        String to use for seperating the found values in the result.

    Returns
    -------
    s: string
       Seperated by the sep string.
       If no strings were found in the dict then an empty string.
    """

    return sep.join([d[x] for x in d if type(d[x]) == str])


# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(li):
    """
    Classify list elements by data type.

    Parameters
    ----------
    li: list
        List to classify

    Returns
    -------
    d: dict
       Dictionary containing the three classes 'int', 'str' and 'other'.
       Each of this classes is a list of elements out of the original
       list that fit that type.
    """
    # This is written a little more general than necessary but it would allow
    # easy extension to more classes by modifying the classifier dict
    classifier = {int: 'int',
                  str: 'str'}

    d = {'others': []}
    for c in classifier.values():
        d[c] = []

    for x in li:
        try:
            d[classifier[type(x)]].append(x)
        except KeyError:
            d['others'].append(x)

    return d
