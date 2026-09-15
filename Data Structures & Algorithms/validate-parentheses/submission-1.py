class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        hashmap_of_letters = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ind, letter in enumerate(s):

            if letter in hashmap_of_letters:

                if len(stack) == 0:
                    return False

                if stack[-1] == hashmap_of_letters[letter]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(letter)

        if len(stack) == 0:
            return True
        else:
            return False