lists1=int(input("Enter keys and values for a dictionary: "))
dict1={}
for i in range(lists1):
    key=input("Enter a key value: ")
    value=int(input("Enter a value: "))
    dict1[key]=value
lists2=int(input("Enter keys and values for a dictionary2: "))
dict2={}
for j in range(lists2):
    keys=input("Enter keys: ")
    values=input("Enter values: ")
    dict2[keys]=values
res=dict1|dict2
print(res)
