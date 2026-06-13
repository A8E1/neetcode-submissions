class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first step: count frequencies of each num using a freq. hashmap
        #second step: use bucket sort to group nums under frequencies where the index represents a specific frequency
        #third step: loop backward (to get largest freq) from bucket sort array and return first k numbers

        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        bucket_sorted_freq = [[] for i in range(0, len(nums) + 1)]

        for num, freq in num_freq.items():
            bucket_sorted_freq[freq].append(num)
        
        top_k_freq = []

        for i in range(len(bucket_sorted_freq)-1, 0, -1):
            for j in range(len(bucket_sorted_freq[i])):
                top_k_freq.append(bucket_sorted_freq[i][j])
                if len(top_k_freq) == k:
                    return top_k_freq
        
        return top_k_freq



        