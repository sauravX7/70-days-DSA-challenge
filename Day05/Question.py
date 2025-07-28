#LeetCode 34. Find First and Last Position of Element in Sorted Array
class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            start, end = 0, len(nums) - 1
            first = -1
            while start <= end:
                m = (start + end) // 2
                if nums[m] >= target:
                    if nums[m] == target:
                        first = m
                    end = m - 1  # Move left
                else:
                    start = m + 1
            return first

        def findLast(nums, target):
            start, end = 0, len(nums) - 1
            last = -1
            while start <= end:
                m = (start + end) // 2
                if nums[m] <= target:
                    if nums[m] == target:
                        last = m
                    start = m + 1  # Move right
                else:
                    end = m - 1
            return last
        
        return [findFirst(nums, target), findLast(nums, target)]



        
