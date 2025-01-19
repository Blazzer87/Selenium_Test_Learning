"""
объект - контейнер состоящий из
1) данные и состояние (атрибуты)
2) поведение

Данные и поведения
а = [3, 4, 21] где,
3, 4, 21 - данные
поведение - это методы применимые к списку, например a.replace()

Каждый объект принадлежит к какому-то классу, напрмиер стринга, интежер или флоат, определяется по функции type
1 4 28 - это всё экземляры класса интежер
[1,2] [6,65] - это всё экземпляры класса лист(список)

объектом является ВСЁ!!

Класс - это шаблон, которым создаются объекты
Когда создаётся объект класса то его АВТОМАТИЧЕСКИ наделяют поведением свойственным этому классу

"""

my_list = [3, 4, 21]
print(isinstance(my_list,list))         # TRUE
print(isinstance(my_list,object))         # TRUE объектом является всё

class Car:
    pass

bmw = Car() # создали объект класса

class Car:
    model = "BMW"
    engine = 1.6


class Person:
    # конструктор
    def __init__(self):
        print("Создание объекта Person")


tom = Person()  # Создание объекта Person