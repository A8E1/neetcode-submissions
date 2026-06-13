class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket_freq = [[] for i in range(len(nums)+1)]

        freq_dict = {}

        res = []

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        for num, freq in freq_dict.items():
            bucket_freq[freq].append(num)
        
        for i in range(len(bucket_freq)-1, 0, -1):
            for num in bucket_freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res