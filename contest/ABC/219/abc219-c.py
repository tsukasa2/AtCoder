X = str( input() )
N = int( input() )
S = [ str( input() ) for _ in range( N ) ]

reversed_X = {}
for i, c in enumerate( X ):
    reversed_X[ c ] = i

def comp( a, b ):
    r = min( len( a ), len( b ) )
    for i in range( r ):
        if reversed_X[ a[ i ] ] < reversed_X[ b[ i ] ]:
            return True
        elif reversed_X[ a[ i ] ] > reversed_X[ b[ i ] ]:
            return False
    
    if len( a ) < len( b ):
        return True
    elif len( a ) > len( b ):
        return False
    else:
        return None

def quick_sort(arr):
    left = []
    right = []
    if len( arr ) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[ 0 ]
    ref_count = 0

    for ele in arr:
        if comp( ele, ref ) == True:
            left.append(ele)
        elif comp( ele, ref ) == False:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

for s in quick_sort( S ):
    print( s )