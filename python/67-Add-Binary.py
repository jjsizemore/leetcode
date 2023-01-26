# region Bit Computation
# Space O(max(len(a), len(b)))
# Time O(max(len(a), len(b)))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        a, b = a.zfill(maxLen), b.zfill(maxLen)

        digits = []
        carry = 0

        for i in range(maxLen - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                digits.append('1')
            else:
                digits.append('0')

            carry //= 2

        if carry == 1:
            digits.append('1')
        digits.reverse()

        return ''.join(digits)
# endregion

# region Bit Manipulation


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry

        return bin(x)[2:]
# endregion
