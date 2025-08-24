# Edge-Chasing Distributed Deadlock Detection Algorithm
class Process:
    def __init__(self, pid):
        self.pid = pid
        self.waiting_for = []  # list of processes this process waits for
    def add_dependency(self, process):
        """Process waits for another process (edge in wait-for graph)."""
        self.waiting_for.append(process)
class EdgeChasingDeadlockDetector:
    def __init__(self, processes):
        self.processes = processes
        self.deadlock_detected = False

    def send_probe(self, initiator, current, visited):
        """
        Send probe messages recursively.
        If probe returns to initiator, deadlock exists.
        """
        if current in visited:
            return  # avoid infinite recursion in traversal

        visited.add(current)

        for neighbor in current.waiting_for:
            print(f"Probe: {initiator.pid} -> {neighbor.pid} (from {current.pid})")

            # Deadlock detected if probe reaches initiator again
            if neighbor == initiator:
                print(f"Deadlock detected! Cycle found at process {initiator.pid}.")
                self.deadlock_detected = True
                return

            # Continue probing
            self.send_probe(initiator, neighbor, visited.copy())

    def detect_deadlock(self):
        """Initiate probe from each process."""
        for process in self.processes:
            print(f"\nInitiating probe from Process {process.pid}")
            self.send_probe(process, process, set())

        if not self.deadlock_detected:
            print("\nNo deadlock detected.")


# ------------------- Example Input -------------------
if __name__ == "__main__":
    # Create processes
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)
    p4 = Process(4)

    # Define dependencies (Wait-For Graph edges)
    p1.add_dependency(p2)   # P1 waits for P2
    p2.add_dependency(p3)   # P2 waits for P3
    p3.add_dependency(p1)   # P3 waits for P1  (Cycle formed here: P1 -> P2 -> P3 -> P1)
    p4.add_dependency(p2)   # P4 waits for P2 (No cycle with P4)

    # Run Deadlock Detection
    detector = EdgeChasingDeadlockDetector([p1, p2, p3, p4])
    detector.detect_deadlock()
