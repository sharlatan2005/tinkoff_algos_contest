class MaxHeap:
    def __init__(self):
        self.buf = []
    
    def insert(self, val):
        self.buf.append(val)
        self.sift_up(len(self.buf) - 1)
        # print(*self.buf)

    def sift_up(self, i):
        if i > 0:
            parent = (i - 1) // 2
            if self.buf[i] > self.buf[parent]:
                self.buf[i], self.buf[parent] = self.buf[parent], self.buf[i]
                self.sift_up(parent)
    
    def extract(self):
        max_val = self.buf[0]
        self.buf[0], self.buf[-1] = self.buf[-1], self.buf[0]
        self.buf = self.buf[:-1]
        self.sift_down(0)
        return max_val
    
    def sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = None
        max_idx = len(self.buf) - 1
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
            
