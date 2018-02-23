from time import time


dizi[]
dizi1[]
dizi2[]
def fibo(n):
    if n<2:
        return n
    return fibo(n-1) + fibo(n-2)

def loop(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a



for i in range (40):
    start = time()
    fibo(i)
    dizi.append(time()-start)
    start1 = time()
    loop(i)
    dizi1.append(time()-start1)
    dizi2.append(i)

