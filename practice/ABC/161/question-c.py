n, k = input().split()
n = int( n )
k = int( k )

print( min( n % k, k - ( n % k ) ) )