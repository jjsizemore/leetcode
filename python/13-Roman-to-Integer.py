# region Left to Right


class Solution:
    def romanToInt(self, s: str) -> int:
        toInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0

        i = 0

        while i < len(s):
            curInt = toInt[s[i]]
            if i < len(s) - 1 and curInt < toInt[s[i + 1]]:
                total -= curInt
            else:
                total += curInt
            i += 1
        return total


# endregion

# region Right to Left


class Solution:
    def romanToInt(self, s: str) -> int:
        toInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = toInt[s[len(s) - 1]]

        i = len(s) - 2

        while i >= 0:
            curInt = toInt[s[i]]
            rtInt = toInt[s[i + 1]]
            if curInt < rtInt:
                total -= curInt
            else:
                total += curInt
            i -= 1
        return total


# endregion
