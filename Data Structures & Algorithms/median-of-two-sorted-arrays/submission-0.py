class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_total = nums1 + nums2


        nums_total.sort()
        mid = len(nums_total) // 2

        if len(nums_total) % 2 == 0:
            return (nums_total[mid-1] + nums_total[mid]) / 2
        else:
            return nums_total[mid]



        return nums_total[mid]
            