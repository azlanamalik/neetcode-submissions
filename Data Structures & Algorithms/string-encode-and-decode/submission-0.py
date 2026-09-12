class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_encoded = ""
        for word in strs:
            for letter in word:
                new = chr(ord(letter) + 1)
                strs_encoded = strs_encoded + new
            strs_encoded = strs_encoded + " "
        print(strs_encoded)
        return strs_encoded
            

    def decode(self, s: str) -> List[str]:
        array = []
        word = ""
        for letter in s:
            if letter == " ":
                array.append(word)
                word = ""
            else:
                word = word + chr(ord(letter) - 1)
        return array