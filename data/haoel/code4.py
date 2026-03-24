def is_opener(char):
    return char in '([{'

def get_matcher(char):
    return {')': '(', ']': '[', '}': '{'}[char]

def is_closer(char):
    return char in ')]}'

def matches_top(stack, char):
    return stack and stack[-1] == get_matcher(char)

def is_valid(s):
    stack = []
    for char in s:
        if is_opener(char):
            stack.append(char)
        elif is_closer(char):
            if not matches_top(stack, char):
                return False
            stack.pop()
    return len(stack) == 0
