#handling zero division error
try:
  x = 10/0
except ZeroDivisionError:
  print("X cannot divided by zero")
finally:
  print("program ended")  
#multiple exceptions
try:
  num = int("abc")
  result = 10/0
except ValueError:
  print("X invalid number")
finally:
  print("done")
#catch any exception
try:
  f = open("data.txt")
except Exception as e:
  print("error:",e)
finally:
  print("file handling attempted")  
 
  