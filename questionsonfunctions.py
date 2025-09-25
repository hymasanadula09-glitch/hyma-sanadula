#q1
def mul_numbers(a,b):
    print("mul of a n b=",a*b)
    return
a = int(input("enter a number:"))
b = int(input("enter a number:"))
mul_numbers(a,b)
#q2
def even_or_odd(num):
    if num%2==0:
        return("even")
    else:
        return("odd")
num = int(input("enter the number:"))
print("the num is,",even_or_odd(num)) 
#q3
def fact(num):
    fact=1
    for i in range(1,1+num):
        fact*=i
    return fact
num = int(input("enter the number:"))
print("the factorial of",num,"is",fact(num))
#qn 4 
def largest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif  b>=a and b>=c:
        return c
    else:
        return c 
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
print("the largest number is,",largest_of_three(a,b,c))
#q5
def reverse_str(str):
    return str[::-1]
txt = input("enter a text:")
print("reverse string is,", reverse_str(txt))
#q6
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
txt = input("enter a text:")
print("vowels:",count_vowels(txt))
