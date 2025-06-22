"""Foundations for quantum neural networks."""

class QuantumNeuralNetwork:
    """High level quantum neural network abstraction."""

    def __init__(self, layers):
        self.layers = layers

    def forward(self, data):
        """Process ``data`` through variational layers (placeholder)."""
        raise NotImplementedError
