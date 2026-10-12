class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index1 = 0
        index2 = 0
        temp = set()
        maximum_len = 0

        while index2 < len(s):
            if s[index2] in temp:
                temp.remove(s[index1])
                index1 += 1
            else:
                temp.add(s[index2])
                maximum_len = max(maximum_len, index2 - index1 + 1)
                index2 += 1

        return maximum_len