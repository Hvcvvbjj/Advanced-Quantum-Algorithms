"""Prototype compiler translating circuits to hardware instructions."""

from quantum import QuantumCircuit


class QuantumCompiler:
    """Experimental quantum compiler interface."""

    def compile(self, circuit: QuantumCircuit):
        """Compile ``circuit`` to hardware-specific instructions."""
        raise NotImplementedError
