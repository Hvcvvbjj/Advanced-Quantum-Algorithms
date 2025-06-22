"""Implementation of quantum teleportation using the circuit simulator."""

import numpy as np

from quantum import QuantumCircuit, H, X, Z, CNOT


def teleport_state(alpha, beta):
    """Teleport a single-qubit state ``alpha|0> + beta|1>`` to qubit 2."""
    norm = np.sqrt(abs(alpha) ** 2 + abs(beta) ** 2)
    if norm == 0:
        raise ValueError("Invalid state")
    alpha, beta = alpha / norm, beta / norm

    qc = QuantumCircuit(3)
    qc.state[0] = alpha
    qc.state[1] = beta

    # Create entangled pair between qubits 1 and 2
    qc.apply_gate(H, [1])
    qc.apply_two_qubit_gate(CNOT, 1, 2)

    # Bell measurement on qubits 0 and 1
    qc.apply_two_qubit_gate(CNOT, 0, 1)
    qc.apply_gate(H, [0])
    bits = qc.measure_qubits([0, 1])

    # Conditional corrections on qubit 2
    if bits[1] == "1":
        qc.apply_gate(X, [2])
    if bits[0] == "1":
        qc.apply_gate(Z, [2])

    return qc


def example_usage():
    alpha, beta = 1 / np.sqrt(3), np.sqrt(2 / 3)
    qc = teleport_state(alpha, beta)
    result = qc.measure_qubits([2])
    print(f"Teleported qubit measurement: {result}")


if __name__ == "__main__":
    example_usage()
