class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        P1, P2 = 0, 0
        N1, N2 = len(word1), len(word2)

        while P1 < N1 or P2 < N2:
            if P1 < N1:
                merged += word1[P1]
                P1 += 1
            if P2 < N2:
                merged += word2[P2]
                P2 += 1

        return merged
