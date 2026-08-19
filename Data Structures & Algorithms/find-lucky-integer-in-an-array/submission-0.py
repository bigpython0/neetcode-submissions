class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyMap = Counter(arr)

        luckyNums = [-1]

        for num in luckyMap:
            if num == luckyMap[num]:
                luckyNums.append(num)
        
        return max(luckyNums) 


        