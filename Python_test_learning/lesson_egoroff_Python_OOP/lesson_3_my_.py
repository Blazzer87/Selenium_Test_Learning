
class PetAPI:

    def __init__(self):
        self.cost1 = 500
        self.cost2 = 500


class BaseTest:

    def setup (self):
        self.api_pet = PetAPI()


x = BaseTest()                          # создали обхект класса бейстест
y = BaseTest()


print("Вывод 1.1", x.__dict__)            # у объекта отсутствуют атрибуты так как нет инита
print("Вывод 1.2", y.__dict__)            # у объекта отсутствуют атрибуты так как нет инита

x.setup()   # выполнили функцию которая принудительно передала атрибуты
print("Вывод 2.1", x.__dict__)            # теперь у объекта есть атрибут, который является объектом класса ПЭтапи
print("Вывод 2.2", y.__dict__)            # теперь у объекта есть атрибут, который является объектом класса ПЭтапи


print("Вывод 3.1", x.api_pet.__dict__)    # запросили у объекта класса бейстест его атрибут, и обратились к атрибуту с запросом его атрибутов.
print("Вывод 3.2", y.api_pet.__dict__)    # запросили у объекта класса бейстест его атрибут, и обратились к атрибуту с запросом его атрибутов.
