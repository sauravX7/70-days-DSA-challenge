# LeetCode 3136 Valid Word 

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)< 3:
            return False 
        v=False
        co=False
        for c in word:
            if c.isalpha():
                if c.lower() in 'aeiou':
                    v=True
                else:
                    co=True
            elif not c.isdigit():
                return False
        return v and co

