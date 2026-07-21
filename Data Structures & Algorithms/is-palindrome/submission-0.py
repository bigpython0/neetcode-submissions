class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = "".join(filter(str.isalnum, s))
        fs = fs.lower()
        return fs[::-1] == fs