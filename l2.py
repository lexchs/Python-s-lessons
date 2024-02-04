# Задача №9. Общее обсуждение
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

# n = int(input())
# count = 1
# cn = 1

# while count != n+1:
#     cn = cn * count
#     count+=1
#     print(cn)
# print(cn)

# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input())
#
# count = 1
# fn1 = 0
# fn2 = 1
# fns = 1
#
# while fns <= a:
#     fns = fn1 + fn2
#     fn1 = fn2
#     fn2 = fns
#     count = count + 1
# print(count)

#Input: 6 -> -20 30 -40 50 10 -10
#Output: 2

#days = int(input('How many days: '))
#count = 0
#g=1
#b=0
#while days>0:
#	d=int(input(f'How many degrees was in {g} day: '))
#	days=days-1
#	g+=1
#	if d >0:
#		count=count+1
#		if count>b:
#			b=count
#	else:
#		count=0
#print(b)


#Input: 5 -> 5 1 6 5 9
#Output: 1 9

#wms=int(input('How many watermelons: '))
#g=1
#wgtmax=0
#wgtmin=9999
#while wms>0:
#	wgt=int(input(f'How much does the {g} watermelon weigh?'))
#	g+=1
#	wms-=1
#	if wgt>wgtmax:
#		wgtmax=wgt
#	if wgt<wgtmin:
#		wgtmin=wgt
#print(wgtmin,wgtmax)


#coins=int(input('How much coins on the table: '))
#e=0
#r=0
#while coins>0:
#	side=int(input('What side: '))
#	if side == 0:
#		e+=1
#	elif side == 1:
#		r+=1
#	else:
#		print('The wrong side!')
#	coins-=1
#if r>e:
#	r=e
#print(r)


#s=int(input('Sum of two numbers: '))
#p=int(input('Proizvedenie of two numbers: '))

#m=s/(p+1)
#b=m*p
#print(m,b)

#n=int(input('Enter the number: '))
#q=1
#while n>q:
#	print(q)
#	w=q*2
#	q=w
    

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

# s = input()
# a = s.split()
# for i in range(len(a)):
#     if i%2==0:
#         print(a[i])

# Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     if a[i]%2==0:
#         print(a[i])


# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# a = [int(s) for s in input().split()]
# for i in range(len(a)-1):
#     if a[i] < a[i + 1]:
#         print(a[i + 1])


# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

# a = [int(s) for s in input().split()]
# for i in range(len(a) - 1):
#     if a[i] * a[i + 1] > 0:
#         print(a[i],a[i+1])
#         break


# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и
# выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.


# a=[int(s) for s in input().split()]
# count=0
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         count+=1
# print(count)

#
# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

# a=[int(s) for s in input().split()]
# print(max(a))
# print(a.index(max(a)))

#
# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему
# это сделать.
# Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в
# строю.
# После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
#
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же,
# как у Пети, то он должен встать после них.


# a=[int(s) for s in input().split()]
# p=int(input())
# for i in range(len(a)-1):
#     if p<=a[i] and p > a[i+1]:
#         print(i+2)
# if p>a[0]:
#     print(1)
# elif p<a[len(a)-1]:
#     print(len(a)+1)

#
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X


# a=[0]*int(input())
# for i in range(len(a)):
#     a.append(int(input()))
# print(a.count((int(input()))))

#
# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

# a = [int(s) for s in input().split()]
# c=0
# for i in range(len(a)-1):
#     if a[i]!=a[i+1]:
#         c+=1
# print(c)


# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.