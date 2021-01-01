class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        used = {}
        # first we set all the pieces to unused
        for i in range(len(pieces)):
            used[i] = False

        position = 0
        while position < len(arr):
            for j in range(len(pieces)):
                if not used[j] and arr[position] == pieces[j][0] and self.matches(position, arr, pieces[j]):
                    position += len(pieces[j])
                    used[j] = True
                    break
                if j == len(pieces)-1:
                    return False

        # we have to make sure we used all pieces
        for i in used:
            if used[i] == False:
                return False

        # we have to make sure we reached the end of the array
        if not position == len(arr):
            return False

        # every condition is satisfied so we return true
        return True

    def matches(self, position: int, arr: List[int], piece: List[int]) -> bool:
        for i in range(len(piece)):
            if not position+i < len(arr) or arr[position+i] != piece[i]:
                return False
        return True
