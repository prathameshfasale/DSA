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

    # Maintain Max Heap
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] > self.a[largest]:
            largest = left

        if right < n and self.a[right] > self.a[largest]:
            largest = right

        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.heapify(n, largest)

    # Heap Sort using Max Heap
    def sort(self):
        # Build Max Heap
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)

        # Extract maximum element
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapify(i, 0)

    # Display sorted array
    def display(self):
        print("\nSorted elements in Ascending Order:")
        print(" ".join(map(str, self.a)))


if __name__ == "__main__":
    h = HeapSort()
    h.read()
    h.sort()
    h.display()