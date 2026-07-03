class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        bucket_freq = [[] for i in range(len(nums)+1)] 
        for num, freq in num_freq.items():
            bucket_freq[freq].append(num)
        res = []
        for i in range(len(bucket_freq)-1, 0, -1):
            for j in range(len(bucket_freq[i])):
                if len(res) == k:
                    return res
                res.append(bucket_freq[i][j])
        
        return res