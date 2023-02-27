# region Follow the Rules
# Time O(n)
# Space O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        curIdx = 0

        while curIdx < len(s) and s[curIdx] == " ":
            curIdx += 1

        if curIdx < len(s) and s[curIdx] == "-":
            sign = -1
            curIdx += 1
        elif curIdx < len(s) and s[curIdx] == "+":
            curIdx += 1

        total = 0

        while curIdx < len(s) and s[curIdx].isdigit():
            total *= 10
            total += int(s[curIdx])
            curIdx += 1

        if total >= 1 << 31:
            if sign == 1:
                total = (1 << 31) - 1
            else:
                total = 1 << 31

        return sign * total


# endregion
