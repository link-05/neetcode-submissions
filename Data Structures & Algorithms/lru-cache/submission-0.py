class LRUCache:
    # setup a doubly linked list
    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next= None
    # Setup hash tables to doubly linked lists
    # oldest - other - newest
    def __init__(self, capacity: int):
        self.oldest = self.Node()
        self.newest = self.Node()
        self.oldest.next = self.newest
        self.newest.prev = self.oldest
        self.capacity = capacity
        self.size = 0
        self.cache = {}

    def insert_at_newest(self, target: Node):
        # n <-> newest - prev -> n
        # n <- newest - prev <-> n
        # n - newest <- prev <-> n
        # n - newest <-> prev <-> n
        target.prev = self.newest.prev
        self.newest.prev.next = target
        target.next = self.newest
        self.newest.prev = target

    def evict(self):
        # old -> n <-> nn
        # nn <- old -> n <-> nn
        # nn <- old -> n <- nn
        # nn <- old -> nn -> n
        # old -> nn -> n
        # old <-> nn - n
        evicted = self.oldest.next
        self.remove(evicted)
        return evicted

    def remove(self, target: Node) -> None:
        # key -> cache -> node
        # p <- node <-> n <- p
        # p <- node -> n <-> p
        # p <-> n - node - 
        target.prev.next = target.next
        target.next.prev = target.prev
        target.next = None
        target.prev = None

    def get(self, key: int) -> int:
        target = self.cache.get(key)
        if target is not None:
            self.remove(target)
            self.insert_at_newest(target)
            return target.value
        return -1

    def put(self, key: int, value: int) -> None:
        target = self.cache.get(key)
        if target is not None:
            target.value = value
            self.remove(target)
            self.insert_at_newest(target)
        else:
            self.size += 1
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            if self.size > self.capacity:
                evicted = self.evict()
                self.cache[evicted.key] = None
            self.insert_at_newest(new_node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)