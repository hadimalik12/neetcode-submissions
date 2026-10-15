class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = []
        self.tm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        times = self.tm[key]

        l = 0
        r = len(times) - 1
        res = ""

        while l <= r:
            m = l + (r-l)//2

            if times[m][1] <= timestamp:
                res = times[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

