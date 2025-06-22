"""Quantum autoencoder stubs."""

import numpy as np

class QuantumAutoencoder:
    """Compress quantum data into a lower dimensional representation."""

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits

    def encode(self, state):
        """Return encoded representation of ``state``.

        This very small prototype simply truncates the state vector to keep the
        first ``2**(self.num_qubits//2)`` amplitudes, mimicking compression.
        """
        cutoff = 2 ** (self.num_qubits // 2)
        return state[:cutoff]

    def decode(self, compressed):
        """Reconstruct original state from ``compressed`` by padding zeros."""
        full_dim = 2 ** self.num_qubits
        state = np.zeros(full_dim, dtype=complex)
        state[: len(compressed)] = compressed
        return state
