#take the hashmaps approach cos im cool
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_hashmap = {}
        for word in strs:
            s = [0] * 26
            for letter in word:
                s[ord(letter) - ord("a")] += 1
            key = tuple(s)
            if key not in set_hashmap:
                set_hashmap[key] = []
            set_hashmap[tuple(s)].append(word)
        return list(set_hashmap.values())

        