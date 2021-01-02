class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = 0
        n = len(arr)
        i = 0
        lastPresent = False

        # counting effective zeros
        # these the zeros that will not be pushed out from the shifting
        while i <= n-1:
            if i is n-1:
                lastPresent = True
                break
            if arr[i] is 0:
                zeros += 1
                n -= 1
            i += 1

        # start writing from the end of the array with a shift of zeros
        n = len(arr)
        write = n-1
        read = write-zeros
        if lastPresent:
            arr[write] = arr[read]
            write -= 1
            read -= 1
        while write >= 0:
            if arr[read] == 0:
                arr[write] = 0
                write -= 1
                arr[write] = 0
                zeros -= 1
            else:
                arr[write] = arr[read]
            read -= 1
            write -= 1
