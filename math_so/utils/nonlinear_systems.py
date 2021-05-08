"""
A nonlinear system is a system in which the change of the output is not
proportional to the change of the input.
"""
import logging


def bisection(func, _a, _b, tol, termination_criterion='x'):
    """
    The bisection method uses the intermediate value theorem iteratively to
    find roots.
    """

    # check if a or b is an exact zero
    if func(_a) == 0:
        return _a
    if func(_b) == 0:
        return _b

    if func(_a)*func(_b) > 0:
        raise Exception('f(a) and f(b) must have opposite signs')

    def check_termination_criterion(_x, _a, _b, tol):
        if termination_criterion == 'x':
            return abs(_b - _a) < tol
        if termination_criterion == 'y':
            return abs(func(_x)) < tol
        raise Exception('Unknown termination criterion: {}'
                        .format(termination_criterion))

    _x = .5*(_a + _b)
    k = 0
    terminate = check_termination_criterion(_x, _a, _b, tol)
    while not terminate:
        if func(_x) == 0:  # found exact zero
            break
        if func(_a)*func(_x) > 0:
            _a = _x
        else:
            _b = _x
        _x = .5*(_a + _b)
        k += 1
        logging.info('k={: 2d}, a={: 15.8e}, b={: 15.8e}, x={: 15.8e}, '
                     'f(x)={: 15.8e}'.format(k, _a, _b, _x, func(_x)))
        terminate = check_termination_criterion(_x, _a, _b, tol)

    logging.info('terminated after %s iterations', k)
    logging.info('x = %s, f(x) = %s', _x, func(_x))
    return _x


def newton(func, _df, _x0, tol, maxits=100, termination_criterion='x'):
    """
    The newton method is a root-finding algorithm which produces successively
    better approximations to the roots of a real-valued function.
    """

    if _df(_x0) == 0:
        raise Exception('df(x0) = 0 is not allowed')

    def check_termination_criterion(_x, _dx, tol):
        if termination_criterion == 'x':
            return abs(_dx) < tol
        if termination_criterion == 'y':
            return abs(func(_x)) < tol
        raise Exception('Unknown termination criterion: {}'
                        .format(termination_criterion))

    _x = _x0
    k = 0
    terminate = False
    while k < maxits and not terminate:
        _dx = func(_x)/_df(_x)
        _x -= _dx
        k += 1
        logging.info('k = {:2d}, x = {:15.8e}, f(x) = {:15.8e}, dx = '
                     '{:15.8e}'.format(k, _x, func(_x), _dx))
        terminate = check_termination_criterion(_x, _dx, tol)

    logging.info('terminated after %s iterations', k)
    logging.info('x = %s, f(x) = %s', _x, func(_x))
    return _x


def heron(_a, tol, _x0=None, termination_criterion='x'):
    """
    Method for finding the non-negative, square root of a real number.
    """
    def func(_x):
        return _x**2 - _a

    def dfunc(_x):
        return 2*_x
    if _x0 is None:
        _x0 = _a
    return newton(func, dfunc, _x0, tol,
                  termination_criterion=termination_criterion)


def secant_method(func, _x0, _x1, tol, maxits=100, termination_criterion='x'):
    """
    The secant method is a root-finding algorithm that uses a succession of
    roots of secant lines to better approximate a root of a function
    """

    def check_termination_criterion(_x, _dx, tol):
        if termination_criterion == 'x':
            return abs(_dx) < tol
        if termination_criterion == 'y':
            return abs(func(_x)) < tol
        raise Exception('Unknown termination criterion: {}'
                        .format(termination_criterion))

    _xp = _x0  # xp = previous approximation
    _x = _x1
    k = 0
    terminate = False
    while k < maxits and not terminate:
        _dx = func(_x)*(_x - _xp)/(func(_x) - func(_xp))
        _x -= _dx
        k += 1
        logging.info('k = {:2d}, x = {:15.8e}, f(x) = {:15.8e}, dx = '
                     '{:15.8e}'.format(k, _x, func(_x), _dx))
        terminate = check_termination_criterion(_x, _dx, tol)

    logging.info('terminated after %s iterations', k)
    logging.info('x = %s, f(x) = %s', _x, func(_x))
    return _x


def regula_falsi(func, _a, _b, tol, termination_criterion='x'):
    """
    The regula falsi, method of false position, or false position method is a
    very old method for solving an equation with one unknown.
    """

    # check if a or b is an exact zero
    if func(_a) == 0:
        return _a
    if func(_b) == 0:
        return _b

    if func(_a)*func(_b) > 0:
        raise Exception('f(a) and f(b) must have opposite signs')

    def check_termination_criterion(_x, _a, _b, tol):
        if termination_criterion == 'x':
            _dx = min(abs(_x - _a), abs(_b - _x))
            return _dx < tol
        if termination_criterion == 'y':
            return abs(func(_x)) < tol
        raise Exception('Unknown termination criterion: {}'
                        .format(termination_criterion))

    k = 0
    _x = _a - func(_a)*(_b - _a)/(func(_b) - func(_a))
    terminate = check_termination_criterion(_x, _a, _b, tol)
    while not terminate:
        if func(_x) == 0:  # found exact zero
            break
        if func(_a)*func(_x) > 0:
            _a = _x
        else:
            _b = _x
        _x = _a - func(_a)*(_b - _a)/(func(_b) - func(_a))

        k += 1
        logging.info('k={: 2d}, a={: 15.8e}, b={: 15.8e}, x={: 15.8e}, '
                     'f(_x)={: 15.8e}'.format(k, _a, _b, _x, func(_x)))
        terminate = check_termination_criterion(_x, _a, _b, tol)

    logging.info('terminated after %s iterations', k)
    logging.info('x = %s, f(x) = %s', _x, func(_x))
    return _x


def fpiterate(func, _x0, tol, maxits=100):
    """
    fixed-point iteration is a method of computing fixed points of a function
    """
    _xp = _x0  # previous approximation
    _x = _x0
    k = 0
    while k < maxits and (k == 0 or abs(_x - _xp) > tol):
        _xp = _x
        _x = func(_x)
        k += 1
        logging.info('k = {:2d}, x = {:15.8e}'.format(k, _x))
    logging.info('terminated after %s iterations', k)
    logging.info('x = %s f(x) = %s', _x, func(_x))
    return _x
