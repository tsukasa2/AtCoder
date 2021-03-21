from math import factorial

n, k = input().split()
n = int( n )
k = int( k )
out = 0

for i in range(k, n+2):
    r = factorial( n+1 ) / ( factorial( k ) * factorial( n+1-k ) )
    for j in 