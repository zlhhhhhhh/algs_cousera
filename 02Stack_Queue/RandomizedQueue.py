from stack_queue import array_queue
import random

#链表为O(n)复杂度,用数组
class RandomizedQueue(object):
    def __init__(self):
        self.queue = array_queue()
        self.count = 0

    def isEmpty(self):
        return self.queue.isEmpty()

    def size(self):
        return self.count

    def enqueue(self,item):
        if item is None:
            raise Exception('add None to queue')
        self.queue.enqueue(item)
        self.count +=1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Empty queue')
        k = random.randint(0,self.count)
        value = self.queue.queue[k]
        self.queue.queue[k] = self.queue.queue[-1]
        self.queue.queue.pop()
        self.count -= 1
        return value

    def sample(self):
        if self.isEmpty():
            raise Exception('Empty queue')
        k = random.randint(0,self.count)
        return self.queue.queue[k]

    def __iter__(self):
        return Queueiterator(self.queue,0)

class Queueiterator(object):
    def __init__(self,queue,index):
        self.queue = queue
        self.index = index
        self.randomList = list(range(self.queue.size()))
        random.shuffle(self.randomList)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=self.queue.size():
            raise   StopIteration
        else:
            k = self.queue.queue[self.randomList[self.index]]
            self.index+=1
            return k

if __name__ == '__main__':
    test = ['wait','with','patience','and','she','would','show','up','at','next','corner']
    q = RandomizedQueue()
    print(q.isEmpty())
    for i in test:
        q.enqueue(i)
    print(q.size())
    for i in range(3):
        print(q.sample())




