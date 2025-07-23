# LeetCode 1717 Maximum Score from Removing Substring 
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def rp(pair,score):
            nonlocal s 
            res=0
            stack=[]
            for c in s:
                if c==pair[1] and stack and stack[-1]==pair[0]:
                    stack.pop()
                    res+=score
                else:
                    stack.append(c)
            s= "".join(stack)
            return res 

        res=0
        pair='ab' if x>y else "ba"
        res += rp(pair,max(x,y))
        res += rp(pair[::-1],min(x,y))
        return res
