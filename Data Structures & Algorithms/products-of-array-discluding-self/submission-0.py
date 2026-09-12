class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        final = []
        total = 1
        for num in nums:
            total = total * num
            pre.append(total)
        total = 1
        for num in reversed(nums):
            total = total * num
            post.append(total)
        post.reverse()
        pre_temp = 0
        post_temp = 0
        for i,num in enumerate(nums):
            if (i -1 < 0):
                pre_temp = 1
            else:
                pre_temp = pre[i -1]
            if (i+1 >= len(nums)):
                post_temp = 1
            else:
                post_temp = post[i + 1]
            final.append(pre_temp * post_temp)
        return final


            
        

