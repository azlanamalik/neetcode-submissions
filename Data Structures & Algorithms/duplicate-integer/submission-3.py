class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_dup = set()
        for x in nums:
            if x in set_dup:
                return True
            set_dup.add(x)
        return False