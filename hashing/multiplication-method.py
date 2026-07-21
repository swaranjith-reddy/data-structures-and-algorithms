class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.A = 0.618   # constant

    def hash_function(self, key):
        fractional_part = (key * self.A) % 1
        return int(self.size * fractional_part)

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        for i in range(self.size):
            print("Index", i, ":", self.table[i])


# Driver Code
keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
size = 7

ht = Hashtable(size)

for key in keys:
    ht.insert(key)

ht.display()
