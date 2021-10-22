import math
import numpy as np
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

def gauss4(x_arr, mu, sigma):
    """
    GAUSS4 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x, where x may be an array
    """
    fd = []
    for x in x_arr:
            a=1/2*((x - mu)/sigma)**2
            e=math.exp(-a)
            fd.append((1/(sigma*math.sqrt(2*math.pi))) * e)
    return np.array(fd)
    
def gauss5(x, mu, sigma):
    """
    GAUSS5 Evaluates Gaussian normal distribution with mean mu and standard
    deviation sigma at x, where x may be an array
    """
    return math.exp(-1/2*(np.linalg.matrix_power((x - mu)/sigma),2))/(sigma*math.sqrt(2*math.pi))

def angle(a, b):
    """
    ANGLE computes the angle between two vectors a and b in R^2
    """
    adotb = np.sum(a*b)            # or np.dot(a,b)
    norma = np.sqrt(np.sum(a*a));  # or np.linalg.norm(a)
    normb = np.sqrt(np.sum(b*b));  # or np.linalg.norm(b)
    return np.arccos(adotb/(norma*normb)); 
