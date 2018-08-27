#归并排序的优化实现(较小数组用插入排序，使用N/2的辅助数组
#基本原理：选取辅助数组，将一个前后都有序的数组排序

#算法实在是太难了

import random
from elementary_sort import Insertion_Sort

class mergesort(object):
    def __init__(self):
        pass

    def _isSorted(self,arr):
        if len(arr) ==1:
            return True
        for i in range(len(arr)-1):
            if arr[i]<=arr[i+1]:
                return True
            else:
                raise AssertionError('Not Sorted Yet')
        return True

    def _merge(self,arr):
        result =[]
        mid = len(arr)//2
        i = 0
        j = mid

        assert self._isSorted(arr[:mid])
        assert self._isSorted(arr[mid:])

        for k in range(len(arr)):
            if (i>=mid):
                result.append(arr[j])
                j +=1
            elif j>=len(arr):
                result.append(arr[i])
                i +=1
            elif arr[i]<=arr[j]:
                result.append(arr[i])
                i += 1
            elif arr[i]>arr[j]:
                result.append(arr[j])
                j += 1
        return result

    #仿照网上的，上面那个是自己的
    def _merge1(self,arr_left,arr_right):
        i = 0
        j = 0
        aux = []

        assert self._isSorted(arr_left)
        assert self._isSorted(arr_right)

        while i<len(arr_left)and j<len(arr_right):
            if arr_left[i] <= arr_right[j]:
                aux.append(arr_left[i])
                i += 1
            else :
                aux.append(arr_right[j])
                j += 1
        aux += arr_left[i:]
        aux += arr_right[j:]
        return aux



    def sort(self,arr):
        #小于某个长度的子序列使用插入排序

        if len(arr)<=5:
            ins = Insertion_Sort(arr)
            return ins.insertion_sort()
        mid = len(arr)//2
        k = self.sort(arr[:mid])
        v = self.sort(arr[mid:])
        arr1 = k+v
        return self._merge(arr1)

    #自底向上取消了递归的使用，使用迭代的方法
    def bottome_up_sort(self,arr):
        length = len(arr)
        sz = 1
        while(sz<length):
            left = 0
            while(left<length-sz):
                hi = min(left+2*sz,length)
                mid = left+sz

                #这里应该还可以再优化一下，我不知道python怎么能偶传一个切片然后修改原来的数组
                k = self._merge1(arr[left:mid],arr[mid:hi])

                count = 0
                for i in range(left,hi):
                    arr[i] = k[count]
                    count  +=1
                left += 2*sz
            sz *=2
        return  arr

    def create_aux(self,arr):
        aux = arr
        return aux

if __name__ == '__main__':
    test = list(range(-50,50))
    random.shuffle(test)
    print(test)
    ms = mergesort()
    print(ms.bottome_up_sort(test))
