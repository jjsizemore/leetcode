class Solution:
    def countTime(self, time: str) -> int:
        mm = (6 if time[3] == "?" else 1) * (10 if time[4] == "?" else 1)

        match (time[0], time[1]):
            case ("?", "?"):
                return mm * 24
            case ("?", ("0" | "1" | "2" | "3")):
                return mm * 3
            case ("?", _):
                return mm * 2
            case (("0" | "1"), "?"):
                return mm * 10
            case (_, "?"):
                return mm * 4

        return mm
