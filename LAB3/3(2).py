from queue import Queue
class VotingProcess:
    def __init__(self, pid, voting_set):
        self.pid = pid
        self.voting_set = voting_set
        self.voted = False
        self.queue = Queue()
    def request_cs(self):
        print(f"P{self.pid} sends REQUEST to {self.voting_set}")
        for q in self.voting_set:
            processes[q].receive_request(self.pid)
    def receive_request(self, requester):
        if not self.voted:
            self.voted = True
            print(f"P{self.pid} votes for P{requester}")
            processes[requester].receive_reply(self.pid)
        else:
            self.queue.put(requester)
            print(f"P{self.pid} queues REQUEST from P{requester}")
    def receive_reply(self, from_pid):
        print(f"P{self.pid} received REPLY from P{from_pid}")
    def release_cs(self):
        print(f"P{self.pid} releases CS, notifies {self.voting_set}")
        for q in self.voting_set:
            processes[q].receive_release(self.pid)
    def receive_release(self, from_pid):
        if not self.queue.empty():
            next_pid = self.queue.get()
            print(f"P{self.pid} sends REPLY to P{next_pid}")
            processes[next_pid].receive_reply(self.pid)
            self.voted = True
        else:
            self.voted = False
processes = [VotingProcess(i, [0, 1, 2]) for i in range(3)]
processes[0].request_cs()
