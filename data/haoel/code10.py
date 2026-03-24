def clean_string(s):
    return [c.lower() for c in s if c.isalnum()]

def is_mirror(chars):
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left, right = left + 1, right - 1
    return True

def is_palindrome(s):
    cleaned = clean_string(s)
    return is_mirror(cleaned)
