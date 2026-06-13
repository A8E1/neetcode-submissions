class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize hashmap
        balls = {}

        #iterate thru nums list and use n=element, i=index
        for testicle1, testicle2 in enumerate(nums):
        #get the difference btwn target and curr element
            sweat = target - testicle2 
        #check if the difference is in the hashmap
            if sweat in balls:
                return [balls[sweat], testicle1]
            #if it is, return index of the diff and current index
            balls[testicle2] = testicle1
        #if not, put element:index into hashmap