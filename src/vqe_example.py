"""Demonstration of a simple variational quantum eigensolver."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

import numpy as np
from quantum import VariationalCircuit, VariationalQuantumEigensolver, Z


def main():
    ansatz = VariationalCircuit(1, [0.1])
    hamiltonian = Z
    vqe = VariationalQuantumEigensolver(ansatz, hamiltonian, iterations=50)
    energy = vqe.run()
    print(f"Estimated ground state energy: {energy:.3f}")


if __name__ == "__main__":
    main()
