num=list(map(int,input("Enter numbers: ").split()))
s=set(num)
print(list(s))

res=list(dict.fromkeys(num))
print(res)
