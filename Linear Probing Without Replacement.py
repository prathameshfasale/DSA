class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.hash = [-1] * self.size

    # Insert key without replacement
    def insert(self, key):
        index = key % self.size
        start = index

        while self.hash[index] != -1:
            index = (index + 1) % self.size
            if index == start:
                print("Hash Table is Full!")
                return

        self.hash[index] = key
        print(f"{key} inserted at index {index}")

    # Display hash table
    def display(self):
        print("\nIndex\tValue")
        for i in range(self.size):
            val = "Empty" if self.hash[i] == -1 else self.hash[i]
            print(f"{i}\t{val}")


if __name__ == "__main__":
    h = HashTable()
    n = int(input("Enter number of keys: "))
    print("Enter keys:")
    for _ in range(n):
        key = int(input())
        h.insert(key)
    h.display()