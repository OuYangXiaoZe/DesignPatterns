from abc import ABCMeta, abstractmethod
#--模仿js事件处理
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def add_event(self,func):
        pass

    @abstractmethod
    def handler(self):
        pass

class BodyHandler(Handler):
    def __init__(self):
        self.func = None

    def add_event(self,func):
        self.func = func

    def handler(self):
        if self.func:
            return self.func()
        else:
            print('已经是最后一级,无法处理')


class ElementHandler(Handler):

    def __init__(self,successor):
        self.func = None
        self.successor = successor

    def add_event(self,func):
        self.func = func

    def handler(self):
        if self.func:
            return self.func()
        else:
            return self.successor.handler()


#客户端
body = {'type': 'body', 'name': 'body', 'children': [], 'father': None}

div = {'type': 'div', 'name': 'div', 'children': [], 'father': body}

a = {'type': 'a', 'name': 'a', 'children': [], 'father': div}

body['children'] = div
div['children'] = a

body['event_handler'] = BodyHandler()
div['event_handler'] = ElementHandler(div['father']['event_handler'])
a['event_handler'] = ElementHandler(a['father']['event_handler'])

def attach_event(element,func):
    element['event_handler'].add_event(func)

#测试
def func_div():
    print("这是给div的函数")

def func_a():
    print("这是给a的函数")

def func_body():
    print("这是给body的函数")

attach_event(div,func_div)
#attach_event(a,func_a)
attach_event(body,func_body)

a['event_handler'].handler()