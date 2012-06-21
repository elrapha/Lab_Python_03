num=1
isPrime=True
while True:
    i=2
    stop=int(sqrt(num))
    while i<=stop:
        if num%i==0:
            isPrime=False

"""
num=9
isPrime=True
stop=int(sqrt(num))+1
#print 'stop', stop
for i in range(2,stop):
    if num%i==0:
        isPrime=False
        break
if isPrime:
    print num, 'is prime'
    count=count+1
"""
