"""Templates for variational quantum algorithms."""

import numpy as np
from quantum import QuantumCircuit, RZ

class VariationalCircuit:
    """Base class for parameterized circuits."""

    def __init__(self, num_qubits: int, parameters):
        self.num_qubits = num_qubits
        self.parameters = list(parameters)

    def construct(self):
        """Construct the circuit using current parameters."""
        qc = QuantumCircuit(self.num_qubits)
        for i, theta in enumerate(self.parameters):
            qc.apply_gate(RZ(theta), [i % self.num_qubits])
        return qc


class Optimizer:
    """Simple optimizer interface for variational circuits."""

    def step(self, objective_fn, params):
        lr = 0.1
        grads = np.zeros_like(params, dtype=float)
        for i in range(len(params)):
            plus = params.copy()
            minus = params.copy()
            plus[i] += 1e-3
            minus[i] -= 1e-3
            grads[i] = (objective_fn(plus) - objective_fn(minus)) / 2e-3
        return params - lr * grads


class VariationalQuantumEigensolver:
    """Estimate ground state energy of ``hamiltonian`` using variational ansatz."""

    def __init__(self, ansatz: VariationalCircuit, hamiltonian: np.ndarray, optimizer=None, iterations: int = 100):
        self.ansatz = ansatz
        self.hamiltonian = hamiltonian
        self.optimizer = optimizer or Optimizer()
        self.iterations = iterations

    def _energy(self, params):
        self.ansatz.parameters = list(params)
        circuit = self.ansatz.construct()
        return np.real(circuit.expectation(self.hamiltonian))

    def run(self) -> float:
        params = np.array(self.ansatz.parameters, dtype=float)
        for _ in range(self.iterations):
            params = self.optimizer.step(self._energy, params)
        self.ansatz.parameters = list(params)
        return self._energy(params)
