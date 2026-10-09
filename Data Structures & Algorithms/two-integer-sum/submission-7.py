class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Seen = {}
        for i , x in enumerate(nums):
            tocheck = target - x
            if tocheck in Seen:
                return [Seen[tocheck],i]
            Seen[x] = i

        