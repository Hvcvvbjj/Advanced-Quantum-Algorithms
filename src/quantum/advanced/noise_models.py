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
        """Mix the state with maximally mixed with probability ``p``."""
        dim = 2 ** circuit.num_qubits
        mixed = np.ones(dim) / np.sqrt(dim)
        circuit.state = (1 - self.p) * circuit.state + self.p * mixed


class AmplitudeDamping(NoiseModel):
    """Amplitude damping channel applied independently to each qubit."""

    def __init__(self, gamma: float):
        if not 0.0 <= gamma <= 1.0:
            raise ValueError("gamma must be between 0 and 1")
        self.gamma = gamma

    def apply(self, circuit: QuantumCircuit) -> None:
        """Apply amplitude damping with parameter ``gamma``."""
        n = circuit.num_qubits
        state = circuit.state.copy()
        for q in range(n):
            damped = np.zeros_like(state)
            sqrt_keep = np.sqrt(1 - self.gamma)
            sqrt_decay = np.sqrt(self.gamma)
            for idx, amp in enumerate(state):
                if amp == 0:
                    continue
                bit = (idx >> q) & 1
                if bit == 0:
                    damped[idx] += amp
                else:
                    damped[idx] += sqrt_keep * amp
                    damped[idx & ~(1 << q)] += sqrt_decay * amp
            state = damped
        circuit.state = state
