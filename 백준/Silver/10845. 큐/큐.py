import sys

def SIZE() :
    return 10001

class Queue :
    
    def __init__(self) :
        self.queue = [-1 for _ in range(0, SIZE())]
        self.front = self.back = 0

    def isEmpty(self) :
        return self.front == self.back
    
    def isFull(self) :
        return self.front == (self.back + 1) % SIZE()
    
    def push(self, data) :
        if not self.isFull() :
            self.queue[self.back] = data
            self.back = (self.back + 1) % SIZE()
    
    def pop(self) :
        if not self.isEmpty():
            data = self.queue[self.front]
            self.front = (self.front + 1) % SIZE()
            return data
        else :
            return None
        
    def size(self) :
        return ( (self.back - self.front + SIZE()) % SIZE() )
    
    def getFront(self) :
        if not self.isEmpty() :
            return self.queue[self.front]
        else :
            return -1

    def getBack(self) :
        if not self.isEmpty() :
            return self.queue[(self.back - 1 + SIZE())%SIZE()]
        else :
            return -1

q = Queue()

N = int(sys.stdin.readline())
count = 0

for i in range(N) :
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push' :
        q.push(int(command[1]))
    elif command[0] == 'pop' :
        data = q.pop()
        print(-1 if data==None else data)
    elif command[0] == 'size' :
        print(q.size())
    elif command[0] == 'empty' :
        print(1 if q.isEmpty() else 0)
    elif command[0] == 'front' :
        print(q.getFront())
    else :
        print(q.getBack())