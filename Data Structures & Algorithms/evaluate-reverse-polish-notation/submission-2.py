class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        special_tokens = set()
        special_tokens.update(["+", "-", "*", "/"])
        for i, val in enumerate(tokens):
            if val not in special_tokens:
                stack.append(int(val))
            else:
                right = stack.pop()
                left = stack.pop()
                if val == "+":
                    temp = left + right
                elif val == "-":
                    temp = left - right
                elif val == "*":
                    temp = left * right
                elif val == "/":
                    temp = int(left / right)
                else:
                    print("error")
                    return 0
                stack.append(temp)
        return stack.pop()