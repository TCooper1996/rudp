import pickle

class Packet:
    def __init__(self, seq, data=None):
        self.seq = (seq).to_bytes(4, "little")
        self.data = data

    def get_data(self):
        return self.data

    def get_seq(self):
        return int.from_bytes(self.seq, "little")

    def reply(self):
        return pickle.dumps(Packet(self.get_seq()+1))

    def reply(self, data):
        return pickle.dumps(Packet(self.get_seq(), data))
