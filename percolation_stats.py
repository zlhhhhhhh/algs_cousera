import sys
sys.path.append(r'.\percolation')
from percolation import Percolation
import math,random

class percolation_stats(object):
    def __init__(self,N,T):
        if N < 0 or T < 0:
            raise Exception('矩阵维度与实验次数不能为负')
        self.T = T
        self.N = N
    #计算均值
    def mean(self,L):
        return float(sum(L)/len(L))

    #计算方差
    def stddev(self,L):
        m = self.mean(L)
        L1 = map(lambda x:pow((x-m),2),L)
        return float(sum(L1))/(self.T - 1) if T > 1 else 0

    def confidence_interval(self,L):
        diff = 1.96*math.sqrt(float(self.stddev(L)/self.T))
        return [self.mean(L)-diff,self.mean(L)+diff]

    def trial_stats(self):
        p_list = []
        for i in range(self.T):
            perco = Percolation(self.N)
            while (True):
                row = random.randint(1, N)
                col = random.randint(1, N)
                perco.open(row, col)
                if perco.percolated():
                    p = float(perco.grid.count(1)/(self.N*self.N))
                   # print('P = ' + str(p))
                    break
            p_list.append(p)
        print(str(self.T) + ' Times trial Mean: ' + str(self.mean(p_list)))
        print(str(self.T) + ' Times trial Stddev: ' + str(self.stddev(p_list)))
        print(str(self.T) + ' Times trial confidence interval: ' + str(self.confidence_interval(p_list)))

if __name__=='__main__':
    T = int(input('Enter your number of trials: '))
    N = int(input('Enter your size of matrix: '))
    p_stats = percolation_stats(N,T)
    p_stats.trial_stats()
