# 适配器模式
#
#      定义:将一个接口转换为客户希望的另一个接口,该模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作
#
#      角色:目标接口,待适配的类,适配器
#
#      适用场景:想使一个已经存在的类,但其接口不符合你的要求.想对一些已经存在的子类.不可能每一个都是用子类来进行适配,对象适配器可以适配其父类接口

from abc import abstractmethod, ABCMeta


#基类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError

#某一种实现类
class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元"%money)

#某一种实现类
class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)

#------待适配的类-----
class WeChatPay:
    def fuqian(self,money):
        print('微信支付%s元'%money)

#------类适配器------
class RealWeChatPay(Payment,WeChatPay):
    def pay(self, money):
        return self.fuqian(money)

#-----对象适配器-----
class PayAdapter(Payment):
    def __init__(self,payment):
        self.payment=payment
    def pay(self, money):
        return self.payment.fuqian(money)

#RealWeChatPay().pay(100)

p=PayAdapter(WeChatPay())
p.pay(200)

