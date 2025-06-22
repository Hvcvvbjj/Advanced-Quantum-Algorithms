"""Blueprint for an advanced quantum framework.

This experimental package sketches a highly modular system intended to
scale across distributed quantum resources and integrate cutting-edge
techniques such as machine-learning–based circuit synthesis and real-time
error mitigation.  Only the high level API is provided for now.
"""

from .orchestrator import QuantumOrchestrator, SimulatedDevice
from .qnn import QuantumNeuralNetwork
from .advanced_scheduling import Scheduler
from .autoencoder import QuantumAutoencoder
from .synergy import HybridRuntime

__all__ = [
    "QuantumOrchestrator",
    "SimulatedDevice",
    "QuantumNeuralNetwork",
    "Scheduler",
    "QuantumAutoencoder",
    "HybridRuntime",
]
