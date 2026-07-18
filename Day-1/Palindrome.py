palin=int(input("Enter a number: "))
original=palin
rev=0
while palin!=0:
    digit=palin%10
    rev=digit
    palin/=10
if original==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
