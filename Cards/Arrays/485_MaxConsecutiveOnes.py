class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > max:
                    max = counter
                counter = 0
        return max if max > counter else counter
