class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0,0]
        counts = Counter(chain.from_iterable(grid))

        n = len(grid)
        
        for num in range(1,n*n+1):
            if counts[num] > 1:
                ans[0] = num
            elif counts[num] == 0:
                ans[1] = num

        return ans