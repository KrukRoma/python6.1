#4
def delete_of_number(a, b):
    count = 0
    for i in b:
        while i in a:
            a.remove(i)
            count += 1
    return count
list_of_numbers = input("Введіть список чисел через пробіл : ")
my_list = [int(x) for x in list_of_numbers.split()]
delete = input("Введіть числа для видалення через пробіл : ")
my_list1 = [int(y) for y in delete.split()]
removed_count = delete_of_number(my_list, my_list1)
print(removed_count)


#5
list = input("Введіть перший список чисел через пробіл : ")
list2 = input("Введіть другий список чисел через пробіл : ")
def elements_of_lists(list, list2):
    list3 = list + list2
    return list3
list = [int(j) for j in list.split()]
list2 = [int(g) for g in list2.split()]
result = elements_of_lists(list, list2)
print(result)


#6
def list_of_user(list_3, stepin):
    result_list = [num ** stepin for num in list_3]
    return result_list
list_4 = input("Введіть список чисел через пробіл : ")
my_list = [int(x) for x in list_4.split()]
stepin = int(input("Введіть степінь для підняття : "))
result = list_of_user(my_list, stepin)
print(result)
