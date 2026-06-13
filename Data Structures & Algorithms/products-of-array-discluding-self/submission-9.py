class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suffix = [0] * n
        prefix = [0] * n
        res = [0] * n

        suffix[n-1] = 1
        prefix[0] = 1

        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]
        for i in range(n):
            res[i] = prefix[i]*suffix[i]

        return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # res = [0] * n
        # pref = [0] * n
        # suff = [0] * n

        # pref[0] = suff[n - 1] = 1
        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        # for i in range(n):
        #     res[i] = pref[i] * suff[i]
        # return res