"""Distributed quantum resource orchestrator."""

class QuantumOrchestrator:
    """Coordinate execution across heterogeneous quantum devices."""

    def __init__(self):
        self.devices = []

    def register_device(self, device):
        """Register a quantum processing unit."""
        self.devices.append(device)

    def run(self, circuit):
        """Dispatch ``circuit`` to the first registered device and return result.

        The orchestrator provides a very small demonstration of how one might
        interface with heterogeneous quantum processors.  Devices are expected to
        expose an ``execute`` method returning a measurement outcome.  If no
        device has been registered the circuit is simply measured locally.
        """
        if self.devices:
            device = self.devices[0]
            return device.execute(circuit)
        return circuit.measure_all()


class SimulatedDevice:
    """Minimal device executing circuits inside the current process."""

    def __init__(self, noise_model=None):
        self.noise_model = noise_model

    def execute(self, circuit):
        if self.noise_model is not None:
            self.noise_model.apply(circuit)
        return circuit.measure_all()
