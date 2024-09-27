import abc


class PaymentService(abc.ABC):
    @abc.abstractmethod
    def paypal(self):
        pass


class Site(PaymentService):
    def paypal(self):
        pass


obj = Site()
obj.paypal()

"""
class HexNumber:
    __add__:
    HexNumber()
    list(hex(int(, 16)))
    __mul__


obj_1 = HexNumber()
obj_2 = HexNumber()
print(obj_1 + obj_2)
""
"""