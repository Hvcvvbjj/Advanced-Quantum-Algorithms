"""Templates for variational quantum algorithms."""


class VariationalCircuit:
    """Base class for parameterized circuits."""

    def __init__(self, num_qubits: int, parameters):
        self.num_qubits = num_qubits
        self.parameters = list(parameters)

    def construct(self):
        """Construct the circuit using current parameters."""
        raise NotImplementedError


class Optimizer:
    """Simple optimizer interface for variational circuits."""

    def step(self, objective_fn, params):
        raise NotImplementedError
