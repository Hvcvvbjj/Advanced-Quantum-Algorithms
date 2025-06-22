"""Basic phase estimation using a rotation gate as the unitary."""

import numpy as np

from quantum import H, X, RZ, QuantumCircuit
from quantum.transform import apply_inverse_qft


def estimate_phase(theta: float, precision: int = 3) -> str:
    """Estimate the phase ``theta`` using ``precision`` qubits."""
    qc = QuantumCircuit(precision + 1)

    # Prepare eigenstate |1> of RZ
    qc.apply_gate(X, [precision])

    for q in range(precision):
        qc.apply_gate(H, [q])

    for q in range(precision):
        angle = 2 ** q * theta
        qc.apply_controlled_gate(RZ(angle), q, precision)

    qc.state = apply_inverse_qft(qc.state, precision, precision + 1)
    result = qc.measure_all()
    return result


def example_usage():
    theta = np.pi / 4
    bits = estimate_phase(theta, precision=3)
    print(f"Estimated phase for theta={theta}: {bits}")


if __name__ == "__main__":
    example_usage()
