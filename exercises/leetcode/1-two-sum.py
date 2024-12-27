class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compareDict = {}

        for i in range(len(nums)):
            compareDict[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in compareDict and i != compareDict[diff]:
                return [i, compareDict[diff]]
