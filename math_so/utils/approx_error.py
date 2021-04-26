"""
The approximation error in some data is the discrepancy between an exact
value and some approximation to it.
"""
import math


def absolute_error(value, approx):
    r"""This function will calculate the absolute error:

    .. math:: \epsilon = \left|v - v_{approx}\right|
        :label: absolute_error

    :value: some value :math:`v`
    :approx: :math:`v_{approx}` approximation of :math:`v`
    :returns: absolute error :math:`\epsilon` according equation :eq:
    `absolute_error`
    """
    return abs(value - approx)


def relative_error(value, approx):
    r"""This function will calculate the relative error:

    .. math:: \eta = \left|\frac{v - v_{approx}}{v}\right|
        :label: relative_error

    This is also the normalized absolute error (see equation :eq:
    `absolute_error`). There are two features that should be kept in mind:

    - Relative error is undefined when the true value is zero as it appears in
      the denominator.
    - Relative error only makes sense when measured on a ratio scale, (i.e. a
      scale which has a true meaningful zero), otherwise it would be sensitive
      to the measurement units.

    :value: some value :math:`v`
    :approx: :math:`v_{approx}` approximation of :math:`v`
    :returns: relative error :math:`\eta` according equation :eq:
    `relative_error`
    """
    return abs((value - approx)/value)


def signif(number, significant_digits):
    """Rounding a number to n significant digits.

    Rounds a number and includes only the desired number of significant digits.

    Use `round(number, ndigits)` with `number` as the number being rounded
    and `ndigits` as the number of significant digits minus
    `(int(math.floor(math.log10(abs(number)))) - 1)`.
    """
    if number is not None and (number == 0):
        return 0.0
    # is None or not zero
    return round(number, significant_digits
                 - int(math.floor(math.log10(abs(number)))) - 1)
