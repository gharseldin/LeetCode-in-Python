class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        itr = 0
        while itr < len(nums):
            while itr < len(nums) and not nums[itr] == 0:
                itr += 1
            seek = itr+1
            while seek < len(nums) and nums[seek] == 0:
                seek += 1
            if seek < len(nums):
                (nums[itr], nums[seek]) = (nums[seek], nums[itr])
            itr += 1
