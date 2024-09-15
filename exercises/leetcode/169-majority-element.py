class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counting = {}

        for n in nums:
            if n in counting:
                counting[n] += 1
            else:
                counting[n] = 0

        max_qty = 0
        res = nums[0]
        for n, qty in counting.items():
            if qty > max_qty:
                max_qty = qty
                res = n
        return res
