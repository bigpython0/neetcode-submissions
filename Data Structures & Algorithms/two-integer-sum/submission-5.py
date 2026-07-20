class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for k in range(n):
                if nums[i] + nums[k] == target:
                        if i == k:
                            continue
                        else:
                            return [i,k]