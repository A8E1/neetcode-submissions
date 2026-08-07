class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        length_of_value_list = len(self.time_map.get(key, ""))
        if length_of_value_list == 0:
            return ""
        
        l, r = 0, length_of_value_list-1
        max_timestamp_val = [-1, ""]
        while l <= r:
            mid = (l + r) // 2
            mid_timestamp = self.time_map[key][mid][0]
            if mid_timestamp > timestamp:
                r = mid - 1
            else:
                max_timestamp_val = [mid_timestamp, self.time_map[key][mid][1]]
                l = mid+1
        
        return max_timestamp_val[1]

                

