k, n = input().split()
a = input().split()

max_interval = 0
for i in range( int( n ) - 1 ):
    interval = int( a[i+1] ) - int( a[i] )
    if max_interval < interval:
        max_interval = interval

interval = int( k ) - int( a[-1] ) + int( a[0] )
if max_interval < interval:
        max_interval = interval

print( int( k ) - max_interval )