class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            midpoint = (left + right) // 2

            if nums[midpoint] == target:
                return midpoint

            elif nums[midpoint] < target:
                print(str(nums[midpoint]) + " less")

                left = midpoint + 1

            else:
                print(str(nums[midpoint]) + " more")

                right = midpoint - 1

            print(midpoint)

        return -1