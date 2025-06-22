# Quantum circuit simulator implementing Shor's algorithm.
# This implementation is intentionally simplified and optimized for clarity
# rather than performance. It uses numpy to manipulate complex state vectors
# representing quantum registers.

import numpy as np
from functools import reduce
from math import gcd

# Basic single-qubit gates
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
I = np.eye(2, dtype=complex)

# Two-qubit gates
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]], dtype=complex)

def tensor(*matrices):
    """Kronecker product of a list of matrices."""
    return reduce(np.kron, matrices)


def apply_gate(state, gate, qubits, n):
    """Apply quantum gate to specific qubits of n-qubit state."""
    gates = []
    for i in range(n):
        if i in qubits:
            gates.append(gate)
        else:
            gates.append(I)
    U = tensor(*gates)
    return U @ state


def qft(n):
    """Quantum Fourier Transform matrix for n qubits."""
    N = 2 ** n
    omega = np.exp(2j * np.pi / N)
    F = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            F[i, j] = omega ** (i * j)
    return F / np.sqrt(N)


def inverse_qft(n):
    """Inverse Quantum Fourier Transform matrix."""
    return np.conjugate(qft(n).T)


def apply_controlled_modexp(state, a, N, n, exponent):
    """Controlled modular exponentiation on the lower n qubits."""
    # This is a placeholder for the complex arithmetic required
    # to implement modular exponentiation quantumly. For simulation,
    # we simply apply the classical modular exponentiation to the
    # basis states.
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
    """Uses quantum order finding to compute the period r such that a^r ≡ 1 mod N."""
    n = int(np.ceil(np.log2(N))) * 2
    state = np.zeros(2 ** (2 * n), dtype=complex)
    state[0] = 1

    # Apply Hadamard to the first n qubits
    for qubit in range(n):
        state = apply_gate(state, H, [qubit], 2 * n)

    # Controlled modular exponentiation
    for i in range(n):
        state = apply_controlled_modexp(state, pow(a, 2 ** i, N), N, n, exponent=True)

    # Apply inverse QFT to the first n qubits
    F_inv = inverse_qft(n)
    state = (tensor(F_inv, np.eye(2 ** n)) @ state)

    # Measure the first register
    probabilities = np.abs(state) ** 2
    measurement = np.random.choice(len(probabilities), p=probabilities)
    phase = measurement / (2 ** n)
    # Attempt to approximate the phase as a fraction r/s.
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

