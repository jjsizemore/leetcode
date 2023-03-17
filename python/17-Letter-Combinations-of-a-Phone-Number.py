from typing import List

# region Recursive DFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        toLets = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        self.retVal = []

        def helper(digits: str, lettersSoFar: List[str], start: int) -> str:
            if start == len(digits):
                return self.retVal.append("".join(lettersSoFar))
            else:
                for letter in toLets[int(digits[start])]:
                    lettersSoFar.append(letter)
                    helper(digits, lettersSoFar, start + 1)
                    lettersSoFar.pop()

        helper(digits, [], 0)

        return self.retVal


# endregion
