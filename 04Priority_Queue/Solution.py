# 第四周作业：8-puzzle problem,在3*3棋盘上移动8个方形棋子让其有序
# 采用 A*（A star）算法，计算两种权重Hamming priority function 和Manhattan priority function来衡量与目标的距离，每次弹出权重小的
# 采用优先队列的数据结构MinPQ，每次弹出权重最小的（与目标最相似的）
# Solution.py找到最小路径
# 大神的讲解https://blog.csdn.net/zhangyuzuishuai/article/details/68167420

# 算法真的好难 * 7
from SearchNode import SearchNode
from Priorityqueue import PriorityQueue_Min as pqMin
from stack_queue import array_stack as stack
from Board import Board


class Solution(object):

    def __init__(self, bd):
        self.__isSolvable = True
        self._current = None
        self._Solver(bd)

    def _Solver(self, bd):
        if bd == None:
            raise Exception('Null Board')
        pq_Min = pqMin()
        pq_Min.insert(SearchNode(bd))
        pq_Min.insert(SearchNode(bd.twin(), flag=False))
        while (True):
            self._current = pq_Min.delMin()
            if self._current.bd.isGoal():
                break
            for nb in self._current.bd:
                if self._current.previous is None or nb != self._current.previous.bd:
                    pq_Min.insert(SearchNode(nb, previous=self._current))
        self._isSolvable = self._current.flag and self._current.bd.isGoal()

    def isSolvable(self):
        return self._isSolvable

    def moves(self):
        if self._isSolvable == False:
            return -1
        else:
            return self._current.moves

    def __iter__(self):
        if self._isSolvable == False:
            raise StopIteration('Not Solvable')

        node = self._current
        s = stack()
        i = 0
        while node != None:
            s.push(node.bd)
            node = node.previous
            i += 1
        return iter(s)


if __name__ == '__main__':
    test = []
    file = open(r'D:\Algorithms\4\8puzzle\puzzle41.txt', 'r')
    L = file.readlines()
    for i in range(1, len(L)):
        s = ' '.join(L[i].split())
        s1 = s.split()
        for k in s1:
            test.append(int(k))
    bd = Board(test)
    print(bd.toString())
    print('==================================')
    Solver = Solution(bd)
    if Solver.isSolvable() == False:
        print('UnSolvable Puzzle')
    else:
        print('Min Moves To Solve Puzzle: ', Solver.moves())
        for bd in Solver:
            print(bd.toString())
