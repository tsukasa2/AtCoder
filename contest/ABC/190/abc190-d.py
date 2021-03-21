N = int( input() )

yakusuu = []
for k in range( 1, int( ( 2 * N ) ** 0.5 ) + 1 ):
    if 2 * N % k == 0:
        yakusuu.append( k )
        yakusuu.append( 2 * N // k )

ans = set()
for y in yakusuu:
    bunshi = ( 2 * N ) // y - y + 1 
    if bunshi % 2 == 0:
        ans.add( ( bunshi // 2, y ) )

# print( yakusuu )
# print( ans )
print( len( ans ) )