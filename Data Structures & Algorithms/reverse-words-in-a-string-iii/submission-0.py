class Solution:
    def reverseWords(self, s: str) -> str:

        s_list = s.split(' ')

        for i in range(len(s_list)):

            reversed_string = s_list[i][::-1]

            s_list[i] = reversed_string
        
        new_s = " ".join(s_list)
        

        return new_s



        