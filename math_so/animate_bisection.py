#!/usr/bin/env python
"""
animates bisection method
"""

import argparse
import logging
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


def sgn(_x):
    """
    sgn: returns the sign of x
    """
    if _x > 0:
        return 1
    if _x < 0:
        return -1
    return 0


def bisect(_f, _a, _b):
    """
    bisec: splitts the interval
    """
    _fa = _f(_a)
    _p = _a+(_b-_a)/2
    _fp = _f(_p)
    if sgn(_fa) == sgn(_fp):
        return _p, _b
    return _a, _p


def bisection_method(_f, _a, _b, _n):
    """
    bisection_method: calls bisec n times
    """
    for _ in range(_n):
        _a, _b = bisect(_f, _a, _b)
    return _a, _b


def animate_bisection(_f, xmin, xmax):
    """
    animates the bisection method
    """
    yrange = _f(xmin), _f(xmax)
    ymin, ymax = min(yrange), max(yrange)
    _x = np.linspace(xmin, xmax)
    _y = _f(_x)
    # Initialize figure
    fig = plt.figure()
    _ax = plt.axes(xlim=(xmin-0.1, xmax+0.1), ylim=(ymin, ymax))
    curve, = _ax.plot([], [], color='blue')
    left, = _ax.plot([], [], color='red')
    right, = _ax.plot([], [], color='red')

    # Figure reset between frames
    def init():
        left.set_data([], [])
        right.set_data([], [])
        curve.set_data([], [])
        return left, right, curve

    # Animation of bisection
    def animate(i):
        _a, _b = bisection_method(_f, xmin, xmax, i)
        logging.info("i: %s, delta_x: %s, delta_y: %s", i, _b-_a,
                     abs(_f(_a)-_f(_b)))
        logging.debug("a: %s, b: %s", _a, _b)
        left.set_data([_a, _a], [ymin, ymax])
        right.set_data([_b, _b], [ymin, ymax])
        curve.set_data(_x, _y)
        return left, right, curve

    animi = animation.FuncAnimation(fig, animate, init_func=init, frames=15,
                                    interval=700, blit=True)
    logging.debug("You animation: %s", animi)

    plt.grid()
    plt.show()


def main(args, loglevel):
    """
    Gather our code in a main() function
    """
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    logging.info("You passed arguments.")
    logging.debug("Your Arguments: %s", args)
    # _f = lambda x: eval(args.function_of_x)  # eval is bad style

    def _f(_x):
        return _x**2-3

    xmin, xmax = args.lower_bound, args.upper_bound
    logging.debug("f(xmin): %s, f(xmax): %s", _f(xmin), _f(xmax))
    animate_bisection(_f, xmin, xmax)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Animates bisection method for f(x)=x^2-3.",
        epilog="As an alternative to the commandline, params can be placed in"
        "a file, one per line, and specified on the commandline like"
        "'%(prog)s @params.conf'.",
        fromfile_prefix_chars='@')
    # parser.add_argument(
    #     "function_of_x",
    #     help="pass FUNC to the program",
    #     metavar="FUNC")
    parser.add_argument(
        "lower_bound",
        help="pass LB to the program",
        metavar="LB",
        type=float)
    parser.add_argument(
        "upper_bound",
        help="pass UB to the program",
        metavar="UB",
        type=float)
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    argv = parser.parse_args()

    # Setup logging
    if argv.verbose:
        LOGLEVEL = logging.DEBUG
    else:
        LOGLEVEL = logging.INFO

    main(argv, LOGLEVEL)
