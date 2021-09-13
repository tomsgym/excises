class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            if((target - n) in nums[i+1:]):
                return [i, nums[i+1:].index(target-n) + i + 1]
