class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        addLater = list(arr1)
        res = []
        for i in range(len(arr2)):
            while arr2[i] in arr1:
                res.append(arr2[i])
                arr1[arr1.index(arr2[i])] = -1
                if arr2[i] in addLater:
                    addLater.remove(arr2[i])
        addLater = sorted(addLater)
        for i in addLater:
            res.append(i)
        return res
            