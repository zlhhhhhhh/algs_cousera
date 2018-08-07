import sys,random
sys.path.append(r'.\union_find')
from union_find import Weighted_Quick_Union
#原题地址为http://coursera.cs.princeton.edu/algs4/assignments/percolation.html

class Percolation(object):
    def __init__(self,N):
        if N < 0:
            raise Exception('N不能为负')
        self.N = N
        self.grid = [0 for i in range(N*N+2)]
        self.wqu = Weighted_Quick_Union(self.grid)
        self.virtual_top = N*N
        self.virtual_bottom = N*N+1

    def percolated(self):
        #print(self.wqu.Connected(self.virtual_top,self.virtual_bottom))
        return self.wqu.Connected(self.virtual_top,self.virtual_bottom)

    def open(self,row,col):
        grid_index = (row - 1)*self.N + col - 1
        if row < 1 or col < 1 or row > self.N or col > self.N:
            raise Exception('数组越界')
        self.grid[grid_index] = 1
        if row == 1:
            self.wqu.Union(self.virtual_top,grid_index)
        elif row == self.N:
            self.wqu.Union(self.virtual_bottom,grid_index)
        # 向上连通
        if row > 1:
            other = (row - 2)*self.N + col - 1
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
        #向下连通
        if row < self.N:
            other = row*self.N + col-1
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
        #向左连通
        if col > 1:
            other = (row-1)*self.N +col-2
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
        #向右连通
        if col < self.N:
            other = (row-1)*self.N + col
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)

if __name__ =='__main__':
    N = int(input('Enter your N: '))
    perco = Percolation(N)
    #手动输入
    #while(True):
    #    s = input('Enter a site as x y: ')
    #    [row,col] = [int(i) for i in s.split()]
    #    perco.open(row,col)
    #    count = count+1
    #    if perco.percolated():
    #        print(str(count)+' open site(s) to percolate the grid with size'+str(N)+'*'+str(N))
    #       break
    #随机open
    while(True):
        row = random.randint(1,N)
        col = random.randint(1,N)
        perco.open(row,col)
        if perco.percolated():
            print( str(perco.grid.count(1))+ ' open site(s) to percolate the grid with size ' + str(N) + '*' + str(N))
            break









