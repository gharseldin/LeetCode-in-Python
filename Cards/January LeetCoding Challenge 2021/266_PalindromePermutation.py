class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = {}
        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] = chars[c]+1
        odds = 0
        for ch in chars:
            if chars[ch] % 2 == 1:
                odds += 1
        return not odds > 1
