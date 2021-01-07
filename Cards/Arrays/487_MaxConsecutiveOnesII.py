class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        intervals = {}
        tempStart = 0
        tempEnd = 0
        started = False
        for i in range(len(nums)):
            if started:
                if nums[i] == 1:
                    tempEnd = i
                else:
                    intervals[tempStart] = tempEnd
                    started = False
            else:
                if nums[i] == 1:
                    started = True
                    tempStart = i
                    tempEnd = i

        if started:
            intervals[tempStart] = tempEnd

        max = 0

        if len(intervals) == 0:
            if len(nums) == 0:
                return 0
            else:
                return 1

        if len(intervals) == 1:
            if nums[0] == 0 or nums[len(nums)-1] == 0:
                for interval in intervals:
                    return intervals[interval] - interval + 2
            else:
                for interval in intervals:
                    return intervals[interval] - interval + 1

        for interval in intervals:
            if intervals[interval] - interval + 2 > max:
                max = intervals[interval] - interval + 2
            if (intervals[interval] + 2) in intervals:
                temp = intervals[intervals[interval]+2] - interval + 1
                if temp > max:
                    max = temp
        return max
