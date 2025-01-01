class Solution:
    def isAlpha(self, s):
        return (ord(s) >= ord('a') and ord(s) <= ord('z')) or (ord(s) >= ord('0') and ord(s) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1

        while L<R:
            sLeft = s[L].lower()
            sRight = s[R].lower()
            if not self.isAlpha(sRight):
                R-=1
                continue
            if not self.isAlpha(sLeft):
                L+=1    
                continue

            if sLeft != sRight:
                return False
            L+=1
            R-=1
        return True
        
