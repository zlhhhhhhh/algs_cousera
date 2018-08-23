#第三周作业，寻找一个平面内共线的四点
#Point.py完成点的初始化和两点的斜率计算

#算法真的好难*2

from matplotlib import pyplot as plt
import functools
import random

class Point(object):
    #(x,y)坐标初始化一个点
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #将该点画在图上
    def draw(self):
        plt.plot([self.x],[self.y],'ro')

    #在图上连接两点
    def drawto(self,point):
        plt.plot([self.x,point.x],[self.y,point.y],'b-')

    #以字符串的形式返回该点
    def toString(self):
        return '('+str(self.x)+' , '+str(self.y)+')'

    #比较两点的y坐标的大小，若相等比较x坐标的大小
    def __lt__(self, other):
        return self.y < other.y if self.y!=other.y else self.x < other.x

    def __gt__(self, other):
        return self.y > other.y if self.y!=other.y else self.x>other.x

    def __eq__(self, other):
        return self.y ==other.y and self.x ==other.x

    def __ne__(self, other):
        return self.y!=other.y or self.x!=other.x

    #计算两点间的斜率,垂直作为正无穷，自身与自身的斜率作为负无穷
    def slopeto(self,point):
        if self.__eq__(point):
            return float('-inf')
        else:
            if self.x == point.x:
                return float('inf')
            else:
                return float((self.y-point.y)/(self.x - point.x))

    #比较多点与该点的斜率，python3中取消了sort方法中的cmp参数，支持key参数，key传入的函数支持一个参数
    #可以用functools.cmp_to_key试试传多个参数
    def customekey(self,point1,point2):

        slope1 = self.slopeto(point1)
        slope2 = self.slopeto(point2)
       # print(point1.toString(),slope1,point2.toString() , slope2)
        if slope1>slope2:
            return 1
        elif slope1 ==slope2:
            return 0
        elif slope1 <slope2:
            return -1

if __name__ == '__main__':
    points = []
    for k in range(3):
        for i in range(3):
            point = Point(k,i)
            points.append(point)
            point.draw()
    for i in range(len(points)):
        print(points[i].toString())
        points.sort(key=functools.cmp_to_key(points[i].customekey))
        for j in range(len(points)):
            print(points[j].toString())
        print('=================')
    plt.show()

