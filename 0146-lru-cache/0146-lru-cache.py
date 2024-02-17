class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev, self.nxt = None, None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictt = dict()
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        
    def addNode(self, node):
        first = self.head.nxt 
        first.prev = node
        node.prev = self.head
        node.nxt = first
        self.head.nxt = node
        
        
    
    
    def delNode(self, node ):
        prev = node.prev
        nxt = node.nxt
        nxt.prev = prev
        prev.nxt = nxt
        
        

    def get(self, key: int) -> int:
        if key in self.dictt:
            node = self.dictt[key]
            ans = node.val
            self.delNode(node)
            self.addNode(node)
            self.dictt[key] = self.head.nxt
            return ans
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictt:
            node = self.dictt[key]
            del self.dictt[key]
            self.delNode(node)
        else:
            if len(self.dictt) == self.capacity:
                node = self.tail.prev
                del self.dictt[node.key]
                self.delNode(node)
        self.addNode(self.Node(key,value))
        self.dictt[key] = self.head.nxt
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)