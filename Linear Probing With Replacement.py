class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.hash = [-1] * self.size

    # Insert key with replacement
    def insert(self, key):
        index = key % self.size

        # If position is empty
        if self.hash[index] == -1:
            self.hash[index] = key
            return

        # Check whether existing key belongs to a different hash address
        if self.hash[index] % self.size != index:
            temp = self.hash[index]
            # Replace existing key
            self.hash[index] = key
            print(f"{temp} is displaced from index {index}")

            # Find next empty position for displaced key
            i = (index + 1) % self.size
            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size

            if self.hash[i] == -1:
                self.hash[i] = temp
            else:
                print("Hash Table is Full!")
        else:
            # Normal linear probing
            i = (index + 1) % self.size
            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size

            if self.hash[i] == -1:
                self.hash[i] = key
            else:
                print("Hash Table is Full!")

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