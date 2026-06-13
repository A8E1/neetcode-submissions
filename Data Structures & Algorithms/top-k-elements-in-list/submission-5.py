class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  

        count = {}
        bucket_elem = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            bucket_elem[freq].append(num)
        
        res = []
        
        for i in range(len(bucket_elem)-1, 0, -1):
            for j in range(0, len(bucket_elem[i])):
                res.append(bucket_elem[i][j])
                if len(res) == k:
                    return res


        






















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
            


        
        
