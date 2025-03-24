# # MRO (Method Resolution Order)
# class Animal:
#     def action(self):
#         return print('Some action')
#                                                          # Animal
# class Flyable(Animal):                          #Flyable            # Swimmable
#     def action(self):                                     # Duck
#         super().action()
#         # return print("Fly")
#
# class Swimmable(Animal):
#     def action(self):
#         super().action()
#         # return print("Swim")
#
# class Duck(Swimmable, Flyable):
#     def make_sound(self):
#         return print('Krya krya')
#
#
# donald_duck = Duck()
#
# donald_duck.action()
# # donald_duck.make_sound()
# # print(Duck.mro())



# Big O нотация — это способ описания сложности алгоритмов. Она показывает,
# # как время выполнения или использование памяти увеличивается при росте размера входных данных n.



# O(1) – Константная сложность

def get_element(list, index):
    return list[index]

list1=[1,2,3,4,5,6,7,8,9,10,]

# print(get_element(list1, 3))


# O(n) – Линейная сложность
                        #4567891023
def find_element(lst, target):
    for i in lst:
        if i == target:
            return i

# print(find_element(list1, 4))

# list1=[1,2,3,4,5,6,7,8,9,10,]
# O(log n) – Логарифмическая сложность
def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# print(binary_search(list1, 6))


# O(n²) – Квадратичная сложность
def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

list2 = [2,5,9,11,32,66,77,334,12,99,221,33,99,12,33,455,]
# bubble_sort(list2)
print(list2.sort())




