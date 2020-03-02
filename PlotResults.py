"""
This is the plotting module. This module will present the user with a menu, from which they will be able
to choose which algorithm they would like to plot.
Student Name: Michael Fourie
Student Number: 20102203
"""
import Menu
import Plotter
import math
import DataFilesMaker


def plotBinarySearch():
    """
    This function will plot the binary search data
    Input: None
    Output: Binary search data graph
    """
    # Open the text file of binary search data
    binarySearchFile = open("binary_search.txt", "r")

    # Create the plot window
    (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
        Plotter.plot(title='Binary Search',
                     canv_width=650, canv_height=650,
                     origin_x=0, origin_y=0, bg='white')

    draw_axes(tick_length=5)

    # This varaible will increase with one unit for each not plotted point
    xValue = 0

    for line in binarySearchFile:
        plotPoint = int(line)
        xValue += 0.3
        plot_point(x=xValue, y=plotPoint, diam=7, colour='black')

    # Plot a function to closley match the graph
    plot_function(math.log2, point_diam=4, colour='black')

    # Use text to distinguish the function plotted from the data recorded
    put_text('log2(x)', x=10, y=2, colour='black')
    put_text('binary search', x=10, y=7, colour='black')

    # Pause execution until graph is closed
    mainloop()


def plotLinearSearch():
    """
    This function will plot the linear search data
    Input: None
    Output: Linear search data graph
    """
    # Open the text file of linear search data
    linearSearchFile = open("linear_search.txt", "r")

    # Create the plott window
    (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
        Plotter.plot(title='Linear Search',
                     canv_width=650, canv_height=650,
                     origin_x=0, origin_y=0, )

    draw_axes(tick_length=5)

    # This varaible will increase with one unit for each not plotted point
    xValue = -1

    for line in linearSearchFile:
        plotPoint = int(line)
        xValue += 1
        plot_point(x=xValue, y=plotPoint, diam=8, colour='black')

    # Plot a function to closley match the graph
    plot_function(lambda x: x, point_diam=4, colour='black')

    # Use text to distinguish the function plotted from the data recorded
    put_text('f(x) = x', x=7, y=2, colour='black')
    put_text('linear search', x=5, y=4, colour='black')

    # Pause execution until graph is closed
    mainloop()


def plotBubbleSort():
    """
    This function will plot bubble sort.
    Input: None
    Output: Graph of data
    """
    # Open the text file of bubble sort data
    bubbleSortFile = open("bubble_sort.txt", "r")

    # Create the plott window
    (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
        Plotter.plot(title='Bubble Sort',
                     canv_width=650, canv_height=650,
                     origin_x=0, origin_y=0, bg='white')

    draw_axes(tick_length=5)

    # This varaible will increase with one unit for each not plotted point
    xValue = -1

    for line in bubbleSortFile:
        plotPoint = int(line)
        xValue += 1
        plot_point(x=xValue, y=plotPoint, diam=8, colour='black')

    # Plot a function to closley match the graph
    plot_function(lambda x: x ** 2, point_diam=4, colour='black')

    # Use text to distinguish the function plotted from the data recorded
    put_text('f(x) = x^2', x=0.3, y=5, colour='black')
    put_text('bubble sort', x=5, y=7, colour='black')

    # Pause execution until graph is closed
    mainloop()


def plotBubbleSortOpt():
    """
    This function will plot optimized bubble sort.
    Input: None
    Output: Graph of data
    """
    # Open the text file of optimized bubble sort data
    bubbleSortOptFile = open("optimized_bubble_sort.txt", "r")

    # Create the plott window
    (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
        Plotter.plot(title='Bubble Sort Optimized',
                     canv_width=650, canv_height=650,
                     origin_x=0, origin_y=0, bg='white')

    draw_axes(tick_length=5)

    # This varaible will increase with one unit for each not plotted point
    xValue = -1

    for line in bubbleSortOptFile:
        plotPoint = int(line)
        xValue += 1
        plot_point(x=xValue, y=plotPoint, diam=8, colour='black')

    # Plot a function to closley match the graph
    plot_function(lambda x: (0.75 * x ** 2), point_diam=4, colour='black')

    # Use text to distinguish the function plotted from the data recorded
    put_text('f(x) = 0.75x^2', x=0.3, y=5, colour='black')
    put_text('optimized bubble sort', x=6, y=7, colour='black')

    # Pause execution until graph is closed
    mainloop()


def plotInsertionSort():
    """
    This function will plot insertion sort.
    Input: None
    Output: Graph of data
    """
    # Open the text file of insertion sort data
    insertionSortFile = open("insertion_sort.txt", "r")

    # Create the plott window
    (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
        Plotter.plot(title='Insertion Sort',
                     canv_width=650, canv_height=650,
                     origin_x=0, origin_y=0, bg='white')

    draw_axes(tick_length=5)

    # This varaible will increase with one unit for each not plotted point
    xValue = -1

    for line in insertionSortFile:
        plotPoint = int(line)
        xValue += 1
        plot_point(x=xValue, y=plotPoint, diam=8, colour='black')

    # Plot a function to closley match the graph
    plot_function(lambda x: (0.2 * x ** 2), point_diam=4, colour='black')

    # Use text to distinguish the function plotted from the data recorded
    put_text('f(x) = 0.2x^2', x=1, y=5, colour='black')
    put_text('insertion sort', x=7, y=8, colour='black')

    # Pause execution until graph is closed
    mainloop()


def plotSelectionSort():
    """
    This function will plot selection sort.
    Input: None
    Output: Graph of data
    """
    # Open the text file of selection sort data
    selectionSortFile = open("selection_sort.txt", "r")

    # Create the plott window
    (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
        Plotter.plot(title='Selection Sort',
                     canv_width=650, canv_height=650,
                     origin_x=0, origin_y=0, bg='white')

    draw_axes(tick_length=5)

    # This varaible will increase with one unit for each not plotted point
    xValue = -1

    for line in selectionSortFile:
        plotPoint = int(line)
        xValue += 1
        plot_point(x=xValue, y=plotPoint, diam=8, colour='black')

    # Plot a function to closley match the graph
    plot_function(lambda x: (0.5 * x ** 2), point_diam=4, colour='black')

    # Use text to distinguish the function plotted from the data recorded
    put_text('f(x) = 0.5x^2', x=1, y=5, colour='black')
    put_text('selection sort', x=5, y=7, colour='black')

    # Pause execution until graph is closed
    mainloop()


def menuFunction():
    """
    This functionw will present the user with a menu from which they can choose which algorthm
    they would like to plot.
    Input: None
    Output: Chose algorithm will be passed to next function
    """
    # First we must make the text files
    DataFilesMaker.getLists()

    m = ['Binary Search', 'Linear Search', 'Bubble Sort', 'Optimized Bubble Sort', 'Insertion Sort', 'SelectionSort']

    while True:
        c = Menu.do_menu('Plot Results', m)
        if c is None:
            break
        print('\nValid choice:', c)
        if c == 1:
            plotBinarySearch()
        elif c == 2:
            plotLinearSearch()
        elif c == 3:
            plotBubbleSort()
        elif c == 4:
            plotBubbleSortOpt()
        elif c == 5:
            plotInsertionSort()
        elif c == 6:
            plotSelectionSort()


menuFunction()




