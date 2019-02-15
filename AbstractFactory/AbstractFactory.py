from abc import abstractmethod, ABCMeta


# 抽象产品
class PhoneShell(metaclass=ABCMeta):

    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


#抽象工厂

class PhoneFactory(metaclass=ABCMeta):

    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


#具体产品

class SmallShell(PhoneShell):
    def show_shell(self):
        print('小手机壳')


class BigShell(PhoneShell):
    def show_shell(self):
        print('打手机壳')


class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果机壳')


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print('骁龙CPU')


class MediaTekCPU(CPU):
    def show_cpu(self):
        print('联发科CPU')


class AppleCPU(CPU):
    def show_cpu(self):
        print('苹果CPU')


class Android(OS):
    def show_os(self):
        print('安卓系统')


class IOS(OS):
    def show_os(self):
        print('IOS系统')


# 具体工厂

class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_os(self):
        return Android()

    def make_cpu(self):
        return SnapDragonCPU();

class HuaweiFactoty(PhoneFactory):
    def make_shell(self):
        return  SmallShell()

    def make_os(self):
        return Android()

    def make_cpu(self):
        return  MediaTekCPU()

class AppleFactoty(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_os(self):
        return IOS()

    def make_cpu(self):
        return AppleCPU()

