class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 1
        position = 0
        while position < len(arr):
            if arr[position] == count:
                position += 1
            else:
                k -= 1
            if k == 0:
                return count
            count += 1
        while k > 0:
            count += 1
            k -= 1
        return count-1
