#Магические методы

#
# # Магические методы (или dunder-методы, от "double underscore") — это специальные методы в Python, которые начинаются и заканчиваются двойным подчеркиванием (__method__). Они позволяют
# # определять поведение объектов классов, например, как объекты сравниваются, выводятся, складываются и т. д.
#
#
# class Person:
#
#     def __init__(self, name="ARDAGER", age=1):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):
#         return "Я же сказал принт"
#
#     def __del__(self):
#         print(f"удаляем {self.name}")
#
#
#
#
# person1 = Person()
# print(person1)
# del person1


class Vector:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, test):
        print(f"{self.x}----")
        print(f"{test.x}----")
        return Vector(self.x + test.x, self.y + test.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # ==
    def __eq__(self, other):
        return ...

    # <
    def __lt__(self, other):
        return ...
    # >
    def __gt__(self, other):
        return ...

    def __str__(self):
        return f"Vector({self.x}-{self.y})"


# v1 = Vector(2,3)
# v2 = Vector(3,4)
# v3 = v1 + v2
# v4 = v2 - v1
# print(v3)
# print(v4)


# list_test[2]
class CustomList:

    def __init__(self, items):
        self.items = items

    # []
    def __getitem__(self, index):
        return self.items[index]

    # =
    def __setitem__(self, index, value):
        self.items[index] = value


    def __delitem__(self, index):
        del self.items[index]



# list[1] = 25
test_list = CustomList([1,2,3,4,5,6,7,8])

test_list[1] = 25
print(test_list.items)
del test_list[6]
print(test_list.items)