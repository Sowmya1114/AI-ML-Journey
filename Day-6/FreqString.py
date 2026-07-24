name=input("Enter a name: ")
freq={}
for char in name:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
