
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l_index = 0
        r_index = len(s) - 1
        while r_index > l_index:
            if s[l_index] != s[r_index]:
                return self.is_palindrome(s, l_index + 1, r_index) or self.is_palindrome(s, l_index, r_index - 1)
            l_index += 1
            r_index -= 1
        return True

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
