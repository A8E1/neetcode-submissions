class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)*2):
            if i <= (len(nums)-1):
                output.append(nums[i])
            else:
                output.append(nums[i - len(nums)])

        return output
        