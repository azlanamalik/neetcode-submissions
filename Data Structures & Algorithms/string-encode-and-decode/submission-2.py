class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for word in strs:
            for letter in word:
                output_str = output_str + str((ord(letter) + 10)) + "."
            output_str = output_str + "#"
        return output_str
    def decode(self, s: str) -> List[str]:
        outputLIST = []
        output = ""
        curr_letter = ""
        for number in s:
            if number == ".":
                output = output + (chr(int(curr_letter)-10))
                curr_letter = ""
            elif number == "#":
                outputLIST.append(output)
                output = ""
            else:
                curr_letter = curr_letter + number
        return outputLIST 
