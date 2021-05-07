#!/usr/bin/env python
"""
animates bisection method
"""

import argparse
import logging


def main(args, loglevel):
    """
    Gather our code in a main() function
    """
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    # TODO Replace this with your actual code.
    print("Hello there.")
    logging.info("You passed an argument.")
    logging.debug("Your Argument: %s", args.argument)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Does a thing to some stuff.",
        epilog="As an alternative to the commandline, params can be placed in"
        "a file, one per line, and specified on the commandline like"
        "'%(prog)s @params.conf'.",
        fromfile_prefix_chars='@')
    # TODO Specify your real parameters here.
    parser.add_argument(
        "argument",
        help="pass ARG to the program",
        metavar="ARG")
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