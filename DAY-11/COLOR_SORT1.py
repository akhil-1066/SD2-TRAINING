class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones=nums.count(1)
        zeroes=nums.count(0)
        for i in range(len(nums)):
            if zeroes:
                nums[i]=0
                zeroes-=1
            elif ones:
                nums[i]=1
                ones-=1
            else:
                nums[i]=2