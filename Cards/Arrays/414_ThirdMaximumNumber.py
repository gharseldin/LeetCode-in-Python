class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxim = []
        for i in range(len(nums)):
            num = nums[i]
            if len(maxim) == 0:
                maxim.append(num)
            elif len(maxim) == 1:
                if num > maxim[0]:
                    maxim.append(num)
                elif num < maxim[0]:
                    maxim.append(maxim[0])
                    maxim[0] = num
            elif len(maxim) == 2:
                if num > maxim[1]:
                    maxim.append(nums[i])
                elif num > maxim[0] and num < maxim[1]:
                    maxim.append(maxim[1])
                    maxim[1] = num
                elif num < maxim[0]:
                    maxim.append(maxim[1])
                    maxim[1] = maxim[0]
                    maxim[0] = num
            else:
                if num > maxim[0] and num < maxim[1]:
                    maxim[0] = num
                elif num > maxim[1] and num < maxim[2]:
                    maxim[0] = maxim[1]
                    maxim[1] = num
                elif num > maxim[2]:
                    maxim[0] = maxim[1]
                    maxim[1] = maxim[2]
                    maxim[2] = num
        if len(maxim) < 3:
            return maxim[len(maxim)-1]
        return maxim[0]
