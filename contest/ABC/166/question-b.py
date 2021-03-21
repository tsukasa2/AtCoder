n, k = input().split()

sunuke = [ 0 ] * int(n)

for i in range( int( k ) ):
    d = int( input() )
    a = input().split()
    for a_i in a:
        sunuke[ int( a_i ) - 1 ] = 1

cnt = 0
for sunuke_i in sunuke:
    if sunuke_i == 0:
        cnt = cnt + 1

print( cnt )