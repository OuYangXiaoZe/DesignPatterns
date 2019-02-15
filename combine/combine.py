# 组合模式
# #
# #      定义:将对象组合成树形结构以表示'部分-整体'的层次结构.组合模式使得用户对单个对象和组合对象的使用具有一致性
# #
# #      角色:抽象组件,叶子组件,复合组件,客户端
# #
# #      适用场景:表示对象的'部分-整体'层次结构,希望用户忽略组合对象与单个对象的不同,用户统一使用组合结构中的所有对象
# #
# #      优点:定义了包含基本对象和组合对象的类层次结构,简化客户端代码,即客户端可以一致的使用组合对象和单个对象,更容易新增新类型的组件
# #
# #      缺点:很难限制组合中的组件
from abc import abstractmethod, ABCMeta

#-------抽象组件--------
class Graph(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add(self,graph):
        pass

    def get_children(self):
        pass

#---------叶子组件--------
class Point(Graph):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(self)

    def add(self,graph):
        raise TypeError

    def get_children(self):
        raise TypeError

    def __str__(self):
        return '点(%s,%s)'%(self.x,self.y)


class Line(Graph):

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        print(self)

    def add(self,graph):
        raise TypeError

    def get_children(self):
        raise TypeError

    def __str__(self):
        return '线段(%s,%s)'%(self.p1,self.p2)

#--------复合组件---------
class Picture(Graph):
    def __init__(self):
        self.children = []

    def add(self,graph):
        self.children.append(graph)

    def get_children(self):
        return self.children

    def draw(self):
        print('-----复合图形-----')
        for g in self.children:
            g.draw()
        print('结束')


#---------客户端---------
pic1 = Picture()
point = Point(2,3)
pic1.add(point)
pic1.add(Line(Point(1,2),Point(4,5)))
pic1.add(Line(Point(0,1),Point(2,1)))

pic2 = Picture()
pic2.add(Point(-2,-1))
pic2.add(Line(Point(0,0),Point(1,1)))

pic = Picture()
pic.add(pic1)
pic.add(pic2)

pic.draw()