class Solution:
    def isPalindrome(self, s: str) -> bool:
        Left_pointer  = 0 
        Right_pointer = len(s) -1
        not_involved_set = set()
        not_involved_set.update(['?',',', ' ', "'", '.', ":", "!"])
        while(Left_pointer <= Right_pointer):
            if (s[Left_pointer] in not_involved_set):
                Left_pointer +=1
                continue
            if (s[Right_pointer] in not_involved_set):
                Right_pointer -=1
                continue
            if s[Left_pointer].lower() != s[Right_pointer].lower():
                print(s[Left_pointer].lower())
                print(s[Right_pointer].lower())
                return False
            Left_pointer +=1
            Right_pointer -=1
        return True