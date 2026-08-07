class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pT = 0
        pS = 0
        while pT < len(t) and pS < len(s):
            if t[pT] == s[pS]:
                pS += 1
            pT += 1
        return pS == len(s)
