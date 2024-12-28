class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity: O(nlogk) 
        # Space complexity: O(n+k)
        heap = []

        numsCount = Counter(nums)
        
        for n, count in numsCount.items():
            heapq.heappush(heap, (count, n))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
