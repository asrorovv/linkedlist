class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def check(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            if last.next == new_node:
                return last.next
            last = last.next

# a = Node(3)
# b = Node(4)
# c = Node(24)
# d = Node(11)
# e = Node(7)
# arr = LinkedList()
# arr.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print(arr.printList())

# a = Node(8)
# b = Node(1)
# c = Node(12)
# d = Node(87)
# e = Node(13)
# arr = LinkedList()
# arr.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print(f"Then - {arr.printList()}")
# arr.push(33)
# print(f"After - {arr.printList()}")


# a = Node(8)
# b = Node(1)
# c = Node(12)
# d = Node(87)
# e = Node(13)
# arr = LinkedList()
# arr.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print(f"Then - {arr.printList()}")
# arr.insert(d, 12)
# print(f"After - {arr.printList()}")


# a = Node(8)
# b = Node(1)
# c = Node(12)
# d = Node(87)
# e = Node(13)
# arr = LinkedList()
# arr.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print(f"Then - {arr.printList()}")
# arr.append(19)
# print(f"After - {arr.printList()}")


# a = Node(8)
# b = Node(1)
# c = Node(12)
# d = Node(87)
# e = Node(13)
# arr = LinkedList()
# arr.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print(f"Then - {arr.printList()}")
# arr.check(13)
# print(f"After - {arr.printList()}")

# a = Node(8)
# b = Node(1)
# c = Node(12)
# d = Node(87)
# e = Node(13)
# arr = LinkedList()
# arr.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# arr.check(12)
# print(f"Cheking - {arr.printList()}")
# arr = LinkedList()
#
# data = []
# for i in range(1, 21):
#     data.append(i)
# arr.head = Node(data[0])
# for x in data[1::]:
#     arr.append(x)
# arr.insert(arr.check(8), 9)
# print(arr.printList())



