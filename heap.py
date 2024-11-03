class Heap:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, loc_new: int):
        if loc_new > 0:
            loc_par = (loc_new - 1) // 2

            if self.heap[loc_new] < self.heap[loc_par]:
                self._swap(self.heap, loc_new, loc_par)
                self._heapify_up(loc_par)
    
    def add(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_down(self, loc_new: int):
        size = len(self.heap)
        left = (2*loc_new) + 1
        right = (2*loc_new) + 2
        if left < size and right < size:
            min_node = min(self.heap[left], self.heap[right])
            if self.head[loc_new] > min_node:
                pass
        if left < size and right >= size:
            pass

    def _swap(self, arr, i1, i2):
        temp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = temp
    
    
    def display(self):
        self._print(0, 0)

    def _print(self, loc, depth):
        if loc < len(self.heap):
            self._print((2*loc)+2, depth+1)
            print(f"{(" "*(depth*3))}{self.heap[loc]}")
            self._print((2*loc)+1, depth+1)




def main():
    bob = Heap()
    bob.add(2)
    bob.add(3)
    bob.add(4)
    bob.add(5)
    bob.add(7)
    bob.add(8)
    bob.display()
    print()

    bob.add(1)

    bob.display()

if __name__ == "__main__":
    main()