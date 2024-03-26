class MaxHeap:
    def __init__(self, buf):
        self.buf = buf
        self.arr_index = len(buf)
    
    def extract(self):
        max_val = self.buf[0]
        self.buf[0], self.buf[self.arr_index - 1] = self.buf[self.arr_index - 1], self.buf[0]
        self.arr_index -= 1
        self.sift_down(0)
        return max_val
    
    def sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = None
        max_idx = self.arr_index - 1
        if (left <= max_idx and right > max_idx):
            largest = left
        elif (left > max_idx and right <= max_idx):
            largest = right
        elif (left <= max_idx and right <= max_idx):
            if (self.buf[left] > self.buf[right]):
                largest = left
            else:
                largest = right
        else:
            return
        if (self.buf[i] < self.buf[largest]):
            self.buf[i], self.buf[largest] = self.buf[largest], self.buf[i]
            self.sift_down(largest)        
            

n = int(input())

arr = list(map(int, input().split()))

max_heap = MaxHeap(arr)

for i in range(n // 2 - 1, -1, -1):
    max_heap.sift_down(i)

for i in range(n):
    max_heap.extract()

print(*max_heap.buf)
