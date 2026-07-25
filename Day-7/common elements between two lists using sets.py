n1=list(map(int,input("Enter a list1: ").split()))
n2=list(map(int,input("Enter a list2: ").split()))
s1=set(n1)
s2=set(n2)
res=s1&s2
print(res)
