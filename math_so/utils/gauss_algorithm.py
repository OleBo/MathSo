"""
Gaussian elimination: solves systems of linear equation with n unknowns

A given system is first transformed to Upper Triangular Matrix by row
operations then solution is obtained by Backward Substitution.
"""
import numpy as np
from math_so.utils import signif


def backsubst(utm, rhs, significant_digits):
    """Backsubstitution: returns rounded x vector of system :math:`Ax=b`.

    Calculates the solution of the linear systems of equations from the upper
    triangular matrix and the right hand side vector and rounds to a given
    number of significant digits.

    :utm: upper triangular nxn-matrix
    :rhs: n-vector of right hand side of the equations
    :significant_digits: number of digits to round
    :returns: vector x of dimension n

    """
    _n = len(rhs)  # Indizes 0,1,...,n-1
    if np.shape(utm) != (_n, _n):
        raise Exception("Dimensionen von U und y passen nicht")
    _x = np.zeros(_n)
    for i in range(_n-1, -1, -1):
        _x[i] = rhs[i]
        for k in range(i+1, _n):
            _x[i] = signif(_x[i] - signif(utm[i, k]*_x[k], significant_digits),
                           significant_digits)
        _x[i] = signif(_x[i]/utm[i, i], significant_digits)
    return np.array([_x]).T  # Spaltenvektor


def forwsubst(ltm, rhs, significant_digits):
    """Forwardsubstitution: Docstring for forwsubst.

    :ltm: lower triangular nxn-matrix
    :rhs: n-vector of right hand side of the equations
    :significant_digits: number of digits to round
    :returns: intermediate vector y of dimension n
    """
    _n = len(rhs)  # Indizes 0,1,...,n-1
    if np.shape(ltm) != (_n, _n):
        raise Exception("Dimensionen von L und b passen nicht")
    _y = np.zeros(_n)
    for i in range(1, _n):
        _y[i] = rhs[i]
        for j in range(0, i):
            _y[i] = signif(_y[i] - signif(ltm[i, j]*_y[j], significant_digits),
                           significant_digits)
        _y[i] = signif(_y[i]/ltm[i, i], significant_digits)
    return np.array([_y]).T  # Spaltenvektor
