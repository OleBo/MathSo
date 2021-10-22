import math
def interest1(b, p, n):
    """
    INTEREST1(b, p, n) computes the new balance after n years for an initial
    balance b and an annual interest rate p in per cent
    """
    return b*(1 + p/100)**n

def gauss3(x, mu, sigma):
    """
    GAUSS3 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x
    """
    return math.exp(-1/2*((x - mu)/sigma)**2)/(sigma*math.sqrt(2*math.pi))

def gauss4(x, mu, sigma):
    """
    GAUSS4 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x, where x may be a scalar or an array
    """    
    return math.exp(-1/2*((x - mu)/sigma)**2)/(sigma*math.sqrt(2*math.pi))