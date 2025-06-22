"""Run the quantum teleportation demonstration."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from algorithms.teleportation import example_usage

if __name__ == "__main__":
    example_usage()
