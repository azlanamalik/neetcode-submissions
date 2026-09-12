class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for x in nums:
            if x in set_nums:
                return True
            set_nums.add(x)
        return False

        