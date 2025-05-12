from heapq import heapify, heappop, heappush
from typing import List


# Time O(nlogn)
# Space O(n)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        avail_rooms = [room for room in range(n)]
        heapify(avail_rooms)
        occupied_rooms = []

        meetings = sorted(meetings, key=lambda x: x[0])

        meet_counts = [0] * n

        for start, end in meetings:
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heappop(occupied_rooms)
                heappush(avail_rooms, room)

            if avail_rooms:
                room = heappop(avail_rooms)
                heappush(occupied_rooms, [end, room])
            else:
                cur_end, room = heappop(occupied_rooms)
                new_end = cur_end + (end - start)
                heappush(occupied_rooms, [new_end, room])

            meet_counts[room] += 1

        meet_max = max(meet_counts)

        return meet_counts.index(meet_max)
