class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, L, R = 0, 0, len(height) - 1

        while L < R:
            area = (R - L) * min(height[R], height[L])
            res = max(res, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return res
