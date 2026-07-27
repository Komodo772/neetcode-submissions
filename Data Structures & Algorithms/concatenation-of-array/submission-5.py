class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = [0 for i in range(len(nums)*2)]
        
        for n in range(len(nums)):
            ans[n] = nums[n]
            ans[n+len(nums)] = nums[n]
        
        return ans