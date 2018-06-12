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


class Solution:
    def __init__(self):
        # stack will contain tuples (cur_length, cur_target, cur_speed)
        self.stack = []

    def bfs(self):
        while True:
            cur_length, cur_target, cur_speed = self.stack.pop(0)
            if cur_target == 0:
                return cur_length
            # A:
            self.stack.append((cur_length + 1, cur_target - cur_speed, cur_speed * 2))
            # R:
            self.stack.append((cur_length + 1, cur_target, -1 if cur_speed > 0 else 1))

    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        self.stack.append((0, target, 1))
        return self.bfs()
