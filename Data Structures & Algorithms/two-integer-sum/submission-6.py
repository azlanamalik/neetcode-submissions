class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_of_dat = set()
        set_of_dat.update(nums)
        temp = 0
        for i,x in enumerate(nums):
            temp = (target - x)
            if temp in set_of_dat and i != nums.index(temp):
                print(temp)
                print(i)
                if i < nums.index(temp):
                    return [i,nums.index(temp)]
                else:
                    return [nums.index(temp),i]
        return
        