n, k = map( int, input().split() )
p = list( map( int, input().split() ) )
c = list( map( int, input().split() ) )

loop = [ -1 for _ in range( n ) ]
loop_score = [ 0 for _ in range( n ) ]
loop_length = [ 0 for _ in range( n ) ]
for i in range( n ):
    if loop[ i ] == -1:
        score = 0
        length = 1
        loop[ i ] = i
        j = p[ i ] - 1
        while j != i:
            loop[ j ] = i
            score += c[ p[ j ] - 1 ]
            j = p[ j ] - 1
            length += 1
        loop_score[ i ] = score + c[ p[ i ] - 1 ]
        loop_length[ i ] = length

# print( loop, loop_score, loop_length)

def solve( start ):
    current = p[ start ] - 1
    l = loop_length[ loop[ start ] ]
    score = loop_score[ loop[ start ] ]
    if l >= k:
        current = start
        max_score = 0
        cur_score = 0
        for i in range( k ):
            current = p[ current ] - 1
            cur_score += c[ current ]
            if max_score < cur_score or i == 0:
                max_score = cur_score
        return max_score
    else:
        if score > 0:
            score = score * ( k // l )
            current = start
            max_score = 0
            cur_score = 0
            for _ in range( k % l ):
                current = p[ current ] - 1
                cur_score += c[ current ]
                if max_score < cur_score:
                    max_score = cur_score
            return max_score + score
        else:
            score = 0
            current = start
            max_score = 0
            cur_score = 0
            for i in range( k % l ):
                current = p[ current ] - 1
                cur_score += c[ current ]
                if max_score < cur_score or i == 0:
                    max_score = cur_score
            return max_score

best_score = - ( 10 ** 10 )
for i in range( n ):
    now_score = solve( i )
    if best_score < now_score:
        best_score = now_score
print( best_score )
