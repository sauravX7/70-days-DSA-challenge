#LeetCode 2109. Adding Spaces to a String
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        r=[]
        p=0
        for i in spaces:
            r.append(s[p:i])
            r.append(" ")
            p=i
        r.append(s[p:])  
        return "".join(r)
