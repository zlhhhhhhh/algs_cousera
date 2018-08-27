# 第四周作业：8-puzzle problem,在3*3棋盘上移动8个方形棋子让其有序
# 采用 A*（A star）算法，计算两种权重Hamming priority function 和Manhattan priority function来衡量与目标的距离，每次弹出权重小的
# 采用优先队列的数据结构MinPQ，每次弹出权重最小的（与目标最相似的）
# SearchNode.py构建可以比较的棋盘
# 大神的讲解https://blog.csdn.net/zhangyuzuishuai/article/details/68167420

from Board import Board

class SearchNode(object):
    # python类不能有多个构造函数（多态），可以用默认参数的方法解决
    def __init__(self, bd, previous=None, flag=True):
        if bd == None:
            raise Exception('Null Board')
        self.bd = bd
        self.previous = previous
        if previous != None:
            self.moves = previous.moves + 1
            self.priority = self.bd.manhattan() + self.moves
            self.flag = previous.flag
        else:
            self.moves = 0
            self.flag = flag
            self.priority = self.bd.manhattan() + self.moves

    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is not None and other is None:
            return False
        elif self is None and other is not None:
            return False
        return self.priority == other.priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return (other.bd.manhattan() - self.bd.manhattan())>0
        else:
            return (other.priority - self.priority)>0

    def __gt__(self, other):
        if self.priority == other.priority:
            return (self.bd.manhattan() - other.bd.manhattan()) > 0
        else:
            return (self.priority - other.priority) > 0

if __name__ == '__main__':
    if __name__ == '__main__':
        test = []
        file = open(r'D:\Algorithms\4\8puzzle\puzzle3x3-07.txt', 'r')
        L = file.readlines()
        for i in range(1, len(L)):
            s = ' '.join(L[i].split())
            s1 = s.split()
            for k in s1:
                test.append(int(k))
        bd = Board(test)
        print(bd.toString(),bd.twin().toString())
        SN1 = SearchNode(bd)
        SN2 = SearchNode(bd.twin())
        if SN1 < SN2 :
            print('test')
