from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counts = [0] * 26

        for task in tasks:
            counts[ord(task) - ord("A")] += 1

        counts.sort()

        f_max = counts.pop()

        idle_time = (f_max - 1) * n

        while counts and idle_time > 0:
            idle_time -= min(f_max - 1, counts.pop())

        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
