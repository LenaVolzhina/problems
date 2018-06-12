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
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        if target < 0:
            print("R", end=' ')
            return 1 + self.racecar(-target)

        # find closest 2 ^ n
        left, left_n = 1, 0
        while left * 2 - 1 < target:
            left *= 2
            left_n += 1
        right = left * 2 - 1
        left = left - 1
        # now left = 2 ^ n - 1 <= target < 2 ^ (n + 1) - 1
        print("({}, {}, {})".format(left, target, right), end=' ')
        if target == left:
            print("A{}".format(left_n), end=' ')
            return left_n
        elif target == right:
            print("A{}".format(left_n + 1), end=' ')
            return left_n + 1
        if target - left < right - target:
            # 2 ^ n is closer
            print("A{}RR".format(left_n), end=' ')
            return left_n + 2 + self.racecar(target - left)
        else:
            print("A{}R".format(left_n + 1), end=' ')
            return left_n + 2 + self.racecar(right - target)
