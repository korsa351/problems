class MoneyBox:
    def __init__(self, capacity):
        self.value = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.value + v <= self.capacity

    def add(self, v):
        self.value += v
