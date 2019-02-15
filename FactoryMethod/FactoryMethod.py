
from abc import  ABCMeta,abstractclassmethod


class Payment(metaclass=ABCMeta):
    #抽象产品角色
    @abstractclassmethod
    def pay(self,money):
        pass


class AiliPay(Payment):
    #具体产品角色
    def __init__(self,enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self,money):
        if self.enable_yuebao:
            print('使用余额宝支付%s元'%money);
        else :
            print('使用支付宝支付%s元'%money)


class ApplePay(Payment):
    #具体产品角色
    def pay(self,money):
        if self.enable_yuebao:
            print('使用苹果支付%s元'%money);


class PaymentFactory(metaclass=ABCMeta):
     #抽象工厂
     @abstractclassmethod
     def creat_payment(self):
         pass


class AiliPayFactory(PaymentFactory):
    #具体工厂
    def creat_payment(self):
        return AiliPay()


class ApplePayFactory(PaymentFactory):
    def creat_payment(self):
        return ApplePay()


af = AiliPayFactory()
ali = af.creat_payment()
ali.pay(100)


#如果要新增支付方式

class WechatPay(Payment):
    def pay(self,money):
        print('使用微信支付%s元'%money)

class WechatPayFactory(PaymentFactory):
    def creat_payment(self):
        return WechatPay()

w = WechatPayFactory()
wc = w.creat_payment()
wc.pay(200)


