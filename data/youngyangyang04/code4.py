class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                if char is not None:
                    stack.append(char)
            elif char == '{':
                if char is not None:
                    stack.append(char)
            elif char == '[':
                if char is not None:
                    stack.append(char)
            elif char == ')':
                if len(stack) > 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif char == '}':
                if len(stack) > 0:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif char == ']':
                if len(stack) > 0:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
