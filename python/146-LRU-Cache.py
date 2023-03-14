# region Doubly Linked List & Hash Map
class DLNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLNode(), DLNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            self.size += 1
            node = DLNode()
            node.key = key
            node.value = value
            self.cache[key] = node
            self._add_node(node)

            if self.size > self.capacity:
                removedNode = self._pop_tail()
                del self.cache[removedNode.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

    def _add_node(self, node) -> None:
        # Always add the node after head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLNode:
        retVal = self.tail.prev
        self._remove_node(self.tail.prev)
        return retVal


# endregion

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
