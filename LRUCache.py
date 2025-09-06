from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curCap = 0
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            print(f"Got key {key}")
            print(self.od)
            return self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key] = value
            # recently accessed so move to beginning of queue
            self.od.move_to_end(key)
            print(f"Updated key {key}")
            print(self.od)
        else:
            if self.curCap < self.cap:
                self.curCap += 1 
            else:
                # pop from front
                self.od.popitem(last = False)

            self.od[key] = value
            print(f"Added key {key}")
            print(self.od)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4