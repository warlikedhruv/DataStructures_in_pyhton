
class Node:
    def __init__(self, datavalue):
        self.datavalue = datavalue
        self.nextvalue = None

class SingleyLinkedList:
    def __init__(self):
        self.headvalue = None

    def print_list(self):
        printvalue = self.headvalue
        while printvalue is not None:
            print(printvalue.datavalue)
            printvalue = printvalue.nextvalue

    def insert_at_beginning(self, newdata):
        new_node = Node(newdata)
        new_node.nextvalue = self.headvalue
        self.headvalue = new_node

    def insert_at_end(self, newdata):
        new_node = Node(newdata)
        if self.headvalue is None:
            self.headvalue = new_node
            return
        tail = self.headvalue
        while tail.nextvalue is not None:
            tail = tail.nextvalue
        tail.nextvalue = new_node

    def insert_between_node(self, node_value, newdata):
        new_node = Node(newdata)
        if self.headvalue.datavalue == node_value:
            self.insert_at_beginning(newdata)
            return
        reqired_node = self.headvalue
        while reqired_node.datavalue != node_value:
            reqired_node = reqired_node.nextvalue
        new_node.nextvalue = reqired_node.nextvalue
        reqired_node.nextvalue = new_node

    def remove_node(self, node_value):
        head = self.headvalue
        if head.datavalue == node_value:
            self.headvalue = head.nextvalue
            return

        while head.nextvalue is not None:
            if head.datavalue == node_value:
                break
            prev_value = head
            head = head.nextvalue
        if head is None:
            return
        prev_value.nextvalue = head.nextvalue
        head = None



singley_list = SingleyLinkedList()
singley_list.headvalue = Node("1st ele")
second = Node("2nd ele")
third = Node("3rd ele")

singley_list.headvalue.nextvalue = second
second.nextvalue = third

singley_list.insert_at_beginning("0th ele")
singley_list.insert_at_end("4th ele")
singley_list.insert_between_node("3rd ele", "3.5 ele")
singley_list.remove_node("3rd ele")
singley_list.print_list()


