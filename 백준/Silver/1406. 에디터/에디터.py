import sys

class DLL :

    def __init__(self) :
        self.head = self.tail = self.cursor = Node()

    def toString(self) :
        pointer = self.head.next
        result = []
        while pointer is not self.head :
            result.append(pointer.key)
            pointer = pointer.next
        return "".join(result)

    def L(self) :
        if self.cursor is not self.head :
            self.cursor = self.cursor.prev

    def D(self) :
        if self.cursor.next is not self.head :
            self.cursor = self.cursor.next

    def B(self) :
        if self.cursor is not self.head :
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            tmp = self.cursor.prev
            del self.cursor
            self.cursor = tmp

    def P(self, data) :
        newNode = Node(data)
        newNode.prev = self.cursor
        newNode.next = self.cursor.next
        self.cursor.next.prev = newNode
        self.cursor.next = newNode
        if self.tail is self.cursor :
            self.tail = newNode
        self.cursor = newNode

class Node :

    def __init__(self, key=None) :
        self.key = key
        self.prev = self
        self.next = self

#실행문
inputString = sys.stdin.readline().strip()
editingString = DLL()
for i in range (0, len(inputString)) :
    editingString.P(inputString[i])

M = int(sys.stdin.readline())

for _ in range (0, M) :
    command = sys.stdin.readline().strip().split()
    if command[0] == 'P' :
        editingString.P(command[1])
    elif command[0] == 'L' :
        editingString.L()
    elif command[0] == 'D' :
        editingString.D()
    else :
        editingString.B()

print(editingString.toString())
