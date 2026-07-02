class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heapop(stones))
            y = abs(heapq.heapop(stones))

            if x == y:
                continue
            
            if x < y:
                y = y - x

            heapq.heappush(y)


        if not stones:
            return 0
        else:
            return stones[0]

