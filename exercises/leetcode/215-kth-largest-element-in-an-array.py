import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## Time: O(n + k log n) (heapify and negate the nums is N time + heap pop k times)
        ## Space O(1) (in-place)
        # for n in range(len(nums)):
        #     nums[n] = -nums[n]
        
        # heapq.heapify(nums)

        # for _ in range(k-1):
        #     heapq.heappop(nums)

        # return -heapq.heappop(nums)

        # Time: O(n Log k) (keeping only K largest in the heap, removing the mins)
        # Space O(k) (storing only K elements in the heap)
        heap = []
        for n in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[n])
            else:
                heapq.heappushpop(heap, nums[n])
        return heap[0]
