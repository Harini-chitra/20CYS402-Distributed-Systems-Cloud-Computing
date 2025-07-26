import threading
from queue import Queue
class Process:
    def __init__(self, pid, n):
        self.pid = pid
        self.timestamp = 0
        self.N = n
        self.replies = 0
        self.request_q = []
        self.in_cs = False
        self.lock = threading.Lock()
    def request_cs(self, processes):
        self.timestamp += 1
        self.replies = 0
        print(f"Process {self.pid} requests CS at timestamp {self.timestamp}")
        for p in processes:
            if p.pid != self.pid:
                p.receive_request(self.timestamp, self.pid)
        while self.replies < self.N - 1:
            pass
        self.enter_cs()
    def receive_request(self, timestamp, pid):
        with self.lock:
            if not self.in_cs and (self.timestamp, self.pid) > (timestamp, pid):
                print(f"Process {self.pid} sends REPLY to {pid}")
                processes[pid].receive_reply()
            else:
                print(f"Process {self.pid} queues REQUEST from {pid}")
                self.request_q.append((timestamp, pid))
    def receive_reply(self):
        self.replies += 1
    def enter_cs(self):
        print(f"Process {self.pid} ENTERS CS")
        self.in_cs = True
        self.exit_cs()
    def exit_cs(self):
        print(f"Process {self.pid} EXITS CS")
        self.in_cs = False
        for t, p in sorted(self.request_q):
            processes[p].receive_reply()
        self.request_q = []
processes = [Process(i, 3) for i in range(3)]
processes[0].request_cs(processes)
processes[1].request_cs(processes)
processes[2].request_cs(processes)
