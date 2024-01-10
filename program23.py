lower = int(input("Enter the lower bound:"))
upper = int(input("Enter the upper bound:"))
result= [num for num in range(lower,upper+1) if all
(int(digit)%2==0 for digit in str(num))and int( num ** 0.5)**
2==num]
print(result)
