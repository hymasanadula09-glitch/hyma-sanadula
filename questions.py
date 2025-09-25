#qn 1 
import array  
numbers = array.array('i',[2,4,6,8])
print(numbers[0])
print(numbers[-1])

#QN 3
import array 
num2=  array.array('i', [2,4,6,8,10,12,14])
print(num2[-2:])
print(num2[:-5])

#qn 5
nums = array.array('i',[5,10,15,20,25,30])
slicing = nums[0:4]
total = 0 
for i in slicing:
    total += i
print("sum =",total)    

#6th qn
num3 = array.array('i',[1,3,5,7,9])
print(num3[::-1])

#qn 2 
num4 = array.array('i',[1,2,3,4,5,])
print(num4[2:5])

#qn 4
num5 = array.array('i',[0,1,2,3,4,5])
print(num5[::2])