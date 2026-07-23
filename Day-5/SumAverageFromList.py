num=list(map(int,input("Enter numbers: ").split()))
sum=0
count=0
for i in num:
    sum+=i
    count+=1
print("Sum: ",sum)
print("Average: ",(sum/count))
