class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_begin(self, inp):
        node = Node(inp)
        node.next = self.head
        self.head = node
        
    def add_end(self, inp):
        node = Node(inp)
        if self.head == None:
            self.head = node
        else:
            temp2 = self.head
            while temp2.next != None:
                temp2 = temp2.next
            temp2.next = node






    def insert(self, inp, pos=None):
        if not (0 < pos <= len(self)):
            print ("Invalid position")
            return
        node = Node(inp)
        if self.head == None:
            self.add_begin(inp)
            return

        else:
            temp2 = self.head
            for i in range(pos):
                temp2 = temp2.next
            # print(temp2.next)
            temp3 = temp2.next
            temp2.next = node
            node.next = temp3
            return




            

            
    def print(self):
        temp2 = self.head
        print("[", end=" ")
        while True:
            print(temp2.data, end=" ")
            if not temp2.next:
                break
            temp2 = temp2.next
        print("]", end="")
        # while temp2.next:
        #     print(temp2.data)
        #     temp2 = temp2.next

    def __len__(self):
        if self.head == None:
            return 0
        else:
            length = 0
            temp2 = self.head
            while True:
                length += 1
                if not temp2.next:
                    break
                temp2 = temp2.next
            return length





    # def print(self):
    #     temp2 = self.head
    #     while temp2 != None:
    #         print(temp2.data)
    #         temp2 = temp2.next






my_ll = LinkedList()
my_ll.add_end(2)
my_ll.add_end(3)
my_ll.add_end(4)
my_ll.add_end(5)
# my_ll.print()


print(f"\nLength before insertion : {len(my_ll)}")
print(f"\nLinkedList before insertion : ")
my_ll.print()
my_ll.insert(6,3)

print(f"\nLength after insertion : {len(my_ll)}")
print(f"\nLinkedList after insertion : ")
my_ll.print()