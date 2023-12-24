#1
a = int(input("Введіть перше число : "))
b = int(input("Введіть друге число : "))
def dobytok_of_number(list):
    list = [a,b]
    num = 1
    if a > b:
        for i in range(b, a +1):
            num *= i
    else:
        for i in range(a, b +1):
            num *= i
    return num
result = dobytok_of_number(list)
print(result)


#2
def min_of_list(c):
    if c:
        minimum = c[0]
        for num1 in c:
            if num1 < minimum:
                minimum = num1
    return minimum
list_of_number = input("Введіть список чисел через пробіл : ")
list1 = [int(x) for x in list_of_number.split()]
results = min_of_list(list1)
print(results)


#3
def list_prime_num(d):
    count = 0
    for num_2 in d:
        if num_2 %2 == 0:
            count += 1
    return count
list_of_numbers = input("Введіть список чисел через пробіл : ")
list2 = [int(y) for y in list_of_numbers.split()]
result1 = list_prime_num(list2)
print(result1)
