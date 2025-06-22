"""Quantum autoencoder stubs."""

class QuantumAutoencoder:
    """Compress quantum data into a lower dimensional representation."""

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits

    def encode(self, state):
        """Return encoded representation of ``state``."""
        raise NotImplementedError

    def decode(self, compressed):
        """Reconstruct original state from ``compressed``."""
        raise NotImplementedError
