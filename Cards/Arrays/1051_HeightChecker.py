class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = []
        for i in heights:
            temp.append(i)
        temp.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                count += 1
        return count
