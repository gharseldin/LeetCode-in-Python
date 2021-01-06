# could be solved more efficiently with binary search
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        i = 0
        j = len(arr) - 1
        cache = {}
        return self.check(arr, i, j, cache)

    def check(self, arr: List[int], i: int, j: int, cache: {str, bool}) -> bool:

        if i >= j:
            return False
        if arr[j] == arr[i]*2 or arr[i] == arr[j]*2:
            return True
        key = str(i)+"-"+str(j)
        if key in cache:
            return cache[key]
        result = self.check(
            arr, i+1, j, cache) or self.check(arr, i, j-1, cache)
        cache[key] = result
        return result
