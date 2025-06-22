"""Hybrid classical/quantum runtime integration."""

class HybridRuntime:
    """Coordinate classical resources alongside quantum execution."""

    def execute(self, circuit, callback=None):
        """Run ``circuit`` with optional classical ``callback``.

        The circuit is executed locally and the measurement result is returned.
        If ``callback`` is provided, it is invoked with the measurement result
        allowing classical post-processing.
        """
        result = circuit.measure_all()
        if callback is not None:
            callback(result)
        return result
