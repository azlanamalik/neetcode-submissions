class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        r = 0
        in_curr = set()
        temp = 0
        max_in_arr =0
        while r < len(s):

            while s[r] in in_curr:
                in_curr.remove(s[l])
                l += 1
                temp -= 1

            temp += 1
            in_curr.add(s[r])

            if temp > max_in_arr:
                max_in_arr = temp

            r = r + 1
        return max_in_arr


