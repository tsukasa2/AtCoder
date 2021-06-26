N, K = map( int, input().split() )
S = str( input() )

def judge( N, K, S, M ):
    # 1を連続でMケタ並べることができるか
    if M > N:
        return False
    elif M == 0:
        return True
    else:
        zero_groups = 0
        prev = "1"
        for c in S[ : M ]:
            if prev == "1" and c == "0":
                zero_groups += 1
            
            prev = c
        
        if zero_groups <= K:
            return True
        
        for i in range( M, N ):
            if S[ i ] == "0" and S[ i - 1 ] == "1":
                zero_groups += 1
            
            if S[ i - M ] == "0" and S[ i - M + 1 ] == "1":
                zero_groups -= 1
            
            if zero_groups <= K:
                return True
        
        else:
            return False

l, r = 0, 10 ** 5 + 100
while r - l > 1:
    m = ( l + r ) // 2
    # print( m, judge( N, K, S, m ) )
    if judge( N, K, S, m ):
        l = m
    else:
        r = m

print( l )