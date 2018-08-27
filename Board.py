# 第四周作业：8-puzzle problem,在3*3棋盘上移动8个方形棋子让其有序
# 采用 A*（A star）算法，计算两种权重Hamming priority function 和Manhattan priority function来衡量与目标的距离，每次弹出权重小的
# 采用优先队列的数据结构MinPQ，每次弹出权重最小的（与目标最相似的）
# Board.py初始化棋盘
# 大神的讲解https://blog.csdn.net/zhangyuzuishuai/article/details/68167420

#算法真的好难 *6

import math


class Board(object):
    # 传入N*N的数组作为棋盘，blocks使用1维数组节省内存
    def __init__(self, blocks):
        self.blocks = blocks
        self.N = int(math.sqrt(len(blocks)))

    # 返回数组的维数
    def dimension(self):
        return self.N

    # 计算hamming priority function
    def hamming(self):
        haming = 0
        for i in range(len(self.blocks)):
            if self.blocks[i] != 0 and self.blocks[i] != i+1:
                haming += 1
        return haming

    # 计算Manhattan priority function
    def manhattan(self):
        manhattan = 0
        for i in range(len(self.blocks)):
            if self.blocks[i]!= 0 and self.blocks[i] != i+1:
                row_dis = abs(i // self.N - (self.blocks[i]-1)//self.N)
                col_dis = abs(i % self.N - (self.blocks[i]-1) % self.N)
                manhattan += (row_dis+ col_dis)
        return manhattan

    # 判断是否为目标
    def isGoal(self):
        return self.hamming() == 0

    # 找到该棋盘的双胞胎棋盘，是为了之后判断问题可解提供方便
    # 棋盘和他的双胞胎棋盘只有一个可解
    # 交换1，2或最后两个（看空位在哪）改变数组的逆序数的奇偶性即可
    def twin(self):
        twinblocks = self.blocks.copy()
        if twinblocks[0] != 0 and twinblocks[1] != 0:
            self._swap(twinblocks, 0, 1)
        else:
            self._swap(twinblocks, len(twinblocks) - 1, len(twinblocks) - 2)
        return Board(twinblocks)

    # 交换一个数组的两个数
    def _swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    # 比较另一个object 是否等于当前(不是很明白为毛要写这么麻烦）
    def __eq__(self, other):
        if other == None:
            return False
        if type(self).__name__ != type(other).__name__:
            return False
        if self.N != other.N:
            return False
        return self.blocks == other.blocks

    # 找遍他的所有邻居
    def __iter__(self):
        neighbors = []
        zero_index = self.blocks.index(0)
        row_move = [-1, 1, 0, 0]
        col_move = [0, 0, -1, 1]
        for i in range(4):
            arr = self.blocks.copy()
            row_index = zero_index // self.N + row_move[i]
            col_index = zero_index % self.N + col_move[i]
            if row_index < self.N and row_index >= 0 and col_index < self.N and col_index >= 0:
                newindex = row_index * self.N + col_index
                self._swap(arr, zero_index, newindex)
                neighbors.append(Board(arr))
        return iter(neighbors)

    # 以字符串的形式输出
    def toString(self):
        string = ''
        for i in range(len(self.blocks)):
            s = str(self.blocks[i],) + '  '
            if (i+1)%self.N == 0:
                s += '\n'
            string += s
        return string


#单元测试
if __name__ == '__main__':
    test = []
    file = open(r'D:\Algorithms\4\8puzzle\puzzle3x3-07.txt','r')
    L = file.readlines()
    for i in range(1,len(L)):
        s = ' '.join(L[i].split())
        s1 = s.split()
        for k in s1:
            test.append(int(k))
    bd = Board(test)
    print(bd.toString())
    print(bd.hamming())
    print(bd.manhattan())
    print(bd.dimension())
    print(bd.isGoal())
    #print(bd.twin().toString())
    for b in bd:
        print(b.toString())