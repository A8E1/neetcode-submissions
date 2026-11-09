class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        #reverse bucket sort implementation (time: O(n))

        buckets = [[] for i in range(len(nums) + 1)]

        num_freqs = {}
        for num in nums:
            num_freqs[num] = num_freqs.get(num, 0) + 1
        
        num_freqs_list = []

        for num, freq in num_freqs.items():
            num_freqs_list.append((num, freq))
        
        for pair in num_freqs_list:
            buckets[pair[1]].append(pair[0])
        
        top_k_freq = []
        for i in range(len(buckets)-1, 0, -1):
            
            for num in buckets[i]:
                if len(top_k_freq) == k:
                    return top_k_freq
            
                top_k_freq.append(num)
        
        return top_k_freq




        # num_freqs = {}
        # for num in nums:
        #     num_freqs[num] = num_freqs.get(num, 0) + 1
        
        # sorted_num_freqs = sorted(
        #     num_freqs.items(), 
        #     key=lambda num_freq: -num_freq[1]
        # )

        # k_freq = []

        # for num_freq in sorted_num_freqs[:k]:
        #     k_freq.append(num_freq[0])
        
        # return k_freq


