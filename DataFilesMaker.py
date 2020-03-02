"""
This module will get two lists of some user-specified size from the list maker module.
One will be sorted and one will not be. It will then colllect data from the search and
modules.
Student Name: Michael Fourie
Student Number: 20102203
"""
import ListMaker
import Searches
import Sorts


# Run this function to start the program
def getLists():
    """
    This module gets the lists based on the users input
    Input: integer from suer
    Output: two lists, one sorted one unsorted
    """

    # The following code will get a user submitted length for the lists, being atleast 100 elements long.
    listLength = 0
    while listLength < 100:
        listLength = int(input("Please indicate the length of the list, being atleast 100 elements long: "))
        if listLength < 100:
            print('Enter a value of atleast 100 elements.')

    # This code will get two lists, one sorted and one unsorted, of the length indicated by the user
    minValue = -10 * listLength  # This code will get an appropriate min range value based on what the user had entered
    maxValue = 10 * listLength  # This code will get an appropriate max range value based on what the user had entered
    unsortedList = ListMaker.unorderdIntegers(minValue, maxValue, listLength)
    sortedList = ListMaker.orderdIntegersAscending(minValue, maxValue, listLength)

    # run searchData to get data from search algorithms
    searchData(unsortedList, sortedList)

    # run sortData to get data from the sorting algorithms
    sortData(unsortedList)


def searchData(unsortedList, sortedList):
    """
    This function runs the two searching algorithms and tracks there data.
    Input: Sorted and unsorted list
    Output: text file of data
    """
    # Begin by testing the binary search
    binarySearchData = []
    linearSearchData = []

    # the range of testing the list begins at zero
    testRange = 0

    # get a value that is known not to be in the list
    target = 0
    while target in sortedList:
        target += 1

    for i in range(len(sortedList) + 1):
        binarySearchCount = Searches.binarySearch(sortedList[:testRange], target)
        binarySearchData.append(binarySearchCount[1])

        linearSearchCount = Searches.linearSearch(sortedList[:testRange], target)
        linearSearchData.append(linearSearchCount[1])

        testRange += 1

    # Wrtie the search data to text file
    writeSearchDataToText(binarySearchData, linearSearchData)


def sortData(unsortedList):
    """
    This function will run the sorting algortihms, and track their data.
    Input: unsorted list
    Output: data from the sorting algorithms
    """
    # We will begin with the data from the bubble sort
    bubbleSortData = []
    bubbleSortOptData = []
    selectionSortData = []
    insertionSortData = []

    # The range of testing will begin at zero
    testRange = 0

    for i in range(len(unsortedList) + 1):
        bubbleSortCount = Sorts.bubbleSort(unsortedList[:testRange])
        bubbleSortData.append(bubbleSortCount)

        bubbleSortOptCount = Sorts.bubbleSortOpt(unsortedList[:testRange])
        bubbleSortOptData.append(bubbleSortOptCount)

        selectionSortCount = Sorts.selectionSort(unsortedList[:testRange])
        selectionSortData.append(selectionSortCount)

        insertionSortCount = Sorts.insertionSort(unsortedList[:testRange])
        insertionSortData.append(insertionSortCount)
        testRange += 1

    # Write the sort data to text file
    writeSortDataToText(bubbleSortData, bubbleSortOptData, selectionSortData, insertionSortData)


def writeSearchDataToText(binarySearchData, linearSearchData):
    """
    This function will write the data colected from the previosu function
    and write it onto a text file
    Input: linear and binary search data
    Output: two text files
    """

    # Write data from binary search
    binarySearchFile = open('binary_search.txt', 'w')
    for i in range(len(binarySearchData)):
        binarySearchFile.write(str(binarySearchData[i]))
        binarySearchFile.write('\n')

    # Write data from linear search
    linearSearchFile = open('linear_search.txt', 'w')
    for i in range(len(linearSearchData)):
        linearSearchFile.write(str(linearSearchData[i]))
        linearSearchFile.write('\n')


def writeSortDataToText(bubbleSortData, bubbleSortOptData, selectionSortData, insertionSortData):
    """
    This module will write the data from the sorting algorithms to text files
    Input: Data from each sorting algorithm
    Output: text files written, holding the data
    """

    # Write data from bubble sort
    bubbleSortFile = open('bubble_sort.txt', 'w')
    for i in range(len(bubbleSortData)):
        bubbleSortFile.write(str(bubbleSortData[i]))
        bubbleSortFile.write('\n')

    # Write data from bubble sort opt
    bubbleSortOptFile = open('optimized_bubble_sort.txt', 'w')
    for i in range(len(bubbleSortOptData)):
        bubbleSortOptFile.write(str(bubbleSortOptData[i]))
        bubbleSortOptFile.write('\n')

    # Write data from selection sort
    selectionSortFile = open('selection_sort.txt', 'w')
    for i in range(len(selectionSortData)):
        selectionSortFile.write(str(selectionSortData[i]))
        selectionSortFile.write('\n')

    # Write data from insertion sort
    insertionSortFile = open('insertion_sort.txt', 'w')
    for i in range(len(insertionSortData)):
        insertionSortFile.write(str(insertionSortData[i]))
        insertionSortFile.write('\n')


if __name__ == '__main__':
    getLists()
    print('This function runs all the subsequent functions below it.')
    print('This will create all text files to be used, and stored on the local disk.')
