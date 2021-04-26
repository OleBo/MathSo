"""
A floating-point number is represented approximately with a fixed number of
significant digits and scaled using an exponent in some fixed base.
"""


def positional2decimal(number, base):
    r"""convert a number from a certain positional notation to decimal.

    .. math::
       x = \sum_{k=-\infty}^n a_k b^k =: (a_n a_{n-1} \ldots a_1 a_0 \, . \,
       a_{-1} a_{-2} \ldots)_b

    for :math:`n\in\mathbb{Z}`, :math:`0\le a_k < b` are the numeral digits,
    for :math:`0\le k` before and :math:`k<0` after the decimal point in the
    fixed point system.

    :number: initial number (given as a string)
    :base: from binary all the way to *hexa*trigesimal base :math:`b\in\N`,
    :math:`b>1`

    """
    number_dec = 0
    val = '0123456789abcdefghijklmnopqrstuvwxyz'

    for exp, digit in enumerate(number.split('.')[0][::-1]):
        factor = val.find(digit)
        number_dec += factor * base ** exp
    if '.' in number:
        for exp, digit in enumerate(number.split('.')[1][::1]):
            factor = val.find(digit)
            number_dec += factor * base ** (-exp-1)
    return number_dec
