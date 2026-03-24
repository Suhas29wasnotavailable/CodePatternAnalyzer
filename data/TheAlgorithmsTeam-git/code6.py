class Solution:
    def maximum_subarray_sum(self, numbers: list) -> int:
        """
        Find the maximum sum of a contiguous subarray.
        Uses Kadane's algorithm for O(n) time complexity.
        """
        maximum_sum = numbers[0]
        current_running_sum = numbers[0]

        for number_index in range(1, len(numbers)):
            current_number = numbers[number_index]
            current_running_sum = max(current_number, current_running_sum + current_number)
            maximum_sum = max(maximum_sum, current_running_sum)

        return maximum_sum
