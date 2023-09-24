class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(input: str) -> str:
            chars = []
            for elem in input:
                if elem != "#":
                    chars.append(elem)
                elif chars:
                    chars.pop()
            return "".join(chars)

        return build(s) == build(t)
