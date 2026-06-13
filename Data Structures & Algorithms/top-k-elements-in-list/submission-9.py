class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        num_freq_bucket = [[] for i in range(len(nums)+1)]

        for num, freq in num_freq.items():
            num_freq_bucket[freq].append(num)

        res = []

        for i in range(len(num_freq_bucket)-1, 0, -1):
            for num in num_freq_bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
        

        
        