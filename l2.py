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

a = int(input())

count = 1
fn1 = 0
fn2 = 1
fns = 1

while fns <= a:
    fns = fn1 + fn2
    fn1 = fn2
    fn2 = fns
    count = count + 1
print(count)

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
    
