def prime(num):
    if num<=1:
        return "Not Prime"
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return "Not Prime"
            break
    return "Prime"
num=int(input("Enter a number: "))
res=prime(num)
print(res)
