"""Simplified noise model abstractions."""

from quantum import QuantumCircuit


class NoiseModel:
    """Base class for circuit noise models."""

    def apply(self, circuit: QuantumCircuit) -> None:
        raise NotImplementedError


class DepolarizingChannel(NoiseModel):
    """Depolarizing channel affecting all qubits equally."""

    def __init__(self, probability: float):
        self.p = probability

    def apply(self, circuit: QuantumCircuit) -> None:
        raise NotImplementedError
