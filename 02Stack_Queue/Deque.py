class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.last = None

#链表为例子,数组比较简单
class Deque(object):
    def __init__(self):
        self.first = Node(None)
        self.tail = Node(None)
        self.count = 0

    def isEmpty(self):
        return self.first.value == None

    def size(self):
        return self.count

    def addFirst(self,item):
        if item  is None:
            raise Exception('Empty item input')
        newNode = Node(item)
        if self.first.value == None:
            self.first = newNode
            self.tail = newNode
        else:
            self.first.last = newNode
            temp = self.first
            self.first = newNode
            self.first.next = temp
        self.count +=1

    def addLast(self,item):
        if item  is None:
            raise Exception('Empty item input')
        newNode = Node(item)
        if self.first.value == None:
            self.first = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            temp2 = self.tail
            self.tail = newNode
            self.tail.last = temp2
        self.count += 1

    def removeFirst(self):
        if self.first.value == None:
            raise Exception('Empty Deque')
        else:
            value = self.first.value
            self.first.value = None
            self.first = self.first.next
            self.count -= 1
            return value

    def removeLast(self):
        if self.first.value == None:
            raise Exception('Empty Deque')
        else:
            value = self.tail.value
            self.tail.value = None
            self.tail = self.tail.last
            self.count -= 1
            return value

    def __iter__(self):
        return DequeIterator(self.first)

class DequeIterator(object):
    def __init__(self,Node):
        self.node = Node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node.value== None:
            raise StopIteration
        else:
            i = self.node.value
            self.node = self.node.next
            return i

if __name__ == '__main__':
    test = ['I','do','if','I','make','a','choice','no','matter','what']
    dq = Deque()
    for i in test:
        dq.addLast(i)
    for i in range(6):
        dq.removeLast()
    for j in dq:
        print(j)
    print(dq.size())