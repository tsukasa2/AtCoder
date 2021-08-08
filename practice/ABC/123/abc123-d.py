X, Y, Z, K = map( int, input().split() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )
C = list( map( int, input().split() ) )

A.sort( reverse = True )
B.sort( reverse = True )
C.sort( reverse = True )

def check( x ):
    # 美味しさがx以上になる組み合わせがK個以上あるか
    count = 0
    for a in A:
        for b in B:
            for c in C:
                if a + b + c < x:
                    break
                else:
                    count += 1
                    if count >= K:
                        return True
    
    return False

l = 0
r = 3 * 10 ** 10 + 100
while r - l > 1:
    m = ( l + r ) // 2
    if check( m ):
        l = m
    else:
        r = m

Kth_ans = l

ans = []
for a in A:
    for b in B:
        for c in C:
            if a + b + c <= Kth_ans:
                break
            else:
                ans.append( a + b + c )

while len( ans ) < K:
    ans.append( Kth_ans )

ans.sort( reverse = True )
print( *ans, sep = "\n" )