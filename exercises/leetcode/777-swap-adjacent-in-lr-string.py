class Solution:
    # TC: O(n)
    # SC: O(1)
    def canTransform(self, start: str, result: str) -> bool:
        P1, P2, N = 0, 0, len(start)

        while P1 < N or P2 < N:
            while P1 < N and start[P1] == "X":
                P1 += 1
            while P2 < N and result[P2] == "X":
                P2 += 1

            if P1 == N and P2 == N:
                return True

            if P1 == N or P2 == N or start[P1] != result[P2]:
                return False

            if start[P1] == "L" and P1 < P2:
                return False

            if start[P1] == "R" and P1 > P2:
                return False
            P1 += 1
            P2 += 1

        return True
