class TimeMap:

    def __init__(self):
        self.keyStore = {} # key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key is not in the hashmap, add a key with empty list as value
        # so we can add values to it next
        if key not in self.keyStore:
            self.keyStore[key] = []
        # add value list to the key. List contains value and timestamp
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # empty str result as if the key is not in keyStore, empty string should be returned
        res = ""
        # get all the key values from keyStore for this specific key
        values = self.keyStore.get(key, [])
        # pointers
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            # if value is less than or equal to timestamp, it is possible that the same timestamp
            # or closer to input timestamp is present towards the right, so we increase left pointer
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Time: O(n log n)
# Space: O(n)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)