#This union-find algorithm with python

import time
#Quick_Find algorithm 0.2069(10million)
class Quick_Find(object):
    #Constructor
    def __init__(self,id):
        self.id = id

    #Connected：To find if two objects are connected
    def Connected(self,p,q):
        print(self.id[p]==self.id[q])
        return

    #Union: Connect two objects if they are not connected
    def Union(self,p,q):
        m = self.id[p]
        k = self.id[q]
        if p==q:
            return
        else:
            for i in range(len(self.id)):
                if self.id[i]== m:
                    self.id[i]= k
                    return

#Quick Union 0.2158s(10million)
class Quick_Union(object):
    #Constructor
    def __init__(self,id):
        self.id = id

    #Find:Find the root of the object
    def find(self,p):
        while(self.id[p]!=p):
            p = self.id[p]
        return p

    #Connected:To Find if Two objects are connected
    def Connected(self,p,q):
        print(self.find(p)==self.find(q))
        return self.find(p)==self.find(q)

    #Union: To connect two objects with a parent-child relation
    def Union(self,p,q):
        if self.Connected(p,q):
            print('=================')
            return
        else:
            m = self.find(p)
            n = self.find(q)
            self.id[m] = n
            return

#Weighted Quick_Union
class Weighted_Quick_Union(object):
    # Constructor
    def __init__(self, id):
        self.id = [i for i in range(len(id))]
        self.sz = [1 for i in range(len(self.id))]

    # Find:Find the root of the object
    def find(self, p):
        if p<0 or p>len(self.id):
            raise Exception('Illegal Input')
        while (self.id[p] != p):
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    #Connected:To Find if Two objects are connected
    def Connected(self,p,q):
        return self.find(p)==self.find(q)

    #Union:To Connect two objects, always link the tree with smaller size to the one with bigger size
    def Union(self,p,q):
        m = self.find(p)
        n = self.find(q)
        if self.Connected(p,q):
            return
        else:
            if self.sz[m]< self.sz[n]:
                self.id[m] = n
                self.sz[n] = self.sz[n] + self.sz[m]
            else:
                self.id[n] = m
                self.sz[m] = self.sz[n] + self.sz[n]
            return

if __name__=='__main__':
    btime = time.time()
    qf = Weighted_Quick_Union(list(range(10000000)))
    qf.Union(1,2)
    qf.Union(3,5)
    qf.Union(2,4)
    qf.Union(4,7)
    qf.Union(8,9)
    qf.Union(5,6)
    qf.Union(7,9378)
    qf.Union(997,9378)
    qf.Union(5321,1236)
    qf.Connected(1,7)
    qf.Connected(4,9)
    qf.Connected(745,9378)
    qf.Connected(1,9378)
    qf.Connected(1,997)
    etime = time.time()
    print(etime-btime)
   # print(qf.id)


