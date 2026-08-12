class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mgzMap = Counter(magazine)

        for c in ransomNote:
            if c not in mgzMap:
                return False
            else:
                if mgzMap[c] == 0:
                    del mgzMap[c]
                else:
                    mgzMap[c] -= 1
        return True