class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[l] <= nums[mid]:
                #if the left side is sorted, 

                if nums[l] <= target < nums[mid]:
                    r = mid-1
                elif nums[mid] == target:
                    return mid
                else:
                    l = mid+1
                
            else:
                #if right side is sorted,

                if nums[mid] < target <= nums[r]:
                    l = mid+1
                elif nums[mid] == target:
                    return mid
                else:
                    r = mid-1

        return -1