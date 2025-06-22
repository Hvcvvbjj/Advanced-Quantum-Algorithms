"""Quantum Fourier Transform utilities."""

import numpy as np

from .circuit import tensor, apply_single_qubit_gate
from .gates import H


def qft(n):
    """Quantum Fourier Transform matrix for n qubits."""
    N = 2 ** n
    omega = np.exp(2j * np.pi / N)
    F = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            F[i, j] = omega ** (i * j)
    return F / np.sqrt(N)


def swap_qubits(state, q1, q2, n):
    state = state.reshape([2] * n)
    state = np.swapaxes(state, q1, q2)
    return state.reshape(2 ** n)


def apply_controlled_phase(state, control, target, angle, n):
    indices = np.arange(len(state))
    mask = ((indices >> control) & 1) & ((indices >> target) & 1)
    state[mask] *= np.exp(1j * angle)
    return state


def apply_inverse_qft(state, n, total_qubits):
    for q in range(n // 2):
        state = swap_qubits(state, q, n - q - 1, total_qubits)
    for j in range(n):
        for k in range(j):
            angle = -np.pi / (2 ** (j - k))
            state = apply_controlled_phase(state, k, j, angle, total_qubits)
        state = apply_single_qubit_gate(state, H, j, total_qubits)
    return state
