class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        table = [0] * (max_num + 1)

        for n in nums:
            table[n] = 1

        for i in range(len(table)):
            if table[i] == 0:
                return i

        # if the missing number is the last number
        return len(nums)
        # Time Complexity: O(N)
        # Space Complexity: O(N)
