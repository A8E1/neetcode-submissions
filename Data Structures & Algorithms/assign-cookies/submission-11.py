class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_pointer = 0
        s_pointer = 0
        content_count = 0

        s.sort()
        g.sort()
        while g_pointer < len(g) and s_pointer < len(s):

            if g[g_pointer] <= s[s_pointer]:
                content_count += 1
                g_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1


        return content_count

                
                    
