"""Foundations for quantum neural networks."""

class QuantumNeuralNetwork:
    """High level quantum neural network abstraction."""

    def __init__(self, layers):
        self.layers = layers

    def forward(self, data):
        """Process ``data`` through variational layers.

        Each layer is expected to be a callable that accepts and returns a state
        vector or ``QuantumCircuit``.  This simplified forward pass merely
        chains the layers together.
        """
        state = data
        for layer in self.layers:
            state = layer(state)
        return state
