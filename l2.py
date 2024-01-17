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
    