num=int(input("Enter a whole number: "))
temp=num
binary=""

while temp > 0:
    if(temp >= 1):
        binary =(str(temp%2)+binary)
        temp//=2        
print("the binary number for",num,"is",binary)
