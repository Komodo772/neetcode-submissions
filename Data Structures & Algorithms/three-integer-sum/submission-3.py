class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left, right, right2, sum3 = 0,0,0,0
        nums.sort()

        output = []


        for i, a in enumerate(nums):
            if a > 0:
                break
            if i>0 and a == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left < right:
                sum3 = a + nums[left] + nums[right]
                if sum3 == 0:
                    if [a, nums[left], nums[right]] not in output:
                        output.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                
                
        return output 

                
            