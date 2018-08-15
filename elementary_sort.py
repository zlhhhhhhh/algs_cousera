'''
Date: 2018/08/15
Author: Zoulianghao
'''
import random
import  time
#Selection_Sort requires ~1/2*N^2 Compares,Not Stable
class Selection_Sort(object):
    def __init__(self,arr):
        self.arr = arr

    def selection_sort(self):
        i = 0
        while(i<len(self.arr)-1):
            min = i
            for j in range(i+1,len(self.arr)):
                if(self.arr[j]<self.arr[min]):
                    min = j

            temp = self.arr[i]
            self.arr[i] = self.arr[min]
            self.arr[min] = temp
            i +=1
        return self.arr

#Insertion_Sort requires 1/4 N^2 Compares, Stable
class Insertion_Sort(object):
    def __init__(self,arr):
        self.arr = arr

    def insertion_sort(self):
        i = 0
        while(i < len(self.arr)):
            j = i
            while(j > 0):
                if self.arr[j] < self.arr[j-1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j-1]
                    self.arr[j-1] = temp
                    j -= 1
                else:
                    break
            i += 1
        return self.arr

#Shell Sort Cost depends on the increment of h
class Shell_Sort(object):
    def __init__(self,arr):
        self.arr = arr

    def Shell_Sort(self):
        h =1
        k = 1
        while(h<len(self.arr)//2):
            #h = 3*h+1
            h = pow(2,k)-1
            k += 1
            print(h)
        i = len(self.arr)-1

        while(h >= 1):
            for i in range(h,len(self.arr)):
                j = i
                while(j>=h and self.arr[j-h]>self.arr[j]):
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j-h]
                    self.arr[j-h] = temp
                    j -= h
            h = h//2
        return self.arr
#shuffle a deck
class shuffle(object):
    def __init__(self,arr):
        self.arr = arr

    def shuffle(self):
        for i in range(1,len(self.arr)):
            k = random.randint(0,i)
            temp = self.arr[i]
            self.arr[i] = self.arr[k]
            self.arr[k] = temp
        return self.arr

if __name__ == '__main__':
    test =list(range(400))
    test2 = ['we','live','in','a','beautiful','world','and','we','shall','cherish','it','because','it','is','vulnerable']
    random.shuffle(test)
    random.shuffle(test2)
    s = shuffle(test2)
    s.shuffle()
    print(s.shuffle())
    #ss = Selection_Sort(test2)
    #ins = Insertion_Sort(test2)
    #shs = Shell_Sort(test2)
    #print(ss.selection_sort())
    #print(ins.insertion_sort())
   # print (shs.Shell_Sort())


