n = int( input() )
a = list( map( int, input().split() ) )

def biconv( x ):
    bi_x = []
    while len( bi_x ) <= 30:
        bi_x.append( x % 2 )
        x = x // 2
    return bi_x

def xor( x, y ):
    ans = []
    for i in range( len( x ) ):
        if x[ i ] + y[ i ] == 1:
            ans.append( 1 )
        else:
            ans.append( 0 )
    return ans

bi_a = []
for a_i in a:
    bi_a.append( biconv( a_i ) )

sum_x = [ 0 for _ in range( 31 ) ]
for a_i in bi_a:
    sum_x = xor( sum_x, a_i )

ans = []
for a_i in bi_a:
    x = xor( a_i, sum_x )
    ans_i = 0
    for i in range( 31 ):
        ans_i += ( 2 ** i ) * x[ i ]
    ans.append( ans_i )

print( " ".join( map( str, ans ) ) )