class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counts = []
        for child in g:
            counter = 0
            for cookie in s:
                if cookie >= child:
                    counter += 1
            counts.append(counter)
        
        return max(counts) -1

            