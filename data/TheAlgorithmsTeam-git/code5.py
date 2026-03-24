class Solution:
    def fibonacci(self, position: int) -> int:
        """
        Compute the nth Fibonacci number using dynamic programming.
        Avoids recursion to prevent stack overflow on large inputs.
        """
        if position <= 0:
            return 0

        if position == 1:
            return 1

        previous_value = 0
        current_value = 1

        for _ in range(2, position + 1):
            next_value = previous_value + current_value
            previous_value = current_value
            current_value = next_value

        return current_value
