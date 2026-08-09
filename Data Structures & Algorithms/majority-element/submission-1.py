class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}

        for i, value in enumerate(nums):
            if value in countMap:
                countMap[value] += 1
            else:
                countMap[value] = 1
        
        print(countMap)
        return max(countMap, key=countMap.get)