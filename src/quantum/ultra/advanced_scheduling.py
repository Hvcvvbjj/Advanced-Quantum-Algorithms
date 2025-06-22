"""Sophisticated scheduling and resource management."""

class Scheduler:
    """Determine optimal job placement on quantum hardware."""

    def schedule(self, circuits, devices):
        """Return a simple noise-aware schedule.

        Parameters
        ----------
        circuits : list
            Quantum circuits to execute.
        devices : list
            Available devices registered with the orchestrator.

        Returns
        -------
        list[tuple[int, object]]
            Pairs of ``device_index`` and ``circuit`` to execute.
        """
        order = sorted(range(len(devices)), key=lambda i: getattr(devices[i], "noise_level", 0))
        schedule = []
        for idx, circuit in enumerate(circuits):
            dev_idx = order[idx % len(devices)]
            schedule.append((dev_idx, circuit))
        return schedule
