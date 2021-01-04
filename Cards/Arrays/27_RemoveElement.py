class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) is 0:
            return 0
        end = len(nums)-1
        while end >= 0 and nums[end] == val:
            end -= 1
        if len(nums) < 0:
            return 0
        start = 0
        length = 0
        while start < end:
            if nums[start] == val:
                (nums[start], nums[end]) = (nums[end], nums[start])
                end -= 1
                while nums[end] == val:
                    end -= 1
            start += 1
            length += 1
        if start == end and nums[start] is not val:
            length += 1
        return length
