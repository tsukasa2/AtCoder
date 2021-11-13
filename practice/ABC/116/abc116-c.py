N = int( input() )
h = list( map( int, input().split() ) )

ans = 0
for j in reversed( range( 1, 101 ) ):
    flag = False
    for i in range( N ):
        if flag == True and h[ i ] < j:
            ans += 1
        
        if h[ i ] >= j:
            flag = True
        else:
            flag = False
    
    if flag == True:
        ans += 1

print( ans )