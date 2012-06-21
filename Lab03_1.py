#printing Prime numbers
from math import sqrt
count=0
num=1
print 'List of prime numbers'
print '.....................'
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
        count=count+1
        print num,
        if count%10==0:
            print '\n'
        
    if count==50:
        break
