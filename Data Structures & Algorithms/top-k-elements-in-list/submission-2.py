class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        elem_freq = {}

        for num in nums:
            #built dictionary tracking elem:freq
            elem_freq[num] = 1 + elem_freq.get(num, 0)
        
        #rn, vals are invisible for lookup. must convert to array for freq. ordering

        freq_arr = []
        for num, freq in elem_freq.items():
            freq_arr.append((freq, num))

        freq_arr.sort(reverse=True)
        result = []

        for i in range(k):
            result.append(freq_arr[i][1])
        return result












        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = {}
        # # counting occurrences
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # # converting hashmap into list then sorting occurrencs
        # count_arr = [] # [(3, 2), (2, 1)]
        # for num, count in count.items():
        #     count_arr.append([count, num])
        # count_arr.sort(reverse=True)

        # # finding top k occurrences
        # result = [] 
        # while len(result) < k:
        #     result.append(count_arr[0][1])
        #     count_arr.pop(0)
        
        # return result
            


        
        
