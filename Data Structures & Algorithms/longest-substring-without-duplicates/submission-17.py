class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        chars = set()

        if len(s) <= 1:
            return len(s)
        
        while r <= len(s)-1:
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])

            longest = max(longest,len(chars))
            
            #print(r, len(s)-1)
            r += 1


        return (longest)