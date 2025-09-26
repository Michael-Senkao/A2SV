# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.myDict = dict()

    def insert(self, key: str, val: int) -> None:
        self.myDict[key] = val

    def sum(self, prefix: str) -> int:
        _sum = 0
        for key, value in self.myDict.items():
            if key.startswith(prefix):
                _sum += value

        return _sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)