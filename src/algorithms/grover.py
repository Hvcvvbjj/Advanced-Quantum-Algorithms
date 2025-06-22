"""Skeleton implementation of Grover's search using the quantum circuit module."""

from ..quantum import QuantumCircuit, H


def grover_search(num_qubits, oracle_fn):
    """Return circuit state after a single Grover iteration.

    Parameters
    ----------
    num_qubits: int
        Number of qubits in the search space.
    oracle_fn: callable
        Function that marks the desired state. For now this is a placeholder.
    """
    qc = QuantumCircuit(num_qubits)
    for q in range(num_qubits):
        qc.apply_gate(H, [q])
    # TODO: apply oracle and diffusion operations
    # This function will be expanded in future commits.
    return qc
