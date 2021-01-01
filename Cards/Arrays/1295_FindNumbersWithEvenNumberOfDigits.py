class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if self.isEvenDigits(i):
                count += 1
        return count

    def isEvenDigits(self, number: int) -> bool:
        digits = 0
        while number > 0:
            number //= 10
            digits += 1
        return digits & 1 == 0
