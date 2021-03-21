import math

k = int( input() )
out_sum = 0

# a==b and b==c
for a in range(1, k+1):
    out_sum += a

# a==b and b!=c
for a in range(2, k+1):
    for b in range(1, a):
        out_sum += 6 * math.gcd(a,b)
# a,b,cから等しい2つを選んだあと残りがそれらより大きいor小さいだから係数は3*2=6

# a!=b and b!=c
for a in range(3, k+1):
    for b in range(2, a):
        for c in range(1, b):
            out_sum += 6 * math.gcd( a, math.gcd(b,c) )

print( out_sum )