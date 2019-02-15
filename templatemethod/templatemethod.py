# 模板方法模式
#
#      定义:定义一个操作中算法的骨架,将一些步骤延迟到子类中,模板方法使得子类可以不改变一个算法的结构即可重定义该算法某些特定的步骤
#
#      角色:抽象类(定义抽象的原子操作,实现一个模板方法作为算法的骨架),具体类(实现原子操作)
#
#      适用场景:一次性实现一个算法不变的部分,各个子类的公共行为,应该被提取出来集中到公共的父类中以避免代码重复,控制子类扩展
from abc import ABCMeta, abstractmethod

#----抽象类-----
class IOHandler(metaclass=ABCMeta):
    @abstractmethod
    def open(self,name):
        pass

    @abstractmethod
    def deal(self,change):
        pass

    @abstractmethod
    def close(self):
        pass
    #在父类中定义了子类的行为
    def process(self,name,change):
        self.open(name)
        self.deal(change)
        self.close()

#子类中只需要实现部分算法,而不需要实现所有的逻辑
#-----具体类--------
class FileHandler(IOHandler):
    def open(self,name):
        self.file = open(name,'w')

    def deal(self,change):
        self.file.write(change)

    def close(self):
        self.file.close()

f = FileHandler()
f.process('abc.txt','hello')