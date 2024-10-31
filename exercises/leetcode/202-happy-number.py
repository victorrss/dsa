class Solution:
    def isHappy(self, n: int) -> bool:
        visits = set()
        while n not in visits:
            visits.add(n)
            lastSum = 0
            while n > 0:
                lastDigit = n % 10
                lastSum += lastDigit * lastDigit
                n //= 10
            if lastSum == 1:
                return True
            n = lastSum

        return False
