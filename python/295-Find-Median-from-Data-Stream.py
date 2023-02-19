# region Two Heaps
# This solution has a better run time than the shorter one because there are at worst 2 pushes and 1 pop during insertion
import heapq


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap) + 1:
                elem = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -elem)
        else:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) > len(self.minHeap):
                elem = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -elem)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) * 0.5
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# endregion

# region Two Heaps Shorter
# This solution runs slower than the one above because there are at worst 3 pushes and 2 pops during insertion, but it's more concise

import heapq


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) * 0.5
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# endregion

# region Insertion Sort


class MedianFinder:
    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        if not self.vals:
            self.vals.append(num)
        else:
            left, right = 0, len(self.vals)

            while left < right:
                mid = left + (right - left) // 2
                if self.vals[mid] > num:
                    right = mid
                else:
                    left = mid + 1

            self.vals.insert(int(left), num)

    def findMedian(self) -> float:
        size = len(self.vals)
        half = int(size // 2)

        return (
            self.vals[half]
            if size % 2
            else (self.vals[half] + self.vals[half - 1]) * 0.5
        )


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# endregion
