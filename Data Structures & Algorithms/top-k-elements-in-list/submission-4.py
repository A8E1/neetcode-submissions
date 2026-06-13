class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        #strategy: build a hashmap that contains val:freq
        #deconstruct hashmap into an array where we can then sort descending order of freqs
        #return k first elements of array

        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        num_freq_arr = []

        for num, freq in num_freq.items():
            num_freq_arr.append((freq, num))
        
        num_freq_arr.sort(reverse=True)


        k_freq_elems = []

        for i in range(0, k):
            k_freq_elems.append(num_freq_arr[i][1])

        return k_freq_elems



        






















        # #goal is to track elems and corresponding frequencies
        # #hashmaps are the best data stx for this operation for O(1) lookups

        # elem_freq_map = {}

        # for num in nums:
        #     elem_freq_map[num] = 1 + elem_freq_map.get(num, 0)
        #     #.get() method retrieves value from passed key (first param), or returns fall back val (second param)
        
        # #now we have a built hashmap that has elem and corresponding frequency
        # #problem is we can't look up based on frequencies rn, which is what problem is asking us to do
        # #so we gotta convert hashmap => array that we can order based on freq. and retrieve elements from it
        # #hashmap => tuple (freq, elem) array => sort descending order based on freq => look up based on 1st elem freq

        # elem_freq_tuple_arr = []

        # for elem, freq in elem_freq_map.items():
        #     elem_freq_tuple_arr.append((freq, elem))
        
        # elem_freq_tuple_arr.sort(reverse=True)

        # result_elem = []
        # for i in range(k):
        #     result_elem.append(elem_freq_tuple_arr[i][1])

        # return result_elem
            












        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
            


        
        
