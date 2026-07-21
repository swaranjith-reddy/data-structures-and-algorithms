class HashDivision:
    def __init__(self, size):
        self.size = size
        # Create an array of empty buckets
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # The Engine: Standard Modulo Math
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        # Safely append to the bucket instead of overwriting
        self.table[index].append(key)

    def display(self):
        print("\n--- Division Hash Table ---")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Driver Code
keys = [45, 12, 105, 8, 22]
size = 10

hd = HashDivision(size)
for key in keys:
    hd.insert(key)

hd.display()
