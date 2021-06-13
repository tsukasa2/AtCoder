N = int( input() )
A = list( map( int, input().split() ) )

if N == 1:
    print( A[ 0 ] / 2 )
    exit()

A.sort()
sum_A = sum( A )
m = -N

L = 0
R = A[ 0 ] / 2
C = sum_A - A[ 0 ]
ans = sum_A
for i, a in enumerate( A[ 1 : ] ):
    L = R
    R = a / 2
    m += 2
    if m < 0:
        ans_i = m * R + C
    else:
        ans_i = m * L + C
    
    # print( i, a, L, R, m, C, ans_i )
    ans = min( ans, ans_i )
    C -= a

print( ans / N )