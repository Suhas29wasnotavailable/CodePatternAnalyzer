class Solution:
    def is_palindrome(self, input_string: str) -> bool:
        """
        Check whether a string is a palindrome.
        Ignores case and non-alphanumeric characters.
        """
        cleaned_characters = [
            character.lower()
            for character in input_string
            if character.isalnum()
        ]

        left_pointer = 0
        right_pointer = len(cleaned_characters) - 1

        while left_pointer < right_pointer:
            if cleaned_characters[left_pointer] != cleaned_characters[right_pointer]:
                return False

            left_pointer += 1
            right_pointer -= 1

        return True
