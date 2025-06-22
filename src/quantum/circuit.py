"""Minimal quantum circuit simulator using numpy."""

from functools import reduce
import numpy as np

from .gates import I


def tensor(*matrices):
    """Kronecker product of a list of matrices."""
    return reduce(np.kron, matrices)


def apply_single_qubit_gate(state, gate, qubit, n):
    """Apply a single-qubit gate without constructing full 2^n matrix."""
    state = state.reshape([2] * n)
    state = np.moveaxis(state, qubit, 0)
    state = (gate @ state.reshape(2, -1)).reshape([2] + [2] * (n - 1))
    state = np.moveaxis(state, 0, qubit)
    return state.reshape(2 ** n)


class QuantumCircuit:
    """Simple state-vector simulator."""

    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.state = np.zeros(2 ** num_qubits, dtype=complex)
        self.state[0] = 1

    def apply_gate(self, gate, qubits):
        """Apply a gate to the specified qubits."""
        for q in qubits:
            self.state = apply_single_qubit_gate(self.state, gate, q, self.num_qubits)

    def apply_unitary(self, unitary):
        """Apply a full unitary matrix to the state."""
        self.state = unitary @ self.state

    def measure(self):
        """Sample from the quantum state distribution."""
        probabilities = np.abs(self.state) ** 2
        return np.random.choice(len(probabilities), p=probabilities)
