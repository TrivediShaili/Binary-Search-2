from typing import List

class Solution:
    def findMin(self, nums: int) -> int:
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        n = len(nums)
        
        while (low <= high):
            if(nums[low] <= nums[high]):
                return nums[low]
            mid = low + (high - low) / 2
            
            if ((mid == 0 or nums[mid]< nums[mid - 1])and ( nums[mid + 1])):
                return nums[mid]
            elif(nums[low]<=nums[mid]):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1