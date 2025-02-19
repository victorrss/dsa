class Solution:
    # TC: O(n * 2ˆn)
    # SC: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(i, partial=[]):
            if i >= len(nums):
                res.append(partial.copy())
                return

            partial.append(nums[i])
            bt(i + 1, partial)

            partial.pop()
            bt(i + 1, partial)

        bt(0, [])
        return res
