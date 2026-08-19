class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #nums = sorted(nums)
        for i in range(max(nums)):
            nums.append(i)
            nums = sorted(nums)

            if nums.index(i) == len(nums) - i - 1:
                return i
            print(i)
            print(nums.index(i))
            print(len(nums)-i-1) 

        return -1