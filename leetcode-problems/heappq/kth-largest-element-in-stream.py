class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = heapq.heapify(-x for x in nums)
        self.copy = (-x for x in nums)

    def add(self, val: int) -> int:
        self.heap = list(self.copy)

        heapq.push(self.heap,val)
        self.copy = list(self.heap)
        for i in range(self.k - 1):
            heapq.heappop(self.heap)
        
        
        return self.heap[0]




        



            

