'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10.

In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
'''
import math

def FindingCombinations(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)


def CombinatroicSelection(a,b,n):
    #a (1) starting, b (100) ending and n is limit(1000000)
    count = 0
    for i in range(a,b+1):
        for r in range(int(i/2)+1):
            if FindingCombinations(i,r) > n:
                count += 2
                if i % 2 == 0 and r == int(i/2):
                    count -= 1
    return count

final = CombinatroicSelection(1,100,1000000)
print(final)