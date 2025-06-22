"""Skeleton implementation of Grover's search using the quantum circuit module."""

import numpy as np

from quantum import QuantumCircuit, H


def grover_search(num_qubits, oracle_fn):
    """Return circuit state after a single Grover iteration.

    Parameters
    ----------
    num_qubits: int
        Number of qubits in the search space.
    oracle_fn: callable
        Function that marks the desired state. For now this is a placeholder.
    """
    qc = QuantumCircuit(num_qubits)

    # Prepare uniform superposition
    for q in range(num_qubits):
        qc.apply_gate(H, [q])

    # Oracle phase flip
    for idx in range(2 ** num_qubits):
        if oracle_fn(idx):
            qc.state[idx] *= -1

    # Diffusion operator
    size = 2 ** num_qubits
    psi0 = np.ones(size) / np.sqrt(size)
    diffusion = 2 * np.outer(psi0, psi0) - np.eye(size)
    qc.apply_unitary(diffusion)

    return qc


def example_usage():
    """Run a simple two-qubit Grover search."""

    target = 3  # state |11>

    def oracle(index: int) -> bool:
        return index == target

    qc = grover_search(2, oracle)
    result = qc.measure()
    print(f"Grover search result: {result}")


if __name__ == "__main__":
    example_usage()
