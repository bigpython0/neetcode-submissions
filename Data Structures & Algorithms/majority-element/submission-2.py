class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        candidate = sortedNums[len(nums)//2]

        if sortedNums.count(candidate) > len(nums)//2:
            return candidate
        
        return -1