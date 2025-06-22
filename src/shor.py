"""Simplified Shor's factoring algorithm built on the quantum circuit utilities."""

import numpy as np
from math import gcd

from quantum import H, QuantumCircuit
from quantum.transform import apply_inverse_qft, qft
from quantum.circuit import tensor


def apply_controlled_modexp(state, a, N, n, exponent):
    """Controlled modular exponentiation on the lower n qubits.

    This placeholder applies classical modular exponentiation to each basis
    state. A full implementation would require a reversible quantum modular
    exponentiation circuit."""
    new_state = np.zeros_like(state)
    for idx, amplitude in enumerate(state):
        if amplitude == 0:
            continue
        binary = np.array(list(np.binary_repr(idx, width=2 * n)), dtype=int)
        x_bits = binary[:n]
        aux_bits = binary[n:]
        x = int("".join(x_bits.astype(str)), 2)
        aux = int("".join(aux_bits.astype(str)), 2)
        result = pow(a, x, N)
        if exponent:
            aux = (aux + result) % N
        new_index = int(
            "".join(
                np.concatenate([
                    x_bits,
                    np.array(list(np.binary_repr(aux, width=n)), dtype=int),
                ]).astype(str)
            ),
            2,
        )
        new_state[new_index] += amplitude
    return new_state


def period_finding(a, N):
    """Use the order finding routine to compute period r such that a^r ≡ 1 mod N."""
    n = int(np.ceil(np.log2(N))) * 2
    qc = QuantumCircuit(2 * n)

    # Apply Hadamard to the first n qubits
    for qubit in range(n):
        qc.apply_gate(H, [qubit])

    # Controlled modular exponentiation
    for i in range(n):
        qc.state = apply_controlled_modexp(
            qc.state, pow(a, 2 ** i, N), N, n, exponent=True
        )

    # Apply inverse QFT to the first n qubits
    qc.state = apply_inverse_qft(qc.state, n, 2 * n)

    # Measure the first register
    probabilities = np.abs(qc.state) ** 2
    measurement = np.random.choice(len(probabilities), p=probabilities)
    phase = measurement / (2 ** n)
    for s in range(1, N):
        if abs(phase - round(phase * s) / s) < 1 / (2 * (2 ** n)):
            r = s
            break
    else:
        r = None
    return r


def shor(N):
    if N % 2 == 0:
        return 2
    while True:
        a = np.random.randint(2, N)
        g = gcd(a, N)
        if g > 1:
            return g
        r = period_finding(a, N)
        if r is None or r % 2 != 0:
            continue
        x = pow(a, r // 2, N)
        if x == N - 1:
            continue
        factor = gcd(x + 1, N)
        if factor not in [1, N]:
            return factor


def main():
    N = 15  # Example composite number
    factor = shor(N)
    print(f"Found factor of {N}: {factor}")


if __name__ == "__main__":
    main()
