"""This module handles output of the route taken and the schedule

This file is Copyright (c) 2021 Leen Al Lababidi, Michael Rubenstein, Maria Becerra and Nada Eldin
"""

import tkinter
from schedule import TimeBlock
from location import Location
import random
import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt

COLORS = ['white', 'red', 'cyan', 'yellow', 'green', 'blue']


def print_schedule(schedule: list[TimeBlock], win: tkinter):
    """A
    """
    x_value = 0
    y_value = 0
    space = 75

    for timeblock in schedule:
        name = timeblock.location_visited.name
        start = timeblock.start_time.strftime("%Y-%b-%d (%H:%M:%S.%f)")
        end = timeblock.end_time.strftime("%Y-%b-%d (%H:%M:%S.%f)")
        color = random.choice(COLORS)
        rectangle(x_value, y_value, space, color, win, name, start, end)
        y_value += space


def rectangle(x: int, y: int, space: int, color: str,
              window: tkinter, name: str, start: str, end: str):
    """Creates a rectangle on a tkinter object with the specified parameters.
    """
    window.create_rectangle(x, y, x + 400, y + space, fill=color)
    window.create_text((x + 200, y + space / 4), text=name)
    window.create_text((x + 200, y + (space / 4) * 2), text='Leave: ' + start)
    window.create_text((x + 200, y + (space/4) * 3), text='Return: ' + end)


def open_window_schedule(schedule: list[TimeBlock]) -> None:
    """Opens a window that allows the user to see their final schedule."""
    window = tkinter.Tk()
    mywin = tkinter.Canvas(window, width=400, height=len(schedule) * 100)
    mywin.pack()
    print_schedule(schedule, mywin)
    window.title("Today's Schedule")
    window.geometry("400x" + str(len(schedule) * 100) + "+10+10")
    window.mainloop()


def show_path(path: list[Location]) -> None:
    """Opens a window that allows the user to see the path they have to take.
    """

    bbox = (2.1303, 2.4774, 48.7231, 48.9942)
    ruh_m = image.imread('map.jpg')
    fig, ax = plt.subplots()

    y = np.array([location.location[0] for location in path])
    x = np.array([location.location[1] for location in path])
    n = np.array([location.name for location in path])
    sizes = np.array([10])

    ax.scatter(x, y, s=sizes, color='red')

    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))
    for i in range(0, len(x) - 1):
        ax.plot([x[i], x[i+1]], [y[i], y[i + 1]])

    ax.set_title('Path for Today')
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])
    ax.imshow(ruh_m, zorder=0, extent=bbox, aspect='equal')
