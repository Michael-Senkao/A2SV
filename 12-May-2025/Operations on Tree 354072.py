# Problem: Operations on Tree - https://leetcode.com/problems/operations-on-tree/

class LockingTree:

    def __init__(self, parent: List[int]):
        self.locks = dict()
        self.parent = parent
        self.children = defaultdict(list)

        for node, par in enumerate(parent):
            self.children[par].append(node)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locks or self.locks[num] != user:
            return False
        del self.locks[num]
        return True

    def upgrade(self, num: int, user: int) -> bool:
    
        currParent = num
        while currParent != -1 and currParent not in self.locks:
            currParent = self.parent[currParent]
            
        if currParent != -1:
            return False
        oneDescLocked = self.checkDescendants(num)
        if not oneDescLocked:
            return False
        self.lockDescendants(num)
        self.locks[num] = user
        return True

    def checkDescendants(self, num):
        for child in self.children[num]:
            if child in self.locks or self.checkDescendants(child):
                return True
        return False

    def lockDescendants(self, num):
        for child in self.children[num]:
            if child in self.locks:
                del self.locks[child]
            self.lockDescendants(child)


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)