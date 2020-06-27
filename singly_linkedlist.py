class Node(object):
    def __init__(self, data=None, next=None):
        super(Node, self).__init__()
        self.data = data
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.data, self.next)


class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self.size = 0

    def size(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count +=1
            curr_node = curr_node.next

        return count


    def find(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return Node(curr_node.data,curr_node.next)
            curr_node = curr_node.next
        raise ValueError("value not found")

    def update(self, data, new_data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                curr_node.data == new_data
                return True
            curr_node = curr_node.next
        raise ValueError("value not found")

    def push_front(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        count += 1


    def pop_front(self):
        curr_node = self.head

        if curr_node :
            self.head = curr_node.next
            curr_node = None
            self.size -= 1

        else:
            raise ValueError("Empty list ")


    def top_front(self):
        if self.head:
            return self.head
        raise ValueError("Empty list ")

    def push_back(self, data):
        new_node = Node(data)
        count += 1

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
        last_node.next = new_node

        return True


    def pop_back(self):
        if self.head is None:
            raise  ValueError("Empty list ")
        else:
            last_node = self.head
            prev_node = None
            while last_node.next:
                 prev_node = last_node
                 last_node = last_node.next

            if not prev_node:
                     self.head = None
            else:
                last_node = None
                prev_node.next = None
        count  -= 1

        return True



    def top_back(self):
        if self.head is None:
            raise ValueError("Empty list ")
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
        return last_node

    def remove(self, data):
        curr_node = self.head
        prev_node = None

        while curr_node:
            if curr_node.data == d:
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
                self.size -= 1
                return True  # data removed
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return False  # data not found


    def _reverse_iterative(self):
        if self.head is None:
            raise  ValueError("Empty list ")
        else:
            curr = self.head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
        self.head = prev
        return True

    def reverse(self, method="recurrsive"):
        if method == "iterative":
            return self._reverse_iterative()
        else:
            self._reverse_recurrsive(None, self.head)
            return self.head

    def _reverse_recurrsive(self, prev, curr):
        if self.head is None:
            raise ValueError("Empty list ")
        else:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            prev = _reverse_recurrsive(prev, curr)
        self.head = prev
        return self


        #print("Complete the implementation")

    def __str__(self):
        result = "\n*** LinkedList ***\n"
        node = self.head
        while node:
            result += "{} -> ".format(node)
            node = node.next

        result += "None"

        return result