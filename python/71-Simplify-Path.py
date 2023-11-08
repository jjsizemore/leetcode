# region Stack/SB
# Time O(N) where N is the num of paths between '/' chars
# Space O(N) -- N for dirs and N for sb
class Solution:
    def simplifyPath(self, path: str) -> str:
        # split string by slash char

        # iterate through the iterable, if string is '' or '.', do nothing

        # if its '..', pop the last value from the sb, IF there is one

        # otherwise, append the string to sb

        dirs = path.split("/")
        sb = []

        for elem in dirs:
            if elem == "" or elem == ".":
                continue
            elif elem == "..":
                if sb:
                    sb.pop()
            else:
                sb.append(elem)

        return "/" + "/".join(sb)


# endregion
