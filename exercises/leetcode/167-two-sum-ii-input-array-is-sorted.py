class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers) - 1
        L = 0
        R = N

        while L < R:
            currSum = numbers[L] + numbers[R]

            if currSum == target:
                return [L + 1, R + 1]
            elif currSum > target:
                R -= 1
            else:
                L += 1
