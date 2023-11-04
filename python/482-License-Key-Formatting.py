class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        s = s.upper()

        s = s[::-1]

        pieces = [s[i : i + k] for i in range(0, len(s), k)]

        s = "-".join(pieces)

        return s[::-1]
