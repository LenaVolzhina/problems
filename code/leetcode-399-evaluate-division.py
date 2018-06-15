"""
[Medium] https://leetcode.com/problems/evaluate-division/description/
Description
Equations are given in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating point number). Given some queries, return the answers.
If the answer does not exist, return -1.0.
"""
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # populate known values
        known = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            known[x][y] = v
            if v > 0:
                known[y][x] = 1 / v

        # try to find answers
        answers = []
        for x, y in queries:
            if x not in known or y not in known:
                # no information about one of operands
                answers.append(-1.0)
            elif x == y:
                # a / a is always 1
                answers.append(1.0)
            elif y in known[x]:
                # already know the answer
                answers.append(known[x][y])
            else:
                # try to find transition between x and y
                visited, queue = {x}, deque([(x, 1)])
                while queue:
                    node, mul = queue.popleft()
                    if y in known[node]:
                        answers.append(mul * known[node][y])
                        break

                    for next_node in known[node]:
                        if next_node not in visited:
                            v = known[node][next_node]
                            queue.append((next_node, v * mul))
                            visited.add(next_node)
                else:
                    # empty queue, can't find the answer
                    answers.append(-1.0)

        return answers
