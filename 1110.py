N = int(input())

def makeNew(n):
    tmp = n//10 + n % 10
    new = (n%10)*10 + tmp%10
    return new
    
new= makeNew(N)
cnt=1
    
while new!=N:
    cnt=cnt+1
    new = makeNew(new)
    
print(cnt)
