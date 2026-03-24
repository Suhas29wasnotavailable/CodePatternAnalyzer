class Solution:
    def count_ways_to_climb(self, total_steps: int) -> int:
        """
        Count distinct ways to climb stairs taking 1 or 2 steps.
        Uses bottom-up dynamic programming for efficiency.
        """
        if total_steps <= 0:
            return 0

        if total_steps == 1:
            return 1

        ways_for_previous_step = 1
        ways_for_current_step = 2

        for step_number in range(3, total_steps + 1):
            ways_for_next_step = ways_for_previous_step + ways_for_current_step
            ways_for_previous_step = ways_for_current_step
            ways_for_current_step = ways_for_next_step

        return ways_for_current_step
