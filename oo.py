n = int (input ("Give me another number"))
sum = 0
temp = n
while temp > 0: 
    digits = temp % 10
    sum += digits ** 3
    temp // 10 

if n == temp:
    print (n,"It's a Armstrong Number!!!")
else:
    print (n, "Your number is very ordinary.")
