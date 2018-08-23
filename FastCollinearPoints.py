#第三周作业，寻找平面上共线的四点
#快速解法：将其他点对某点的斜率进行排序，斜率相等的一组为共线的一组

#算法真的好难*4

from matplotlib import pyplot as plt
from Point import Point
from LineSegment import LineSegment
import functools

class FastCollinearPoints(object):
    #线段数目，和返回的共线线段
    def __init__(self):
        self.N = 0
        self.ls = []

    #通过计算其他点与该点的斜率来找共线
    def FastCollinearPoints(self,points):
        if points == None:
            raise TypeError('Empty Points')
        for i in range(len(points)):
            for k in range(i+1,len(points)):
                if points[i] ==points[k]:
                    raise Exception('Duplicate Points Not Allowed')
        length = len(points)
        ls = []

        for i in range(length):
            point_copy = points.copy()
            #快排是原地排序，避免原始点的顺序被打乱，新建了一个复制
            point_copy.sort(key = functools.cmp_to_key(points[i].customekey))
            j = 1
            while j < len(point_copy)-2:
                k = j
                s1 = point_copy[0].slopeto(point_copy[k])
                k += 1
                s2 = point_copy[0].slopeto(point_copy[k])
                k += 1
                while(s1 == s2):
                    if k==length:
                        k += 1
                        break
                    s2 = point_copy[0].slopeto(point_copy[k])
                    k += 1
                if k-j<4:
                    j += 1
                    continue
                pp = []
                pp.append(point_copy[0])
                for q in range(j,k-1):
                    pp.append(point_copy[q])
                pp.sort()
                if pp[0] == point_copy[0]:
                    ls.append(LineSegment(pp[0], pp[len(pp) - 1]))
                j = k-1
            self.N = len(ls)
            self.ls = ls



    def numberOfSegments(self):
        return self.N

    def segments(self):
        return self.ls

if __name__ == '__main__':
    points = []
    #file = open(r'D:\Algorithms\3\collinear\input1000.txt','r')
    #L = file.readlines()
    #for i in range(1,len(L)):
    #    s = ' '.join(L[i].split())
    #    p = Point(float(s.split()[0]),float(s.split()[1]))
    #    points.append(p)
    for i in range(8):
        for j in range(8):
            p = Point(i,j)
            points.append(p)
    for point in points:
        point.draw()


    fcp = FastCollinearPoints()
    fcp.FastCollinearPoints(points)
    ls = fcp.segments()
    print(fcp.numberOfSegments())
    for i in ls:
        i.draw()
    plt.show()








