n = int( input() )

if n % 2 == 1:
    print( 0 )
    exit()

ans = 0
n = n // 2
while n > 0:
    n = n // 5
    ans += n
# k = 1
# while n > 10 ** k:
#     ans += ( n // ( 10 ** k ) + n // ( 5 ** k ) - n // ( 50 ** k ) )
#     k += 1

print( ans )