#快速排序，时间复杂度为O(nlogn)（概率上的），最坏的情况可到N^2,是一种不稳定的原地排序，
#主要思路为分而治之，假设一个键左右两边的子序列满足，左边的子序列都小于它，右边的子序列都大于她，那么当两边排好序时，总的序列也排好了

import random
from elementary_sort import Insertion_Sort

class quickSort(object):

    #交换数组两个数
    def _swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def _partition(self,arr,left,right):
        lo = left
        i = lo
        hi = right
        while(lo<hi):
            while(arr[hi] >= arr[i] and hi > lo):
                hi -= 1
            while(arr[lo] <= arr[i] and hi > lo):
                lo += 1
            if lo < hi:
                self._swap(arr,lo,hi)
        self._swap(arr,i,hi)
        return hi

    #算法导论的解法
    #def quick_sort(array, l, r):
    #    if l < r:
    #        q = partition(array, l, r)
    #        quick_sort(array, l, q - 1)
    #        quick_sort(array, q + 1, r)

    #def partition(array, l, r):
    #    x = array[r]
    #    i = l - 1
    #    for j in range(l, r):
    #        if array[j] <= x:
    #            i += 1

    #************************************************************
    #            array[i], array[j] = array[j], array[i] 交换两个数
    #**********************************************************

     #   array[i + 1], array[r] = array[r], array[i + 1]
     #   return i + 1

    def _quicksort(self,arr,lo,hi):
        if lo+5>=hi:
            ins = Insertion_Sort(arr)
            return ins.insertion_sort()
        k = self._partition(arr,lo,hi)
        self._quicksort(arr,lo,k-1)
        self._quicksort(arr,k+1,hi)

    def quicksort(self,arr):
        random.shuffle(arr)
        self._quicksort(arr,0,len(arr)-1)

    #针对重复的键值很多的,Dijkstra -Dutch flag problem
    def three_way_quicksort(self,arr,lo,hi):
        if lo>=hi:
            return
        i = lo
        lt = lo
        gt = hi
        v = arr[lo]
        while(i <= gt):
            if arr[i]<v:
                self._swap(arr,i,lt)
                i += 1
                lt += 1
            elif arr[i]>v:
                self._swap(arr,i,gt)
                gt -= 1
            elif arr[i] ==v:
                i += 1
        self.three_way_quicksort(arr,lo,lt-1)
        self.three_way_quicksort(arr,gt+1,hi)




if __name__ == '__main__':
    qs = quickSort()
    #test = list(range(-50,50))
    #random.shuffle(test)
    test = [3,1,2,4,8,6,5,3,6,5,-1,5,6,5,9,6,6,6,6,7]
    qs.three_way_quicksort(test,0,len(test)-1)
    print(test)




