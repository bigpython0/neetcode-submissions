class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letMap = Counter("".join(words))

        print(letMap)
        for c in letMap:
            if letMap[c] % len(words) != 0:
                return False
        
        return True



        