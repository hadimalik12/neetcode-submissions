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
        res = -1

        while l <= r:
            m = l + (r-l)//2

            if times[m][1] == timestamp:
                return times[m][0]
            elif times[m][1] < timestamp:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        if res == -1:
            return ""
        else:
            return times[res][0]

