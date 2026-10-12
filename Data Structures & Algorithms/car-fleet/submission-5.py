class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = []
        for i, j in enumerate(position):
            pos.append((j, i))
        
        pos = sorted(pos, key=lambda item: item[0], reverse=True)

        time = []
        for i in pos:
            tt = (target-i[0])/speed[i[1]]
            if time and time[-1] >= tt:
                continue
            time.append(tt)
        
        return len(time)


