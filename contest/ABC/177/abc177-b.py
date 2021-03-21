s = str( input() )
t = str( input() )

def compare( s, t ):
    count = 0
    for i in range( len( s ) ):
        if s[ i ] != t[ i ]:
            count += 1
    return count

ans = 10 ** 10
for i in range( len( s ) - len( t ) + 1 ):
    ans_i = compare( s[ i : i + len( t ) ], t )
    if ans_i < ans or i == 0:
        ans = ans_i

print( ans )