# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key=-1, val=0, next=None, prev=None):
        self.key = key
        self.value = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keys = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node = self.keys[key]
        self.delete(key)
        self.put(node.key, node.value)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.delete(key)

        if len(self.keys) == self.capacity:
            self.delete(self.head.next.key)

        newNode = Node(key,value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.keys[key] = newNode
    
 
    def delete(self, key):
        if key not in self.keys:
            return
        
        node = self.keys[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        del self.keys[key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)