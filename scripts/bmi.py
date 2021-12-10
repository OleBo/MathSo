# When your package is installed in editable mode, you can call
# instances of that package from any directory. For example, this
# script may be run by calling
#
#     python scripts/bmi.py
#
# and it will call methods inside our python_ml_template project.

from math_so.apps.pywebio import bmi

if __name__ == '__main__':
    bmi.main()
