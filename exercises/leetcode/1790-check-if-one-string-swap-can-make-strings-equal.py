class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        swaps = 0
        chrLsts1 = list()
        chrLsts2 = list()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps +=1

                if s1[i] in chrLsts2:
                    chrLsts2.remove(s1[i])
                elif s1[i] not in chrLsts1: 
                    chrLsts1.append(s1[i]) 

                if s2[i] in chrLsts1: 
                    chrLsts1.remove(s2[i]) 
                elif s2[i] not in chrLsts2:
                    chrLsts2.append(s2[i]) 

            if swaps > 2:
                return False

        return len(chrLsts1) == 0 and len(chrLsts2) == 0 
