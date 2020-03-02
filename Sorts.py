"""
This module contains sorting algorithms.
Student Name: Michael Fourie
Student Number: 20102203
"""


def swap(aList, x, y):
    """Exchanges the values of a[x] and a[y]"""
    aList[x], aList[y] = aList[y], aList[x]


def bubbleSort(aList):
    """
    Bubble sort algorithm.
    Input: a list of unsorted values
    Output: a count of sorts made
    """
    swapped = True

    # Holds count of sorts made
    count = 0

    while swapped:
        swapped = False
        for i in range(1, len(aList)):
            if aList[i - 1] > aList[i]:
                swap(aList, i - 1, i)
                swapped = True
            count += 1
    # Returns count of sorts made
    return count


def bubbleSortOpt(aList):
    """
    Sorts list a into ascending order by value.
    This version avoids unnecessary passes over already sorted elements at the end of the list.
    Input: a list of unsorted values
    Output: a count of sorts made
    """
    # Holds count of comparisons
    count = 0

    n = len(aList)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if aList[i - 1] > aList[i]:
                swap(aList, i - 1, i)
                swapped = True
            count += 1  # for analysis only
        n -= 1
    # Returns count of sorts made
    return count


def selectionSort(aList):
    """
    Sorts list a in ascending order by value.
    Input: list of unsorted values
    Output: count of sorts made
    """
    n = len(aList)
    # Holds count of swaps
    count = 0
    for i in range(n - 1):
        min = i;
        for j in range(i + 1, n):
            if (aList[j] < aList[min]):
                min = j;
            # Add value to count variable
            count += 1
        if (min != i):
            swap(aList, i, min)
    return count


def insertionSort(aList):
    """
    This sorts a list in ascending order by values
    Input: list of unsorted values
    Output: count of sorts made
    """

    # Count number of sorts
    count = 0

    for i in range(1, len(aList)):
        # use j to itterate through the list from position i towards position 0
        j = i
        while (j > 0) and (aList[j - 1] > aList[j]):
            # if the element on the left is larger, swap the items
            aList[j - 1], aList[j] = aList[j], aList[j - 1]
            # Add value to count variable
            count += 1
            j = j - 1
    return count


if __name__ == '__main__':
    aList = [5, 2, 13, 425, 34, 76, 975, 34576, 46, 64, 245, 7, 13]
    print(aList, 'list unsorted')
    print(bubbleSort(aList), 'sorts made to sort the list.\nSorted list: ', aList)

    print('')

    aList = [5, 2, 13, 425, 34, 76, 975, 34576, 46, 64, 245, 7, 13]
    print(aList, 'list unsorted')
    print(bubbleSort(aList), 'sorts made to sort the list.\nSorted list: ', aList)

    print('')

    aList = [5, 2, 13, 425, 34, 76, 975, 34576, 46, 64, 245, 7, 13]
    print(aList, 'list unsorted')
    print(selectionSort(aList), 'sorts made to sort the list.\nSorted list: ', aList)

    print('')

    aList = [5, 2, 13, 425, 34, 76, 975, 34576, 46, 64, 245, 7, 13]
    print(aList, 'list unsorted')
    print(insertionSort(aList), 'sorts made to sort the list.\nSorted list: ', aList)










