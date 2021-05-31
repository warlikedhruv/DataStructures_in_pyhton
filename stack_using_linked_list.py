class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class StackLL:
    def __init__(self):
        self.head = None


    def push_val(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop_val(self):
        if self.head is None:
            return None
        else:
            del_val = self.head.data
            self.head = self.head.next
            return del_val


my_stack = StackLL()
my_stack.push_val(1)
my_stack.push_val(2)
my_stack.push_val(3)
print(my_stack.pop_val())

