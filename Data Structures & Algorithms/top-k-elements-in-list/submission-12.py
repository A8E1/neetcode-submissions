class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        bucket_list = [[] for i in range(len(nums) + 1)]

        for num, freq in num_freq.items():
            bucket_list[freq].append(num)
        
        res = []

        for i in range(len(bucket_list)-1, -1, -1):

            if len(res) < k:
                for j in range(len(bucket_list[i])):
                    res.append(bucket_list[i][j])
            else:
                return res
        
        return res