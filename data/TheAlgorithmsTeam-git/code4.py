class Solution:
    def is_valid_parentheses(self, input_string: str) -> bool:
        """
        Check if a string of brackets is valid.
        Uses a stack to match opening and closing brackets.
        """
        bracket_stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}

        for current_character in input_string:
            if current_character in matching_brackets:
                if not bracket_stack:
                    return False

                top_of_stack = bracket_stack.pop()

                if top_of_stack != matching_brackets[current_character]:
                    return False
            else:
                bracket_stack.append(current_character)

        return len(bracket_stack) == 0
