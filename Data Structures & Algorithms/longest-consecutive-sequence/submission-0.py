class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_s = set(nums)
        max_counter = 0
        for x in set_s:
            if x - 1 not in set_s:
                counter = 1
                while x + 1 in set_s:
                    counter += 1
                    x += 1
                max_counter = max(max_counter, counter)
        return max_counter