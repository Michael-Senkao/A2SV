# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)

        self.k = k

        self.adjustHeap()
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        self.adjustHeap()

        return self.heap[0]
    
    def adjustHeap(self):
        while len(self.heap) > self.k:
            heappop(self.heap)
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)