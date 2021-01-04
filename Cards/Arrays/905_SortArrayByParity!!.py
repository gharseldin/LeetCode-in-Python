class Solution:

    # needs optimization
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        # seek the first odd element
        position = 0
        while position is not len(A) and A[position] % 2 is 0:
            position += 1

        while True:
            even = position
            while even < len(A) and A[even] % 2 is not 0:
                even += 1
            if even == len(A):
                return A
            (A[even], A[position]) = (A[position], A[even])
            position += 1
