class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h_map1 = {}
        h_map2 = {}
        for char in s1:
            h_map1[char] = h_map1.get(char, 0) + 1
        index1 = 0
        index2 = len(s1) - 1
        while index2 < len(s2):
            for i in range(len(s1)):
                char = s2[index1 + i]
                h_map2[char] = h_map2.get(char, 0) + 1
            if h_map1 == h_map2:
                return True
            h_map2.clear()
            index1 += 1
            index2 += 1
        return False