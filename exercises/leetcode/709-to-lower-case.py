class Solution:
    def toLowerCase(self, s: str) -> str:
        strList = s.split()
        for i in range(len(strList)):
            strList[i] = strList[i].lower()
        return "".join(strList)
      
