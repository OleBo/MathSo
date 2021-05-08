"""
When your package is installed in editable mode, you can call
instances of that package from any directory. For example, this
script may be run by calling

     python scripts/animate_bisection.py

#and it will call methods inside our python_ml_template project.
"""
import math
import numpy as np
from math_so import animate_bisection


if __name__ == '__main__':
    animate_bisection(lambda x: np.exp(-x) - np.sin(x), 0, 5*math.pi)
