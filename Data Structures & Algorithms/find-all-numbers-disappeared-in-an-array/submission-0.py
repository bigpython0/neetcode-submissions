class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(i+1)

        for num in nums:
            if num in res:
                res.remove(num)

        return res