import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

UPPER_BOUNDARY = 10
LOWER_BOUNDARY = -10
STEP_SIZE = 0.1
INSIDE_COLOR = "g"
OUSIDE_COLOR = "b"


def compute(a, b, max_x):
    z = complex(a, b)
    try:
        x = abs((z - 1) / (z + 1))
    except ZeroDivisionError:
        return a, b, OUSIDE_COLOR
    if x < max_x:
        return a, b, INSIDE_COLOR

    else:
        return a, b, OUSIDE_COLOR


if __name__ == '__main__':
    green_list_x = []
    green_list_y = []
    blue_list_x = []
    blue_list_y = []
    UPPER_BOUNDARY = 5
    LOWER_BOUNDARY = -5
    STEP_SIZE = 0.01
    RADIUS = 0.5
    for m in [0.5, 1, 2]:
        RADIUS = m
        for i in np.arange(LOWER_BOUNDARY, UPPER_BOUNDARY, STEP_SIZE):
            for i2 in np.arange(LOWER_BOUNDARY, UPPER_BOUNDARY, STEP_SIZE):
                x = compute(i, i2, RADIUS)
                if x[2] == INSIDE_COLOR:
                    green_list_x.append(x[0])
                    green_list_y.append(x[1])
                elif x[2] == OUSIDE_COLOR:
                    blue_list_x.append(x[0])
                    blue_list_y.append(x[1])
        plt.scatter(green_list_x, green_list_y, c=INSIDE_COLOR)
        print()
        plt.scatter(blue_list_x, blue_list_y, c=OUSIDE_COLOR)
        plt.savefig("Radius = " + str(RADIUS) + "Ferdinand_vergewaltigt_python.png")
        plt.clf()
        print("completed = ", RADIUS)
