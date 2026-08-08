class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counters = []
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counters.append(counter)
                counter = 0
            else:
                counter += 1
        counters.append(counter)
        if not counters:
            counters.append(0)
        return max(counters)