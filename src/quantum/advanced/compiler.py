"""Prototype compiler translating circuits to hardware instructions."""

from quantum import QuantumCircuit


class QuantumCompiler:
    """Experimental quantum compiler interface."""

    def compile(self, circuit: QuantumCircuit):
        """Compile ``circuit`` to hardware-specific instructions."""
        instructions = []
        for op in getattr(circuit, "operations", []):
            kind = op[0]
            if kind == "gate":
                _, gate, qubits = op
                name = _gate_name(gate)
                instructions.append(f"APPLY {name} {qubits}")
            elif kind == "two_qubit":
                _, gate, c, t = op
                name = _gate_name(gate)
                instructions.append(f"APPLY2 {name} {c} {t}")
            elif kind == "controlled":
                _, gate, c, t = op
                name = _gate_name(gate)
                instructions.append(f"CTRL {c} {t} {name}")
            elif kind == "unitary":
                instructions.append("CUSTOM_UNITARY")
        return instructions


def _gate_name(mat):
    from quantum.gates import H, X, S, T, I

    known = {
        id(H): "H",
        id(X): "X",
        id(S): "S",
        id(T): "T",
        id(I): "I",
    }
    return known.get(id(mat), "U")
