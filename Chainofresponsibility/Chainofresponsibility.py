from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handel_leave(self,day):
        pass

class GeneralManagerHandler(Handler):
    def handel_leave(self,day):
        if day < 10:
            print('总经理批准请假%s天'%day)

        else:
            print('不能请假')

class DepartmentManagerHandler(Handler):
    def __init__(self):
        self.successor = GeneralManagerHandler()
    def handel_leave(self,day):
        if day < 7:
            print('部门经理批准请假%s天' % day)
        else:
            print('部门经理无权批假')
            self.successor.handel_leave(day)

class ProjectDirectorHandler(Handler):
    def __init__(self):
        self.successor = DepartmentManagerHandler()
    def handel_leave(self,day):
        if day < 3:
            print('项目经理批准请假%s天' % day)
        else:
            print('项目经理无权批假')
            self.successor.handel_leave(day)

day = 6
h = ProjectDirectorHandler()
h.handel_leave(day)