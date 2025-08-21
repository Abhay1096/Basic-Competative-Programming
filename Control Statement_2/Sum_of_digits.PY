num = int(input("Enter the number : "))
digit=0
sum=0
for i in range(num):
    if(num>0):
        digit= num%10
        sum = sum+digit
        num = num//10
print("Sum : ",sum)