n = int(input("Enter a number whose count-sum-product required : "))

count = 0
sum_digit = 0
product = 1

if n==0:
    count = 1
    sum_digit = 0
    product = 0

else:
    while n>0:

        digit = n%10
        count +=1
        sum_digit += digit
        product *= digit
        n = n//10

print("Count of the value is : ", count)
print("Sum of the digit is : ", sum_digit)
print("Product of the number is : ", product)
    

