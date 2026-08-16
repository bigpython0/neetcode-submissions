class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        optimalNums = [i for i in range(1,len(nums)+1)]

        nums = sorted(nums)
        ans = [0,0]

        for num in nums:
            if num in optimalNums:
                optimalNums.remove(num)
            else:
                ans[0] = num
        
        ans[1]=optimalNums[0]

        return ans
            


