class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        libCount = Counter(chars)
        c = 0

        for word in words:
            curMap = Counter(word)
            if curMap <= libCount:
                c += len(word)
        
        return c