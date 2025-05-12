class Solution:
    # Space O(n)
    # Time O(n)
    def isValid(self, s: str) -> bool:
        closers = {"(": ")", "[": "]", "{": "}"}

        stack = []

        # Iterate through the string, and if the char is an opener, append the corresponding closer to the stack
        # If the char is not an opener and the stack is non-empty, the top value must be the same closer
        # If the stack is empty, or the top stack value is different, the parentheses are invalid
        # If we are able to loop through the whole string and the length of the stack is 0 at the end, the parentheses are valid
        for val in s:
            if val in closers:
                stack.append(closers[val])
            else:
                if len(stack) == 0 or val != stack.pop():
                    return False
        return len(stack) == 0
