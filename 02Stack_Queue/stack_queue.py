class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class array_stack(object):
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self):
        if self._list == []:
            raise Exception('Empty Stack')
        return self._list.pop()

    def size(self):
        return len(self._list)

    def isEmpty(self):
        return self._list == []

    def __iter__(self):
        return Stackiterator(self._list.copy())

# 将栈作为一个迭代器
class Stackiterator(object):
    def __init__(self,L):
        self.L = L

    def __iter__(self):
        return self

    def __next__(self):
        if self.L == []:
            raise StopIteration('NoneType Stack')
        else:
            return self.L.pop()

class linked_stack(object):
    def __init__(self):
        self.First = Node(None)
        self.count = 0

    def push(self, item):
        newNode = Node(item)
        if self.First.value == None:
            self.First = newNode
        else:
            tempNode = self.First
            self.First = newNode
            self.First.next = tempNode
        self.count += 1

    def pop(self):
        value = self.First.value
        if (value == None):
            raise Exception('Empty Stack')
        self.First.value = None
        self.First = self.First.next
        self.count -= 1
        return value

    def size(self):

        return self.count

    def isEmpty(self):
        return self.First.value == None

    def __iter__(self):
        return linkedIterator(self.First)


class array_queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue == []:
            raise Exception('Empty Queue')
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []


class linked_queue(object):
    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)
        self.count = 0

    def enqueue(self, item):
        newNode = Node(item)
        if self.first.value == None:
            self.first = newNode
        else:
            self.last.next = newNode
        self.last = newNode
        self.count += 1

    def dequeue(self):
        if (self.first.value == None):
            raise Exception('Empty Queue')
        else:
            if self.first is self.last:
                self.last = None
            value = self.first.value
            self.first.value = None
            self.first = self.first.next
            self.count -= 1
            return value

    def size(self):
        return self.count

    def isEmpty(self):
        return self.first.value == None

    def __iter__(self):
        return linkedIterator(self.first)


class linkedIterator(object):
    def __init__(self, first):
        self.node = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.node.value is None:
            raise StopIteration
        else:
            value = self.node.value
            self.node = self.node.next
            return value


if __name__ == '__main__':
    testlist1 = [5, 3, 12, 64, 35, 95, 31, 94, 312, 84, 321, 5, 56, 9]
    testlist2 = ['my', 'life', 'is', 'simple', 'and', 'beautiful']
    # ===================
    arrstack = array_stack()

    for i in range(5):
        arrstack.push(i)
    print(arrstack.isEmpty())
    print(arrstack.size())

    print('===========================')
    linstack = linked_stack()
    print(linstack.isEmpty())
    for i in testlist2:
        linstack.push(i)
    print(linstack.size())
    for i in range(5):
        linstack.pop()
    print(linstack.size())
    for i in linstack:
        print(i)
    print('==============================')
    arrqueue = array_queue()
    print(arrqueue.isEmpty())
    for i in testlist2:
        arrqueue.enqueue(i)
    print(arrqueue.size())
    print(arrqueue.queue)
    for i in range(3):
        arrqueue.dequeue()
    print(arrqueue.queue)
    print('================================')
    linqueue = linked_queue()
    print(linqueue.isEmpty())
    for i in testlist2:
        linqueue.enqueue(i)
    print(linqueue.isEmpty())
    print(linqueue.size())
    for i in linqueue:
        print(i)
    for i in range(3):
        linqueue.dequeue()
    for i in linqueue:
        print(i)
