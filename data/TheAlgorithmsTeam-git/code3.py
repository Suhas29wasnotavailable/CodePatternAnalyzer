class Solution:
    def binary_search(self, sorted_numbers: list, target_value: int) -> int:
        """
        Perform binary search on a sorted list.
        Returns the index of the target or -1 if not found.
        """
        left_index = 0
        right_index = len(sorted_numbers) - 1

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = sorted_numbers[middle_index]

            if middle_value == target_value:
                return middle_index
            elif middle_value < target_value:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1

        return -1
