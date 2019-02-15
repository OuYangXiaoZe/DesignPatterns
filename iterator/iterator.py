#
# 迭代器模式
#
#      定义:提供一种方法可顺序访问一个聚合对象中的各个元素,而又不需要暴露该对象的内部指示
#
#      适用场景:实现方法__iter__,__next__
class LinkedList:
    class Node:
        def __init__(self,item=None):
            self.item=item
            self.next=None
    class LinkedListIterator:
        def __init__(self,node):
            self.node = node
        #实现next方法,返回下一个元素
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item

        def __iter__(self):
            return self
    def __init__(self,iterable=None):
        self.head = LinkedList.Node(0)
        self.tail = self.head
        self.extend(iterable)

    #链表尾部追加元素
    def append(self,obj):
        s = LinkedList.Node(obj)
        self.tail.next = s
        self.tail = s
    #链表自动增加长度
    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)
        self.head.item += len(iterable)

    def __iter__(self):
        return self.LinkedListIterator(self.head.next)

    def __len__(self):
        return self.head.item

    def __str__(self):
        return '<<'+', '.join(map(str,self)) + '>>'

li = [i for i in range(100)]
lk = LinkedList(li)
print(lk)