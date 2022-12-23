def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    
    return result

list2 = list()
my_list = list()

n = int(input())

for i in range(n):
    my_list += [[int(i) for i in input().split()]]
    
for i in range(len(my_list)):
    list1 = my_list[i]
    list2 = quick_merge(list1,list2)
    
list1 = []
print(*quick_merge(list1, list2))