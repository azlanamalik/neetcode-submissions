class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h_map = {}
        index1 = 0
        index2 = 0
        longest_arr = 0
        while index2 < len(s):
            h_map[s[index2]] = 1 + h_map.get(s[index2], 0)
            lives = (index2 - index1 + 1) - max(h_map.values())
            if lives > k:
                h_map[s[index1]] = h_map[s[index1]] - 1
                index1 += 1
            longest_arr = max(longest_arr, index2 - index1 + 1)
            index2 += 1
            
        return longest_arr

