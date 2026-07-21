class HashMidSquare:
    def __init__(self, size):
        self.size = size
        # Create an array of empty buckets
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # 1. Square the key
        squared = key * key
        
        # 2. Convert to string to find the middle
        sq_str = str(squared)
        mid_index = len(sq_str) // 2
        
        # 3. Extract the middle character
        middle_char = sq_str[mid_index]
        
        # 4. Convert back to integer and wrap it to table size
        return int(middle_char) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        # Safely append to the bucket
        self.table[index].append(key)

    def display(self):
        print("\n--- Mid-Square Hash Table ---")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Driver Code
keys = [12, 93, 31, 45, 82]
size = 10

hms = HashMidSquare(size)
for key in keys:
    hms.insert(key)

hms.display()
