from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        # key -> {"times": [...], "vals": [...]}
        self.store = defaultdict(lambda: {"times": [], "vals": []})

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append keeps times sorted (amortized O(1))
        self.store[key]["times"].append(timestamp)
        self.store[key]["vals"].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        times = self.store[key]["times"]
        vals = self.store[key]["vals"]

        # Find insertion index to the right of 'timestamp'
        idx = bisect_right(times, timestamp)

        if idx == 0:
            return ""            # no timestamp <= requested
        return vals[idx - 1]      # rightmost time <= requested
