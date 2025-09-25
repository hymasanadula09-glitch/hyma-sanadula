num=int(input('enter the number:'))
if(num%3==0 and num%5==0):
    print('the given ',num,' is divisible by 3 and 5')
else:
    print('the given ',num,' is not divisible by 3 and 5')

num=int(input('enter the number:'))
if(num%3==0 or num%5==0):
    print('the given ',num,' is divisible by 3 or 5')
else:
    print('the given is ',num,' is not divisible by 3 or 5')
