class HeapSort:
    def __init__(self):
        self.a = []
        self.n = 0

    # Read array elements
    def read(self):
        self.n = int(input("Enter number of elements: "))
        print("Enter elements:")
        # Supports both space-separated and line-by-line input
        while len(self.a) < self.n:
            self.a.extend(map(int, input().split()))
        self.a = self.a[:self.n]

    # Maintain Min Heap
    def heapify(self, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] < self.a[smallest]:
            smallest = left

        if right < n and self.a[right] < self.a[smallest]:
            smallest = right

        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.heapify(n, smallest)

    # Heap Sort using Min Heap
    def sort(self):
        # Build Min Heap
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)

        # Extract minimum element
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapify(i, 0)

    # Display sorted array
    def display(self):
        print("\nSorted elements in Descending Order:")
        print(" ".join(map(str, self.a)))


if __name__ == "__main__":
    h = HeapSort()
    h.read()
    h.sort()
    h.display()