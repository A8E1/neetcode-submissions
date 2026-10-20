class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Classify first: the pattern, why it fits, the data structure(s), the target complexity, and your confidence from 1 to 5. 

        #pattern: we do bucket sort, then iterate the array in reverse to get the top k
        #why it fits: bucket sort allows us to group values by a specific trait/bucket, therefore we group by freq
        #target complexity: we'll try for O(n), my confidence is at a 4

        buckets = [[] for i in range(len(nums)+1)]

        output = []

        num_freq_count = {}

        for num in nums:
            num_freq_count[num] = num_freq_count.get(num, 0) + 1
        
        for num, freq in num_freq_count.items():
            buckets[freq].append(num)


        for i in range(len(buckets)-1, 0, -1):
            
            for num in buckets[i]:

                if k == len(output):
                    return output
                else:
                    output.append(num)

        return output
                

        

