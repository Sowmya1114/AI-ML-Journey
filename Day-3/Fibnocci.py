num=int(input("Enter a number: "))
f1,f2=0,1
f3=0
if num==1:
    print(f1)
elif num==2:
    print(f2)
else:
    for i in range(3,num+1):
        f3=f1+f2
        f1=f2
        f2=f3
print(f3)
