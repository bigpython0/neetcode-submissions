class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tMap = Counter(text)
        print(tMap['l'])
        print(tMap['o'])

        return max(0, min(tMap['b'],tMap['a'],tMap['l']//2,tMap['o']//2,tMap['n']))