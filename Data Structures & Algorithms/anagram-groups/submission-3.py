class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = {}
        for val in strs:
            sorted_val = str(sorted(val))
            if sorted_val in dict_str:
                dict_str[sorted_val].append(val)
            else:
                dict_str[sorted_val] = [val]
        return list(dict_str.values())