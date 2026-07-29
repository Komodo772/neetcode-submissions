class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerbound = 0
        upperbound = 0

        upperbound = len(s)-1

        while lowerbound < upperbound:

            while lowerbound < upperbound and not s[lowerbound].isalnum():
                lowerbound += 1
            while lowerbound < upperbound and not s[upperbound].isalnum():
                upperbound -= 1
            
            if s[lowerbound].lower() != s[upperbound].lower():
                return False
        
            lowerbound += 1
            upperbound -= 1

        return True