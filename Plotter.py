import tkinter

# Default settings - These values should not be changed.
DEFAULT_CANV_WIDTH = 650
DEFAULT_CANV_HEIGHT = 650
MIN_CANV_WIDTH = 100
MIN_CANV_HEIGHT = 100
DEFAULT_SCALE_X = 40
DEFAULT_SCALE_Y = 40
DEFAULT_BACKGROUND = 'mint cream'


# For other colour possibilities, visit
# http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png

def plot(title='Plot',
         canv_width=DEFAULT_CANV_WIDTH,
         canv_height=DEFAULT_CANV_HEIGHT,
         origin_x=DEFAULT_CANV_WIDTH // 2,
         origin_y=DEFAULT_CANV_HEIGHT // 2,
         scale_x=DEFAULT_SCALE_X,
         scale_y=DEFAULT_SCALE_Y,
         bg=None):
    """Creates a window consisting of a title bar and a blank tkinter canvas.
    Returns a tuple of functions that give the programmer controlled access to
    the canvas and its window.

    Parameters (all optional):

        title (defaults to 'Plot') - Becomes the title showing in the window's
            title bar.

        canv_width (defaults to DEFAULT_CANV_WIDTH) - The intended width of the
            canvas in pixels.

        canv_height (defaults to DEFAULT_CANV_HEIGHT) - The intended height of
            the canvas in pixels.

        origin_x (defaults to the horizontal middle of the canvas) -
            The intended horizontal position of 0. origin_x is set realtive to
            the left edge of the canvas.

        origin_y (defaults to the vertical middle of the canvas) -
            The intended vertical position of 0. origin_y is set relative to
            the bottom edge of the canvas.

        Note about origin_x and origin_y: In the tkinter coordinate system,
        position (x=0,y=0) (the origin) is fixed at the top left corner of a
        canvas, and y coordinate values increase downwards. This means, for
        example, that the pixel at (x=10,y=8) is directly below the pixel at
        (x=10,y=7). This function, however, has y coordinate values growing
        upwards and allows the origin to be placed arbitrarily.

        scale_x (defaults to DEFAULT_SCALE_X) - Determines the number
            pixels that represent a unit measurement in the x (horizontal)
            direction. This value is allowed to be fractional, e.g., 0.25, but
            not 0 or negative.

        scale_y (defaults to DEFAULT_SCALE_Y) - Determines the number
            pixels that represent a unit measurement in the y (vertical)
            direction. This value is allowed to be fractional, e.g., 0.25, but
            not 0 or negative.

        bg (defaults to None) - Determines the background colour of the
            canvas. A setting of None produces tkinter's default canvas colour.

    Returned values:

    This function returns a tuple of functions that interact with the canvas
    or its encompassing window as follows:

        draw_axes()

        plot_point()

        plot_function()

        put_text()

        destroy() - Maps to the tkinter .destroy() method. Not needed if it is
            intended that the user close the window in some other way (e.g.,
            with a mouse click on the title bar's close window icon).

        mainloop() - Maps to the tkinter .mainloop() method. Blocks further
            execution until the window is closed.

    See the first four functions' own docstring comments for additional details.
    """
    # Check for and reject bad parameter values.
    if canv_width <= MIN_CANV_WIDTH or canv_height <= MIN_CANV_HEIGHT:
        raise ValueError('Specified canvas is too small.')
    if scale_x <= 0.0:
        raise ValueError('scale_x set less than or equal to 0.0.')
    if scale_y <= 0.0:
        raise ValueError('scale_y set less than or equal to 0.0.')

    master = tkinter.Tk()
    master.title(title)
    canv = tkinter.Canvas(master,
                          width=canv_width + 1,
                          height=canv_height + 1,
                          bd=0,
                          highlightthickness=0,
                          background=bg)
    canv.config()
    canv.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    # Move plot window to foreground.
    # Source: https://stackoverflow.com/questions/1892339/how-to-make-a-tkinter-window-jump-to-the-front
    master.lift()
    master.attributes('-topmost', True)
    master.after_idle(master.attributes, '-topmost', False)

    canv.update()

    min_x = -origin_x
    max_x = canv_width - origin_x
    min_y = -origin_y
    max_y = canv_height - origin_y

    def get_x(x_val):
        """Returns x_val mapped into the tkinter coordinate system."""
        return x_val + origin_x

    def get_y(y_val):
        """Returns y_val mapped into the tkinter coordinate system."""
        return canv_height - y_val - origin_y

    def plot_point(x=0, y=0, diam=2, colour='black'):
        """Puts a dot on the canvas.

        Parameters (all optional):

            x (defaults to 0) - The horizontal position.

            y (defaults to 0) - The vertical position.

            diam (defaults to 2) - The diameter of the dot.

            colour (defaults to 'black') - The colour of the dot.
        """
        x = get_x(x * scale_x) - diam // 2
        y = get_y(y * scale_y) - diam // 2
        canv.create_oval(x, y, x + diam, y + diam, outline=colour, fill=colour)

    def plot_function(fn, point_diam=2, colour='black'):
        """Draws a function of the form y = f(x) on the canvas.

        Parameters:

            fn - the function (Note: NOT a string; the corresponding argument
                should be a function identifier and not appear in quotes.)

            point_diam (optional, defaults to 2) - the size of each plotted
                dot used to draw the function.

            colour (optional, defaults to 'black') - the colour of each
                plotted dot.
        """
        for screen_x in range(min_x, max_x + 1):
            x = screen_x / scale_x
            # The try-except, below, ensures that nothing gets plotted when
            # a call to fn(x) triggers an exception. This allows functions
            # with limited ranges to get plotted.
            try:
                plot_point(x, fn(x), diam=point_diam, colour=colour)
            except:
                pass

    def draw_axes(line_width=1, colour='black', tick_length=0,
                  tick_interval_x=1, tick_interval_y=1):
        """Draws x and y axes so that they intersect at the origin. Adds ticks
        at regular intervals, optionally.

        Parameters (all optional):

            line_width (defaults to 1) - The width of the axis lines in pixels.

            colour (defaults to 'black') - The colour used to draw the axes

            tick_length (defaults to 0) - The length of tick marks in pixels.
                A value of 0 causes tick marks to be omitted. Positive values
                cause tick marks to appear along the top of the x axis and on
                the right of the y axis; negative values cause tick marks to
                appear along the bottom of the x axis and on the left of the
                y axis.

            tick_interval_x (defaults to 1) - The number of units separating
                ticks in the x (horizontal) direction. Non-integer values
                (like math.pi) are allowed. Ignored if tick_length is 0.

            tick_interval_y (defaults to 1) - The number of units separating
                ticks in the y (vertical) direction. Non-integer values
                are allowed. Ignored if tick_length is 0.

        """
        # Draw x axis
        canv.create_line(0, get_y(0), canv_width + 1, get_y(0), fill=colour)

        # Draw y axis
        canv.create_line(get_x(0), canv_height, get_x(0), -1, fill=colour)

        # Draw ticks
        if tick_length != 0:
            # Check for and reject invalid tick intervals
            if tick_interval_x < 1:
                raise ValueError('Inappropriate tick_interval_x value.')
            if tick_interval_y < 1:
                raise ValueError('Inappropriate tick_interval_y value.')
            x = tick_interval_x
            start_tick = int(tick_length // abs(tick_length))
            end_tick = start_tick * abs(tick_length) + start_tick
            while get_x(x * scale_x) < canv_width:
                # positive x tick
                canv.create_line(get_x(x * scale_x),
                                 get_y(start_tick),
                                 get_x(x * scale_x),
                                 get_y(end_tick),
                                 fill=colour)
                # negative x tick
                canv.create_line(get_x(-x * scale_x),
                                 get_y(start_tick),
                                 get_x(-x * scale_x),
                                 get_y(end_tick),
                                 fill=colour)
                x += tick_interval_x
            y = tick_interval_y
            while get_y(y * scale_y) > 0:  # Remember that y grows down.
                # positive y tick
                canv.create_line(get_x(start_tick),
                                 get_y(y * scale_y),
                                 get_x(end_tick),
                                 get_y(y * scale_y),
                                 fill=colour)
                # negative y tick
                canv.create_line(get_x(start_tick),
                                 get_y(-y * scale_y),
                                 get_x(end_tick),
                                 get_y(-y * scale_y),
                                 fill=colour)
                y += tick_interval_y

    def put_text(msg, x=0, y=0, size=None, colour='black'):
        """Draws a text message using the default tkinter font onto the canvas.

        Parameters:

            msg - the message.

            x (optional, default 0) - The x (horizontal) position of the
                left edge of the text.

            y (optional, default 0) - The y (vertical) position of the
                vertical middle of the text.

            size (optional, default None) - The point size of the font used
                for the message. If None, the system default size is used.

            colour (optional, default 'black') - The colour of the font used
                for the message.
        """
        if size is None:  # no change (the initial size is system dependent)
            canv.create_text(get_x(x * scale_x), get_y(y * scale_y),
                             text=msg,
                             fill=colour,
                             anchor='w')
        else:
            canv.create_text(get_x(x * scale_x), get_y(y * scale_y),
                             text=msg,
                             font=('TkDefaultFont', size),
                             fill=colour,
                             anchor='w')
        canv.pack()

    return (draw_axes, plot_point, plot_function, put_text,
            master.destroy, master.mainloop)


if __name__ == '__main__':
    # Testing! Testing!

    # Draw an empty plot and get functions that allow us to add elements to it.
    (draw_axes,
     plot_point,
     plot_function,
     put_text,
     kill,
     pause) = plot(title='Test Plot',
                   origin_x=DEFAULT_CANV_WIDTH // 2,
                   origin_y=DEFAULT_CANV_HEIGHT // 2,
                   bg='bisque')
    # from math import * # Since I'll be using some math library functions
    import math

    # Plot some 10-pixel diameter coloured points
    plot_point(math.pi, 0, 10, 'yellow')
    plot_point(math.pi / 2, 0, 10, 'red')
    plot_point(0, 1, 10, 'blue')
    # Draw the axes. These will be drawn over the coloured points.
    draw_axes(tick_length=-4, tick_interval_x=math.pi)
    plot_function(math.sin, colour='green')
    plot_function(math.cos, colour='purple')
    # Plotting a couple of "anonymous" functions
    plot_function(lambda x: 2 * (x - 2) ** 2 - 3 * x + 1, colour='navy')
    plot_function(lambda x: -4 * x ** 3 - 4, colour='deep pink')
    put_text('Various points and functions', x=-7.5, y=-3, size=16, colour='green')
    pause()  # User must close the canvas window to continue.

    # Plot some anonymous functions on a different canvas
    (drw_axs,
     plt_pnt,
     plt_fn,
     put_txt,
     destroy,
     wait) = plot(title='2nd Test Plot',
                  scale_x=10,
                  scale_y=10,
                  bg='thistle1')
    drw_axs(tick_length=4, tick_interval_x=5, tick_interval_y=2, colour="orange")
    plt_fn(lambda x: x ** 2 if (x >= 0) else None, colour='green')
    put_txt('y = x**2, for x >= 0', 40, 100, size=14, colour='green')
    plt_fn(lambda x: math.log(x, 10) if (x > 0) else None, colour='blue')
    put_txt('log(x, 10) for x > 0', 100, 60, size=9, colour='blue')
    put_txt('This is a test using put_txt()\'s defaults.')
    wait()  # Module exits when user closes the canvas window.
