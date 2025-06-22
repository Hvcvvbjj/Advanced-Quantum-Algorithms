"""Showcase advanced 'ultra' modules with a noisy device."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from algorithms.grover import grover_search
from quantum.ultra import QuantumOrchestrator, SimulatedDevice
from quantum.advanced.noise_models import AmplitudeDamping


def main():
    oracle = lambda idx: idx == 3  # search for |11>
    circuit1 = grover_search(2, oracle)
    circuit2 = grover_search(2, oracle)

    orchestrator = QuantumOrchestrator()
    device_a = SimulatedDevice(noise_model=AmplitudeDamping(0.2), noise_level=0.2)
    device_b = SimulatedDevice(noise_model=AmplitudeDamping(0.1), noise_level=0.1)
    orchestrator.register_device(device_a)
    orchestrator.register_device(device_b)

    results = orchestrator.run_batch([circuit1, circuit2])
    print(f"Noisy Grover results: {results}")


if __name__ == "__main__":
    main()
