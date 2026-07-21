class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_fun(self, key):
        s = str(key)
        total = 0

        for i in range(0, len(s), 2):
            part = s[i:i+2]
            total += int(part)

        return total % self.size   # important

    def insert(self, key):
        index = self.hash_fun(key)
        self.table[index].append(key)

    def display(self):
        for i in range(self.size):
            print("Index", i, ":", self.table[i])


# Driver Code
h = Hash(7)
keys = [1234, 5678, 91011, 1213]

for k in keys:
    h.insert(k)

print("Hash Table:")
h.display()

