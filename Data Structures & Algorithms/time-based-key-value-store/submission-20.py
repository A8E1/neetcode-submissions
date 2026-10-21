class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_map:
            return ""
        
        val_list = self.time_map[key]
        l, r = 0, len(val_list)-1
        while l < r:
            m = (l + r+1) // 2

            if timestamp >= val_list[m][0]:
                l = m
            else:
                r = m-1
            
        if val_list[l][0] <= timestamp:
            return val_list[l][1]
        else:
            return ""



        
