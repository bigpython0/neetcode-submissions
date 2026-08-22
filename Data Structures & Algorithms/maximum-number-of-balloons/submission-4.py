class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tMap = Counter(text)
        return max(0, min(tMap['b'],tMap['a'],tMap['l']//2,tMap['o']//2,tMap['n']))