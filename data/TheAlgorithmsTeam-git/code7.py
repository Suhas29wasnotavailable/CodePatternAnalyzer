class Solution:
    def merge_sorted_arrays(self, first_array: list, second_array: list) -> list:
        """
        Merge two sorted arrays into one sorted array.
        Uses two-pointer technique for O(n + m) time complexity.
        """
        merged_result = []
        first_pointer = 0
        second_pointer = 0

        while first_pointer < len(first_array) and second_pointer < len(second_array):
            if first_array[first_pointer] <= second_array[second_pointer]:
                merged_result.append(first_array[first_pointer])
                first_pointer += 1
            else:
                merged_result.append(second_array[second_pointer])
                second_pointer += 1

        merged_result.extend(first_array[first_pointer:])
        merged_result.extend(second_array[second_pointer:])

        return merged_result
