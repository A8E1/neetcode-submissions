class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        num_freqs = {}
        for num in nums:
            num_freqs[num] = num_freqs.get(num, 0) + 1
        
        sorted_num_freqs = sorted(
            num_freqs.items(), 
            key=lambda num_freq: -num_freq[1]
        )

        k_freq = []

        for num_freq in sorted_num_freqs[:k]:
            k_freq.append(num_freq[0])
        
        return k_freq


