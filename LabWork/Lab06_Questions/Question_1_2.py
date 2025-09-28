from Node_Class import Node

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
    
    def insert_at_index(self, item, index):
        temp = self.head
        count = 1
        while temp.getNext() is not None and count < index:
            count += 1
            temp = temp.getNext()
        
        new_node = Node(item)
        new_node.setNext(temp.getNext())
        temp.setNext(new_node)

        if new_node.getNext() is None:
            self.tail = new_node

    def search(self, item):
        temp = self.head.getNext()  
        while temp is not None:
            if temp.getItem() == item:
                return temp          
            temp = temp.getNext()
        return None
    
    def delete(self, item):
        if self.head.getNext() is None:
            return None

        cursor = self.search(item)
        if cursor is None:
            return None
        
        precursor = self.head
        while precursor.getNext() is not cursor:
            precursor = precursor.getNext()

        precursor.setNext(cursor.getNext())

        if cursor.getNext() is None: 
            self.tail = precursor

        cursor.setNext(None)
        return cursor.getItem()


    def traverse(self):
        temp = self.head.getNext()
        print("Head->", end="")
        while temp is not None:
            print(temp.getItem(), end= "->")
            temp = temp.getNext()
        print("None")

L_list = LinkedList()
print("\n")
## Insert Note:--
## it's a 1-based List, 0th idx for Head/Dummy
# 0 idx to insert at start
# specific index to add at that index
# if index doesn't exist (too big), inserted at the end

L_list.insert_at_index(10,1)
L_list.insert_at_index(20,2)
L_list.insert_at_index(40,3)

L_list.insert_at_index(30,3)
L_list.insert_at_index(00,0)

L_list.traverse()

## Search
result = L_list.search(10)
print(f"Found Node and it's Value is: {result.getItem()}")

## Deleting
to_be_deleted = [40,30,20,10,0] ## All Case Testing
for item in to_be_deleted:
    print(f"Item Deleted: {L_list.delete(item)}")
print(f"List after Deleting {to_be_deleted}")
L_list.traverse()
print("Head and Tail are Equal after deleting all Elements:", L_list.head == L_list.tail)
print("\n")
