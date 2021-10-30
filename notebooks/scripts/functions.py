"""
functions
"""

import math
import numpy as np


def interest1(_b, _p, _n):
    """
    INTEREST1(_b, _p, _n) computes the new balance after n years for an initial
    balance b and an annual interest rate p in per cent
    """
    return _b * (1 + _p / 100)**_n


def gauss3(_x, _mu, sigma):
    """
    GAUSS3 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x
    """
    return math.exp(-1 / 2 *
                    ((_x - _mu) / sigma)**2) / (sigma * math.sqrt(2 * math.pi))


def gauss4(x_arr, _mu, sigma):
    """
    GAUSS4 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x, where x may be an array
    """
    _fd = []
    for _x in x_arr:
        _a = 1 / 2 * ((_x - _mu) / sigma)**2
        _e = math.exp(-_a)
        _fd.append((1 / (sigma * math.sqrt(2 * math.pi))) * _e)
    return np.array(_fd)


def gauss5(_x, _mu, sigma):
    """
    GAUSS5 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x, where x may be an array
    """
    return math.exp(-1 / 2 * (np.linalg.matrix_power(
        (_x - _mu) / sigma), 2)) / (sigma * math.sqrt(2 * math.pi))


def angle(_a, _b):
    """
    ANGLE computes the angle between two vectors a and b in R^2
    """
    adotb = np.sum(_a * _b)  # or np.dot(a,b)
    norma = np.sqrt(np.sum(_a * _a))
    # or np.linalg.norm(a)
    normb = np.sqrt(np.sum(_b * _b))
    # or np.linalg.norm(b)
    return np.arccos(adotb / (norma * normb))
