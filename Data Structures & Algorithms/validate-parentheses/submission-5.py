class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == '(' and s[i] == ')' or stack[-1] == '[' and s[i] == ']' or stack[-1] == '{' and s[i] == '}':
                        stack.pop()
                    else:
                        stack.append(s[i])
        
        if len(stack) != 0:
            return False
        else:
            return True