class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            self.length -= 1
            return None
        elif self.length == 1:
            temp = self.tail.value
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            new_tail = None
            while temp.next is not None:
                new_tail = temp
                temp = temp.next

            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        if self.length == 0:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp

    def get(self, index):
        if 0 > index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if 0 > index > self.length:
            return False
        if self.length == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before_node = self.get(index - 1)
        new_node.next = before_node.next
        before_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if 0 > index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        before_node = self.get(index - 1)
        temp = before_node.next
        before_node.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before_node = None
        after_node = temp.next
        while after_node is not None:
            temp.next = before_node
            before_node = temp
            temp = after_node
            after_node = after_node.next
        temp.next = before_node


new_linked_list = LinkedList(5)
new_linked_list.append(7)
new_linked_list.append(11)
new_linked_list.append(13)

new_linked_list.print_list()
print("------")
print(new_linked_list.remove(4))
print("------")

new_linked_list.print_list()
print("Reversed link list: ")
new_linked_list.reverse()
new_linked_list.print_list()

print("------")

new_linked_list.remove(1)
new_linked_list.print_list()


