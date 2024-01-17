# name = input()
# print("hi", name)
# print(f'hi {name}')

# age = int(input())
# if age < 12:
#     print("kid")
# elif age < 45:
#     print("adult")
# else:
#     print("old")

# n = 700
# m = 750
# d = m//n + (m%n>0)
# print(d)
# print(m%n)


# a = int(input("Enter how many people? "))
# b = int(input("Enter how many people? "))
# c = int(input("Enter how many people? "))

# desk = ((a+a%2)+(b+b%2)+(c+c%2))//2
# print(desk)

# i = int(input("Enter wagon's number from head: "))
# j = int(input("Enter wagon's number: "))
# if i == j:
#     print("Incorect!")
# else:
#     print(f'The train have {i+j-1} wagons')

# y = int(input('Enter the year: '))
# if y % 400 == 0 and y % 100 != 0 or y % 100 != 0 and y % 4 == 0:
#     print("Good")
# else:
#     print('Not good')


# Задача 2: Найдите сумму цифр трехзначного числа.

# n = int(input())
# fn = n//100
# sn = (n//10)%10
# tn = n%10
# print(fn+sn+tn)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# j = int(input())
# k = j//3*2
# s = p = k//4
# print(p,k,s)


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# ticket = int(input())
# fn = ticket//1000
# sn = ticket%1000
# fs = fn//100+(fn//10)%10+fn%10
# ss = sn//100+(sn//10)%10+sn%10
# if fs==ss:
#     print('Lucky ticket!')
# else:
#     print('Just a ticket(')


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))
# k = int(input("Enter k: "))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print("Yes")
# else:
#     print("No")



