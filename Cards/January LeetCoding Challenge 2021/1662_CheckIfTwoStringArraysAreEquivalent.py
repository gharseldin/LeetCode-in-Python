class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
            # Not a very efficient solution because strings are immutable
            w1 = ""
            w2 = ""
            for s in word1:
                w1 += s
            for s in word2:
                w2 +=s
            return w1 == w2
        """
        w1 = []
        w2 = []
        for i in word1:
            for j in i:
                w1.append(j)

        for i in word2:
            for j in i:
                w2.append(j)

        if len(w1) != len(w2):
            return False

        for i in range(len(w1)):
            if(w1[i] != w2[i]):
                return False

        return True
