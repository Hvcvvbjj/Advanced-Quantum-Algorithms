"""Placeholders for advanced error correction techniques."""

from quantum import QuantumCircuit


class SurfaceCode:
    """Prototype for a surface code implementation."""

    def __init__(self, distance: int):
        self.distance = distance

    def encode(self, circuit: QuantumCircuit) -> None:
        """Encode ``circuit`` using the surface code."""
        raise NotImplementedError

    def decode(self, syndrome):
        """Return a correction based on ``syndrome``."""
        raise NotImplementedError


class StabilizerMeasurement:
    """Utilities for stabilizer measurements."""

    def measure(self, circuit: QuantumCircuit):
        """Return syndrome information for ``circuit``."""
        raise NotImplementedError
