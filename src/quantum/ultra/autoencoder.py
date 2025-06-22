"""Quantum autoencoder stubs."""

import numpy as np

class QuantumAutoencoder:
    """Compress quantum data into a lower dimensional representation."""

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.parameters = np.zeros(num_qubits // 2)

    def encode(self, state):
        """Return encoded representation of ``state``.

        This very small prototype simply truncates the state vector to keep the
        first ``2**(self.num_qubits//2)`` amplitudes, mimicking compression.
        """
        cutoff = 2 ** (self.num_qubits // 2)
        phases = np.exp(1j * self.parameters)
        return state[:cutoff] * phases

    def decode(self, compressed):
        """Reconstruct original state from ``compressed`` by padding zeros."""

        full_dim = 2 ** self.num_qubits
        phases = np.exp(-1j * self.parameters)
        state = np.zeros(full_dim, dtype=complex)
        state[: len(compressed)] = compressed * phases
        return state

    def train(self, data, epochs: int = 100, lr: float = 0.1):
        params = self.parameters
        m = len(data)
        for _ in range(epochs):
            grad = np.zeros_like(params, dtype=float)
            for state in data:
                compressed = self.encode(state)
                reconstructed = self.decode(compressed)
                diff = reconstructed - state
                grad += 2 * np.imag(compressed * diff[: len(compressed)].conj())
            params -= lr * grad / m
        self.parameters = params
