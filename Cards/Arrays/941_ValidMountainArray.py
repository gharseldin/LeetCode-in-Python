class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] < arr[0]:
            return False
        last = arr[0]
        peak = False

        for i in range(1, len(arr)):
            if peak:
                if not arr[i] < last:
                    return False
                else:
                    last = arr[i]
            else:
                if arr[i] > last:
                    last = arr[i]
                elif arr[i] < last:
                    peak = True
                    last = arr[i]
                else:
                    return False
        return peak
