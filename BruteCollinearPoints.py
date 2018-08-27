#第三周作业，寻找平面上共线的四点
#BruteCollinearPoints.py用排序遍历四点斜率的方法找共线的四点

#算法好难*3

from Point import Point
from LineSegment import LineSegment
from matplotlib import pyplot as plt

class BruteCollinearPoints(object):

    def __init__(self):
        self.N = 0
        self.linesegments = []

    #找到所有共线的四点
    #返回值 LineSegment[]
    def BruteCollinearPoints(self,points):
        if points == None:
            raise TypeError('Empty Points')
        for i in range(len(points)):
            for k in range(i+1,len(points)):
                if points[i] ==points[k]:
                    raise Exception('Duplicate Points Not Allowed')

        points.sort()
        length = len(points)
        linesegments = []
        for i in range(length-3):
            for j in range(i+1,length-2):
                for k in range(j+1,length-1):
                    for l in range(k+1, length):
                        slope1 = points[i].slopeto(points[j])
                        slope2 = points[i].slopeto(points[k])
                        if slope1 != slope2:
                            continue
                        slope3 = points[i].slopeto(points[l])
                        if slope1==slope3:
                            linesegments.append(LineSegment(points[i],points[l]))
        self.N = len(linesegments)
        self.linesegments = linesegments

    def numberOfSegments(self):
        return self.N

    def segments(self):
        return self.linesegments

if __name__ == '__main__':
    points = []
    file = open(r'D:\Algorithms\3\collinear\input200.txt','r')
    L = file.readlines()
    for i in range(1,len(L)):
        s = ' '.join(L[i].split())
        p = Point(float(s.split()[0]),float(s.split()[1]))
        points.append(p)

    for point in points:
        point.draw()

    bcp = BruteCollinearPoints()
    bcp.BruteCollinearPoints(points)
    ls = bcp.segments()
    print(bcp.numberOfSegments())
    for i in ls:
        print(i.toString())
        i.draw()
    plt.show()






