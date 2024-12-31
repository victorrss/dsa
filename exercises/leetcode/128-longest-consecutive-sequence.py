class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        mySet = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in mySet:  # it's the begining of a sequence
                length = 1
                while nums[i] + length in mySet:  # walks to look for the end of the seq
                    length += 1
                longest = max(longest, length)
        return longest
