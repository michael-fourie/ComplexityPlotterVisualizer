"""
This module creates lists that will be used to analyze the performance of the searching and sorting algorithms.
Student Name: Michael Fourie
Student Number: 20102203
"""
import random


def unorderdIntegers(minValue, maxValue, length):
    """
    This function produces a list of random integers unordered.
    Input: the range of what the integers should be in aswell as length of list
    Output: list of unordered integers
    """
    # Empty list to hold the values
    aList = []

    # For loop to append each random value to the list
    for i in range(0, length):
        aList.append(random.randint(minValue, maxValue))

    # return list
    return aList


def orderdIntegersAscending(minValue, maxValue, length):
    """
    This function produces a list of random integers ordered from smallest to largest.
    Input: the range of what the integers should be in aswell as length of list
    Output: list of ordered integers
    """
    # Empty list to hold the values
    aList = []

    # For loop to append each random value to the list
    for i in range(0, length):
        aList.append(random.randint(minValue, maxValue))

    # sort list
    aList.sort()

    # return list
    return aList


def orderdIntegersDescending(minValue, maxValue, length):
    """
    This function produces a list of random integers ordered from largest to smalled.
    Input: the range of what the integers should be in aswell as length of list
    Output: list of ordered integers
    """
    # Empty list to hold the values
    aList = []

    # For loop to append each random value to the list
    for i in range(0, length):
        aList.append(random.randint(minValue, maxValue))

    # sort list
    aList.sort(reverse=True)

    # return list
    return aList


def unorderdFloats(length):
    """
    This function produces a list of unordered floats between 0.0 and 1.0
    Input: length of list
    Output: unordered list
    """

    # empty list to hold values
    aList = []

    # for loop to append values to list
    for i in range(length):
        aList.append(random.random())

    # rerns the list
    return aList


def ascendingFloats(length):
    """
    This function produces a list of ascending floats between 0.0 and 1.0
    Input: length of list
    Output: unordered list
    """

    # empty list to hold values
    aList = []

    # for loop to append values to list
    for i in range(length):
        aList.append(random.random())

    # sort the list
    aList.sort()

    # rerns the list
    return aList


def descendingFloats(length):
    """
    This function produces a list of Descending floats between 0.0 and 1.0
    Input: length of list
    Output: unordered list
    """

    # empty list to hold values
    aList = []

    # for loop to append values to list
    for i in range(length):
        aList.append(random.random())

    # sort the list
    aList.sort(reverse=True)

    # rerns the list
    return aList


if __name__ == '__main__':
    print(unorderdIntegers(-1000, 1000, 25),
          '\nshould be a list of random integers, unsorted, 25 units long, range from -1000 to 1000')
    print('')
    print(orderdIntegersAscending(-1000, 1000, 25),
          '\nshould be a list of random integers, sorted and ascending, 25 units long, range from -1000 to 1000')
    print('')
    print(orderdIntegersDescending(-1000, 1000, 25),
          '\nshould be a list of random integers, sorted and descending, 25 units long, range from -1000 to 1000')
    print('')
    print(unorderdFloats(25), '\nshould be a list of random floats, unsorted.')
    print('')
    print(descendingFloats(25), '\nshould be a list of random floats, descending.')
    print('')
    print(ascendingFloats(25), '\nshould be a list of random floats, ascending.')
    print('')









