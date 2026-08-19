class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mapNums = Counter(nums)

        for num in mapNums:
            if mapNums[num] % 2 == 0:
                continue
            else:
                return False
        
        return True