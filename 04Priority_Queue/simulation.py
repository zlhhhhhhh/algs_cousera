#模拟小球碰撞
#simulation.py设置物理模型：hard-disc模型

def f(n):
    for i in range(n):
        yield i**2

for i in f(8):
    print(i)


