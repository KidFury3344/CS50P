class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.n = 0

    def __str__(self):
        return "🍪" * self.n

    def deposit(self, n):
        if self.n + n > self.capacity:
            raise ValueError("The jar cannot hold that many cookies")
        self.n = n + self.n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not that many cookies in jar")
        self.n = self.n - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) is not int:
            raise TypeError("Capacity must be an integer")
        elif capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity

    @property
    def size(self):
        return self.n

