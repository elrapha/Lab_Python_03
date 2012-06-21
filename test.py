from math import sqrt
count=0
num=1
while True:
    num=num+1
    isPrime=True
    stop=int(sqrt(num))+1
    for i in range(2,stop):
        if num%i==0:
            isPrime=False
            #print i, 'divided',num
            break
    if isPrime:
        print num, 'is prime'
        count=count+1
    if count==12:
        break
