
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chars = list(word.lower())
        ch = ch.lower()
        l_index = 0
        r_index = 0
        for index, char in enumerate(chars):
            if char == ch:
                r_index = index
                break
        if r_index == 0:
            return word
        while r_index > l_index:
            chars[l_index], chars[r_index] = chars[r_index], chars[l_index]
            l_index += 1
            r_index -= 1
        return ''.join(chars)
