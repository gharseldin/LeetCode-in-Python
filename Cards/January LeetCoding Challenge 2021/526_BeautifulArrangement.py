class Solution:
    def countArrangement(self, n: int) -> int:
        num = set()
        for i in range(n):
            num.add(i+1)
        count = [0]
        self.iterateOver(1, num, count)
        return count[0]

    def iterateOver(self, pos: int, num: List[int], count: List[int]) -> int:
        if(len(num) is 0):
            count[0] += 1

        possible = []
        for i in num:
            if (i is not None) and (i % pos == 0 or pos % i == 0):
                possible.append(i)
        for i in possible:
            num.remove(i)
            self.iterateOver(pos+1, num, count)
            num.add(i)
