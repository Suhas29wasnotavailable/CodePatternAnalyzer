class Solution:
    def isPalindrome(self, s):
        cleaned = []
        for ch in s:
            if ch is not None:
                if ch.isalnum():
                    if ch.lower() is not None:
                        cleaned.append(ch.lower())
        is_palindrome = True
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] is not None and cleaned[right] is not None:
                if cleaned[left] != cleaned[right]:
                    if is_palindrome:
                        is_palindrome = False
            left += 1
            right -= 1
        return is_palindrome
