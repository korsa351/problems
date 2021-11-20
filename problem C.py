class Buffer:
    def __init__(self):
        self.sequence = []

    def add(self, *a):
        if len(self.sequence) + len(a) >= 5:
            self.sequence += a
            if len(self.sequence) <= 5:
                print(sum(self.sequence))
                self.sequence = []
            else:
                while len(self.sequence) >= 5:
                    print(sum(self.sequence[:5]))
                    self.sequence = self.sequence[5:]
        else:
            self.sequence += a

    def get_current_part(self):
        return self.sequence
