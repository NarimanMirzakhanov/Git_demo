my_list = [2, 4, 2, 6, 4, 7, 4]
print(set(my_list))
# {2, 4, 6, 7}
set1 = {1, 2, 3, 'one', 'ten', 6}
set2 = {1, 2, 3, 'one', 'ten', 100, 525}
set3 = {"A", 0, 1, 2, 3}
print(set3.pop())
print(set3)
print(set1.union(set2))  # общее у обоих множеств
# {1, 2, 3, 'ten', 100, 6, 525, 'one'}
print(set1.issubset(set2))  # set1 является ли подмножеством set2
# False
print(set2.issuperset(set1))  # set2 включает ли в себя set1
# False
print(set2.intersection(set1))  # отличие
# {1, 2, 3, 'ten', 'one'}
print(set2.difference(set1))  # общее
# {100, 525}
print(set2.symmetric_difference(set1))  # общее у обоих сетов
# {100, 6, 525}
set1.remove(1)  # удаление по значению (не по индексу)
print(set1)
# {2, 3, 'one', 6, 'ten'}
set1.add(5)  # добавить элемент
print(set1)
# {2, 3, 'one', 6, 5, 'ten'}
print(set2)
# {1, 2, 3, 100, 'one', 525, 'ten'}
print(set1.isdisjoint(set2))  # есть ли общие значения в множествах
# False

fs = frozenset({1, 2, 3})  # заморозить SET (невозможно изменить SET)
print(fs)
# frozenset({1, 2, 3})

num = {i for i in range(int(input()))}
print(num)
