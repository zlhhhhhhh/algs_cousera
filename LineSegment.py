#第三周作业，寻找平面上共线的四点
#Linesegment.py用于构建线段

#算法真的好难*3
from Point import Point
from matplotlib import pyplot as plt

class LineSegment(object):
    def __init__(self,point_a,point_b):
        self.start = point_a
        self.end = point_b

    def draw(self):
        plt.plot([self.start.x,self.end.x],[self.start.y,self.end.y],'b-')

    def toString(self):
        return self.start.toString()+'-->'+self.end.toString()

if __name__ == '__main__':
    p1 = Point(1.2,3.6)
    p2 = Point(5.36,8.2)
    ls = LineSegment(p1,p2)
    ls.draw()
    print(ls.toString())
    plt.show()

