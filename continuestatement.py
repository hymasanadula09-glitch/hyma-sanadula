for number in range(1,7):
  if number == 3:
     print("skippin the number 3")
     continue
  print("number", number)

#question
list1= [1,2,3,4,5,-9,-8,-7,-6]
for num in list1:
  if num<0:
    print("skipping the negative numbers")
    continue
  print("number:",num)

list2= [2,3,6,8,9,15]
for num in list2:
  if num%3==0:
    print("skipping the multiples of 3")
    continue
  print("number",num)