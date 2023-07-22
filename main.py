list_num = [int(i) for i in input().split()]
if len(list_num) == 1:
    print(list_num[0])
elif len(list_num) == 2:
    print(list_num[1]*2, list_num[0]*2)
else:
    for i in range(len(list_num)):
        if i < len(list_num) - 1:
            print(list_num[i - 1] + list_num[i + 1], end=" ")
        else:
            print(list_num[0] + list_num[i - 1])