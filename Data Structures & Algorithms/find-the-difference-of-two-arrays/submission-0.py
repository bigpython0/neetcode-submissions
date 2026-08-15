class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        ls1 = []
        ls2 = []

        for key in Counter(nums1)-Counter(nums2):
            ls1.append(key)
        
        for key in Counter(nums2)-Counter(nums1):
            ls2.append(key)

        return [ls1,ls2]