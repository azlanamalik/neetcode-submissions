class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        pointer1 = 0
        pointer1_temp = 1
        pointer2 = len(nums) -1
        pointer2_temp = 1
        for _ in nums:
            pointer1_temp = pointer1_temp * nums[pointer1]
            prefix[pointer1] = pointer1_temp
            pointer2_temp = pointer2_temp * nums[pointer2]
            postfix[pointer2] = pointer2_temp
            pointer1 += 1
            pointer2 -= 1
        #just save space by overwriting prefix
        final = [1] * len(nums)
        for i,_ in enumerate(nums):
            if (i-1) <0:
                final[i] = final[i] * postfix[1]
            elif (i+1) >= len(nums):
                final[i] = final[i] * prefix[i-1]
            else:
                final[i] = final[i] * prefix[i-1] * postfix[i+1]
        return final