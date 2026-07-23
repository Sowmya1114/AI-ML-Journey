num=list(map(int,input("Enter numbers: ").split()))
max_num=num[0]
max_num2=0
for i in num:
    if i>max_num:
        max_num2=max_num
        max_num=i
    elif i>max_num2 and i!=max_num:
        max_num2=i
print(max_num2)
