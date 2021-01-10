class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_set(self):
        if self is None:
            return None         
        out = set()   # Declare a set
        node = self.head  # create a temporary node object
        
        while node:
            out.add(node.value)
            node = node.next
        return out

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1 is None or llist_2 is None:
        return None

    union_set = llist_1.to_set().union(llist_2.to_set())

    if len(union_set) == 0:
        return None

    arr = LinkedList()
    for value in union_set:
        arr.append(value)
    return arr

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 is None or llist_2 is None:
        return None

    instersection_set = llist_1.to_set().intersection(llist_2.to_set())

    if len(instersection_set) == 0:
        return None

    arr = LinkedList()
    for i in instersection_set:
        arr.append(i)
    return arr

def main():
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))   #32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
    print (intersection(linked_list_1,linked_list_2)) #4 -> 21 -> 6 -> 

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23] 
    element_2 = [1,7,8,9,11,21,1]       

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4)) #65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    print (intersection(linked_list_3,linked_list_4))  # None as there are no matching elements

    # Test case 3  Edge Case

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print (union(linked_list_5,linked_list_6))   #None
    print (intersection(linked_list_5,linked_list_6))  #None

    # Test case 4  Edge Case

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23] 

    for i in element_1:
        linked_list_3.append(i)

    print (union(linked_list_3,linked_list_4))   #65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 23 ->
    print (intersection(linked_list_3,linked_list_4)) #None

if __name__ == "__main__":
    main()