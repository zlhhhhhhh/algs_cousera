import sys,random
sys.path.append(r'.\union_find')
from union_find import Weighted_Quick_Union
from matplotlib import  pyplot as plt

class Percolation(object):
    def __init__(self,N):
        if N < 0:
            raise Exception('N不能为负')
        self.N = N
        self.grid = [0 for i in range(N*N)]
        self.wqu = Weighted_Quick_Union(N*N+2)#with virtual_top & bottom
        self.wqu2 = Weighted_Quick_Union(N*N+1)
        self.virtual_top = N*N
        self.virtual_bottom = N*N+1

    def percolated(self):
        #print(self.wqu.Connected(self.virtual_top,self.virtual_bottom))
        return self.wqu.Connected(self.virtual_top,self.virtual_bottom)

    def isopen(self,row,col):
        grid_index = (row-1)*self.N+col-1
        return True if self.grid[grid_index]>0 else False

    def isFull(self,row,col):
        grid_index = (row - 1) * self.N + col - 1
        return self.wqu.Connected(self.virtual_top,grid_index)

    def open(self,row,col):
        grid_index = (row - 1)*self.N + col - 1
        if row < 1 or col < 1 or row > self.N or col > self.N:
            raise Exception('数组越界')
        self.grid[grid_index] = 1
        if row == 1:
            self.wqu.Union(grid_index,self.virtual_top)
            self.wqu2.Union(grid_index, self.virtual_top)
        elif row == self.N:
            self.wqu.Union(grid_index,self.virtual_bottom)
        # 向上连通
        if row > 1:
            other = (row - 2)*self.N + col - 1
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
                self.wqu2.Union(other, grid_index)

        #向下连通
        if row < self.N:
            other = row*self.N + col-1
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
                self.wqu2.Union(other, grid_index)


        #向左连通
        if col > 1:
            other = (row-1)*self.N +col-2
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
                self.wqu2.Union(other, grid_index)

        #向右连通
        if col < self.N:
            other = (row-1)*self.N + col
            if(self.grid[other]):
                self.wqu.Union(other,grid_index)
                self.wqu2.Union(other, grid_index)



if __name__ =='__main__':
    pass





