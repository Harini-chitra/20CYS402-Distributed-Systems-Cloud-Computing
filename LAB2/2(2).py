class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0
    def event(self, desc):
        self.clock += 1
        print(f"Process {self.pid}: '{desc}' - Clock: {self.clock}")
    def send(self, receiver):
        self.clock += 1
        print(f"Process {self.pid}: 'send to {receiver.pid}' - Clock: {self.clock}")
        receiver.receive(self.clock)
    def receive(self, sender_clock):
        self.clock = max(self.clock, sender_clock) + 1
        print(f"Process {self.pid}: 'receive' - Updated Clock: {self.clock}")
p1 = Process(1)
p2 = Process(2)
p1.event("start")
p2.event("start")
p1.send(p2)
p2.event("local work")
p2.send(p1)
p1.event("end")