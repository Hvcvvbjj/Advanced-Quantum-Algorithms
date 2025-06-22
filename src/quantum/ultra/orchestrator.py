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
            device = min(self.devices, key=lambda d: getattr(d, "noise_level", 0))
            return device.execute(circuit)
        return circuit.measure_all()

    def run_batch(self, circuits, scheduler=None, max_workers=None):
        """Execute ``circuits`` in parallel across registered devices.

        Parameters
        ----------
        circuits : list[QuantumCircuit]
            Circuits to execute.
        scheduler : Scheduler, optional
            Scheduler providing a mapping of circuits to devices.  If ``None``
            a default noise-aware scheduler is used.
        max_workers : int, optional
            Maximum number of worker threads.

        Returns
        -------
        list[str]
            Measurement results for each circuit.
        """
        if not self.devices:
            return [c.measure_all() for c in circuits]

        from .advanced_scheduling import Scheduler
        scheduler = scheduler or Scheduler()
        schedule = scheduler.schedule(circuits, self.devices)

        results = [None] * len(schedule)

        def execute(dev, circ):
            return dev.execute(circ)

        from concurrent.futures import ThreadPoolExecutor

        with ThreadPoolExecutor(max_workers=max_workers or len(self.devices)) as exe:
            futures = [exe.submit(execute, self.devices[idx], circ) for idx, circ in schedule]
            for i, fut in enumerate(futures):
                results[i] = fut.result()

        return results


class SimulatedDevice:
    """Minimal device executing circuits inside the current process."""

    def __init__(self, noise_model=None, noise_level: float = 0.0):
        self.noise_model = noise_model
        self.noise_level = noise_level

    def execute(self, circuit):
        if self.noise_model is not None:
            self.noise_model.apply(circuit)
        return circuit.measure_all()
