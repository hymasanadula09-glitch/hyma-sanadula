#higher order function
def square(x):
  return x*x
numbers = [2,6,25,28]
squared = list(map(square,numbers))
print(squared)

#filters
def is_even(x):
  return x % 2 == 0
numbers =[1,2,3,4,5,6]
even_numbers = list(filter(is_even,numbers))
print(even_numbers)

#reduce
from functools import reduce
def add(x,y):
  return x+y
numbers = [1,2,3,4,5,6]
sum_num = reduce(add,numbers)
print(sum_num)


















































