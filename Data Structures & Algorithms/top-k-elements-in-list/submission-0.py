class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmappy = {}
        for num in nums:
            if num not in hashmappy:
                hashmappy[num] = 0
            hashmappy[num] += 1
        print(list(hashmappy.values()))
        print(list(hashmappy.values())[len(hashmappy.values()) - k:])
        return sorted(
            hashmappy,
            key=hashmappy.get,
            reverse=True
        )[:k]