"""Experimental advanced modules for future quantum features."""

from .compiler import QuantumCompiler
from .error_correction import SurfaceCode, StabilizerMeasurement
from .noise_models import (
    NoiseModel,
    DepolarizingChannel,
    AmplitudeDamping,
    PhaseDamping,
)
from .variational import VariationalCircuit, Optimizer, VariationalQuantumEigensolver

__all__ = [
    "QuantumCompiler",
    "SurfaceCode",
    "StabilizerMeasurement",
    "NoiseModel",
    "DepolarizingChannel",
    "AmplitudeDamping",
    "PhaseDamping",
    "VariationalCircuit",
    "Optimizer",
    "VariationalQuantumEigensolver",
]
