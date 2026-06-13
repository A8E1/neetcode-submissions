class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total_size = len(nums)

        elem_count = {}

        for num in nums:
            elem_count[num] = elem_count.get(num, 0) + 1

        maj_elem = nums[0]
        for elem, freq in elem_count.items():
            if freq > elem_count[maj_elem]:
                maj_elem = elem
        
        return maj_elem
        