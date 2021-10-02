N = int( input() )
A = list( map( int, input().split() ) )
X = int( input() )

sum_A = sum( A )
ans = ( X // sum_A ) * N
sum_a = 0
X %= sum_A
for a in A:
    # print( sum_a, a, ans )
    if sum_a + a > X:
        ans += 1
        break
    else:
        sum_a += a
        ans += 1
    
print( ans )