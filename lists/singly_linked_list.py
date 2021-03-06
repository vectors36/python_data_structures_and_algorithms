# Singly linked lists
# A singly linked list is a list with only one pointer between two successive nodes. It can only be traversed in a
# single direction, that is, you can go from the first node in the list to the last node, but you cannot move from the
# last node to the first node.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # create empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        # populate list by appending items. Appending to head takes operation time from O(n) to O(1)
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        # Keep track of the size of the list for quick recall
        self.count += 1

    # Seperation of client concerns. Provide access point so client code doesnt access Node class
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    # Delete a node by its contents
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    # Check if a list contains an item
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False


class printSLL:
    def __init__(self):
        print("--- Singly Linked list start")
        # add new items to SinglyLinkedList
        words = SinglyLinkedList()
        words.append('egg')
        words.append('ham')
        words.append('bacon')
        current = words.tail
        # Simple method to print list output
        for word in words.iter():
            print(word)
        # print List count without needing to iterate over each element in list. taking running time from O(n) to O(1).
        print("Word count: " + str(words.count))
        words.delete('ham')
        print("After deleting word, word count is: " + str(words.count))
        # Find a word in the list using the iter method. Returns True if found False if missing.
        if words.search('bacon'):
            print("found bacon in the list.")
        print('/--- Singly Linked list end')

