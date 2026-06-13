class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            sum_of_indices = numbers[l] + numbers[r]
            if sum_of_indices == target:
                return [l+1, r+1]
            elif sum_of_indices > target:
                r-=1
            else:
                l+=1
        
        