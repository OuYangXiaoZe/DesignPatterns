class Singleton(object):
     def __new__(cls, *args, **kwargs):
         if not hasattr(cls,'_instance'):
             cls._instance = super(Singleton, cls).__new__(cls)
         return cls._instance



#继承
class MyClass(Singleton):
    def __init__(self,name):
        if name:
            self.name = name

a = MyClass('a')
print(a)
print(a.name)


b = MyClass('b')
print(b)
print(b.name)


print(a)
print(a.name)
