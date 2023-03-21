class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.next,self.prev = None,None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dictt = dict()
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right, self.left
        
    def remove(self,node):
        node.prev.next,node.next.prev = node.next,node.prev

        
    def insert(self,node):
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next,node.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.dictt:
            self.remove(self.dictt[key])
            self.insert(self.dictt[key])
            return self.dictt[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictt:
            self.remove(self.dictt[key])
        self.dictt[key] = Node(key,value)  
        self.insert(self.dictt[key])
            
        if len(self.dictt) > self.cap:
            del self.dictt[self.left.next.key]
            self.remove(self.left.next)
                
                
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)