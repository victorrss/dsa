class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        check = set()
        maxL = 0

        for R in range(len(s)):
            while s[R] in check:
                check.remove(s[L])
                L += 1

            check.add(s[R])
            maxL = max(maxL, R - L + 1)
        return maxL
