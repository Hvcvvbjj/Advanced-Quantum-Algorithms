"""Showcase advanced 'ultra' modules with a noisy device."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from algorithms.grover import grover_search
from quantum.ultra import QuantumOrchestrator, SimulatedDevice
from quantum.advanced.noise_models import AmplitudeDamping


def main():
    oracle = lambda idx: idx == 3  # search for |11>
    circuit = grover_search(2, oracle)

    orchestrator = QuantumOrchestrator()
    device = SimulatedDevice(noise_model=AmplitudeDamping(0.2))
    orchestrator.register_device(device)

    result = orchestrator.run(circuit)
    print(f"Noisy Grover result: {result}")


if __name__ == "__main__":
    main()
