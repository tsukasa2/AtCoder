N = int( input() )
a = list( map( int, input().split() ) )
b = list( map( int, input().split() ) )

b.sort()

ans = []
for b_i in b:
    x = a[ 0 ] ^ b_i
    c = [ a_i ^ x for a_i in a ]
    c.sort()
    if b == c:
        ans.append( x )

ans = list( set( ans ) )
ans.sort()
print( len( ans ) )
if ans:
    print( "\n".join( map( str, ans ) ) )