from matplotlib import pyplot as plt
import  numpy as np
import random
from percolation import Percolation



class visualiser(object):
    def __init__(self,N,grid,perco):
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)
        self.grid = grid
        self.N = N
        self.perco = perco
        x = [0, 0, N, N]
        y = [0, N, N, 0]
        self.ax.axis([0, N, 0, N])
        plt.xticks(np.arange(0, N + 1, step=1))
        plt.yticks(np.arange(0, N + 1, step=1))
        self.ax.grid(color='k', linewidth=2,alpha=0.5)
        self.ax.fill(x, y, color='k')

    def opened(self):
        for i in list(range(len(self.grid))):
            grid_value = self.grid[i]
            row = int(i/self.N)+1
            col = i%self.N+1
            x1 = [col - 1, col - 1, col, col]
            y1 = [self.N - row + 1, self.N - row, self.N - row, self.N - row + 1]
            if grid_value==1:
                self.ax.fill(x1, y1, color='w')
            if self.perco.wqu2.find(i)==self.perco.wqu2.find(self.perco.virtual_top):
                self.ax.fill(x1, y1, color='b')





if __name__=='__main__':
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
    v = visualiser(N,perco.grid,perco)
    v.opened()
    plt.show()




