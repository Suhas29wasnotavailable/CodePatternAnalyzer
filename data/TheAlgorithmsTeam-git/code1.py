class Solution:
    def two_sum(self, numbers: list, target_value: int) -> list:
        """
        Find two indices whose values sum to the target.
        Uses a hash map for O(n) time complexity.
        """
        seen_numbers = {}

        for current_index, current_number in enumerate(numbers):
            required_number = target_value - current_number

            if required_number in seen_numbers:
                return [seen_numbers[required_number], current_index]

            seen_numbers[current_number] = current_index

        return []
