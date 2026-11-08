class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        #bet

        # Notice that `nums1` has empty space (zeros) at the very end. 
        #If you try to merge elements starting from the beginning, 
        #you might overwrite valid values in `nums1` before you have processed them.

        nums1[m:] = nums2[:n]
        nums1.sort()
