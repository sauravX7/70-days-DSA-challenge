# LeetCode 2529. Maximum Count of Positive And Negative Integer

class Solution(object):
    def maximumCount(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1  
            else:
                r = m - 1  
        neg_count = l 
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m - 1
        pos_count = len(nums) - l  
        return max(neg_count, pos_count)



