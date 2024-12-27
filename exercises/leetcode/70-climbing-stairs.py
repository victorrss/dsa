class Solution:
    def climbStairs(self, n: int) -> int:
        ## Top down DP (memoization)
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)
        # memo = {1:1,2:2}
        # def f(n):
        #     if n in memo:
        #         return memo[n]
            
        #     memo[n] = f(n-1) + f(n-2)
        #     return memo[n]
        # return f(n)

        # Bottom-Up No Memory
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if n <= 2:
             return n

        prev = 1
        cur = 2
        for i in range(3, n+1):
            prev, cur = cur, prev+cur
        return cur

        ## Bottom-Up (Tabulation)
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)
        # if n <= 2:
        #     return n
        # stairs = [0] * (n+1)
        # stairs[1] = 1
        # stairs[2] = 2
        # for i in range(3, len(stairs)):
        #     stairs[i] = stairs[i-1] + stairs[i-2]
        # return stairs[n]
        
        ## Recursion Backtracking
        ## Time Complexity: O(2^n)
        ## Space Complexity: O(n)
        # if n <= 2:
        #     return n
        # return self.climbStairs(n-2) + self.climbStairs(n-1)
