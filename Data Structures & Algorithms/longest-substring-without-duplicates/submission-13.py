class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        chars = set()

        if len(s) <= 1:
            return len(s)
        
        while r <= len(s)-1:
            if s[r] in chars:
                while s[l] != s[r]:
                    l += 1
                l += 1
            chars = set(s[l:r+1])
            
            #print(s[l:r])
            #print(chars)
            #print("------")

            if len(chars) > longest:
                longest = len(chars)
            
            #print(r, len(s)-1)
            r += 1


        return (longest)