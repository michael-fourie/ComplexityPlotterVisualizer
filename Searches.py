"""
This module will hold all of the sorting algorithms.
Student Name: Michael Fourie
Student Number: 2102203
"""


def binarySearch(aList, target):
    """
    This is the binary search function.
    Input: list of values, target value
    Output: tuple containing the index of the search vale, none if not found, aswell as the count of comparisons the function made
    """
    low = 0
    high = len(aList) - 1

    # This will count the number of itterations
    itterationCount = 0

    while high >= low:
        # This will add a value to the itteration count
        itterationCount += 1

        midpoint = (high + low) // 2

        if target == aList[midpoint]:

            # Tuple to be returned from function
            returnedTuple = (midpoint, itterationCount)
            return returnedTuple

        elif target > aList[midpoint]:
            low = midpoint + 1
        elif target < aList[midpoint]:
            high = midpoint - 1

    # Tuple to be returned from function
    returnedTuple = (None, itterationCount)
    return returnedTuple


def linearSearch(aList, target):
    """
    This is the linear search function.
    Input: a list of values, as well as target value
    Output: Tuple of index of searched value, none if not found, aswell as the number of comparisons made
    """

    # Count the number of itterations
    itterationCount = 0

    for element in range(len(aList)):
        if aList[element] == target:

            # The tutple to be returned when element is found in the list
            returnedTuple = (element, itterationCount)
            return returnedTuple
        else:
            # Increase itteration count by one when element not found
            itterationCount += 1

    # When element not found
    returnedTuple = (None, itterationCount)
    return returnedTuple


if __name__ == '__main__':
    aList = [1, 3, 5, 7, 9, 11, 13, 15, 18, 21]
    target = 16
    print(binarySearch(aList, target), 'should be None and three')
    print(linearSearch(aList, target), 'should be None and 10')
    target = 15
    print(binarySearch(aList, target), 'should be 7 and 2')
    print(linearSearch(aList, target), 'should be 7 and 7')














