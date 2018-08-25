# 第四周课程：优先队列的实现。找到N的元素的前M大的元素。主要API包括Insert,DelMin(Max)，用顺序或者乱序数组实现的复杂度是N
# 这里我们用堆(Heap)来实现

# 算法真的好难*5
import random


class PriorityQueue(object):

    def __init__(self, arr):
        self._arr = arr
        self._heap_constructor()

    # 任意排列的数组构造成二叉堆
    def _heap_constructor(self):
        self._arr.insert(0, None)
        N = len(self._arr) - 1
        k = N // 2
        # Bottom-up method
        while k >= 1:
            self._sink(k, N)
            k -= 1

    # 交换两个数
    def _swap(self, a, b):
        self._arr[a], self._arr[b] = self._arr[b], self._arr[a]


    # 插入一个数到堆的正确位置：先插到最后再向上游
    def _swim(self, k):
        while k > 1 and self._arr[k // 2] < self._arr[k]:
            self._swap(k, k // 2)
            k = k // 2

    # 某个节点不满足二叉堆的顺序，将其向下调整
    def _sink(self, k, l):
        while k <= l / 2 :
            j = 2 * k
            if j < l and self._arr[j]<self._arr[j+1]:
                j += 1
            if self._arr[k] > self._arr[j]:
                break
            self._swap(k,j)
            k = j

    # 插入一个数在堆中
    def insert(self, value):
        self._arr.append(value)
        N = len(self._arr) - 1
        self._swim(N)

    # 从堆里删除一个数
    def delMax(self):
        max = self._arr[1]
        N = len(self._arr) - 1
        self._swap(N, 1)
        self._arr.pop()
        N = N - 1
        self._sink(1, N)
        return max

    def isEmpty(self):
        return len(self._arr) <= 1

    # 堆排序,保证O(NlogN),原地(in place).
    # 先将一个任意数组构建为一个堆，依次取出根节点（最大值），与最后一个值交换，然后重新组合成堆，不断重复
    # 排序后好像没法再回到堆了，这个可以修改下，单独写一个sort
    def sort(self):
        N = len(self._arr) - 1
        while (N > 1):
            self._swap(1, N)
            N -= 1
            self._sink(1, N)

        self._arr.pop(0)
        result = self._arr
        return result


if __name__ == '__main__':
    test = ['s', 'i', 'k', 'm', 'k', 'o', 'v', 'm', 'x', 'u', 'u', 'a', 'b', 'f', 'p', 'q', 'r', 'b', 'n', 'c', 'd',
            'h']
    random.shuffle(test)
    heap = PriorityQueue(test)
    print(heap.delMax())
    heap.insert('z')
    print(heap.delMax())
    print(heap.sort())
