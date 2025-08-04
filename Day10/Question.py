#LeetCode 15. 3Sum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Fix: Added parentheses

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # Skip duplicate elements
                continue 

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    # Move `l` and `r` to avoid duplicate triplets
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # Move pointers forward
                    l += 1
                    r -= 1

        return res  # Fix: Return the result list
