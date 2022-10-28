
#  Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input("Enter number: "))
# def f(i):
#     return (3*i)+1

# dictionary = [(i, f(i)) for i in range(1, n+1)]
# print(dictionary)


# n = int(input("Enter number: "))
# factorial_list = []
# factorial = 1
# for i in range(1, n+1):
#     if (n > 0):
#         factorial = (i * factorial)
#         factorial_list.append(factorial)
# print(factorial_list)


# factorial = 1
# n = int(input("Enter number: "))
# def f(x, factorial):
#     return x * factorial

# factorial_list = [f(i) for i in range(1, n+1) if n > 0]
# print(factorial_list)


#  Task № 3
# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55


n = int(input('Enter number: '))
amount = 0


def f(x):
    return (1+(1/x))**x


n_list = [f(i) for i in range(1, n+1)]
print(n_list)
for i in range(len(n_list)):
    amount += n_list[i]
print(amount)
