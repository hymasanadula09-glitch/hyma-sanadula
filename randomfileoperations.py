#writing data to a file
f = open("data.txt","w")
f.write("hello,python!\n")
f.close()

#write lines()
f = open("data.txt","w")
f.writelines(["line1\n","line2\n","line3\n"])
f.close()

f = open("data.txt","r")
print(f.readline())
print(f.readline())
f.close()

#readlines
f=open("data.txt","r")
lines = f.readlines()
print(lines)
f.close()

#randomoperations
f = open("data.txt","r")
print(f.read(6))
print("pointer at",f.tell())
f.seek(0)
print(f.read(6))
f.close()





