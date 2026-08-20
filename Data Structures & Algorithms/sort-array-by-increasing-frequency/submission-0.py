class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = Counter(nums)
        res = []

        for element, anzahl in sorted(freqMap.items(), key=lambda x: (x[1], -x[0])):
            for i in range(anzahl):
                res.append(element) 

        return res