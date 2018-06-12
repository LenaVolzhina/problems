"""
https://leetcode.com/problems/race-car/description/
Description
Your car starts at position 0 and speed +1 on an infinite number line.
(Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 ,
otherwise speed = 1. (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.
"""
from collections import deque


class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        # [(cur_length, cur_pos, cur_speed)]
        stack = deque([(0, 0, 1)])
        # [(cur_pos, cur_speed)]
        visited = {(0, 1)}
        while True:
            cur_length, cur_pos, cur_speed = stack.popleft()
            if cur_pos == target:
                return cur_length
            moves = (
                # A:
                (cur_pos + cur_speed, cur_speed * 2),
                # R:
                (cur_pos, -1 if cur_speed > 0 else 1)
            )
            for new_pos, new_speed in moves:
                if new_pos == target:
                    return cur_length + 1
                if (new_pos, new_speed) not in visited and new_pos < 2 * target:
                    # prune visited conditions and too big positions
                    stack.append((cur_length + 1, new_pos, new_speed))
                    visited.add((new_pos, new_speed))
