"""Simplified noise model abstractions."""

from quantum import QuantumCircuit
import numpy as np


class NoiseModel:
    """Base class for circuit noise models."""

    def apply(self, circuit: QuantumCircuit) -> None:
        """Apply the noise model to ``circuit`` in place.

        The base implementation performs no modification and allows derived
        classes to override this method.
        """
        pass


class DepolarizingChannel(NoiseModel):
    """Depolarizing channel affecting all qubits equally."""

    def __init__(self, probability: float):
        self.p = probability

    def apply(self, circuit: QuantumCircuit) -> None:
        # Apply depolarizing noise by mixing state with maximally mixed state
        dim = 2 ** circuit.num_qubits
        mixed = np.ones(dim) / np.sqrt(dim)
        circuit.state = (1 - self.p) * circuit.state + self.p * mixed
