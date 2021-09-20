T = int( input() )
cases = [ tuple( map( int, input().split() ) ) for _ in range( T ) ]

def solve( case ):
    L, M, N = case
    res = 0

    # 3 * 2 + 4 * 1
    if M // 2 > N:
        res += N
        M -= 2 * N
        N = 0
    else:
        res += M // 2
        N -= M // 2
        M = 0
    
    # 2 * 2 + 3 * 2:
    if L > M:
        res += M // 2
        L -= 2 * ( M // 2 )
        M -= 2 * ( M // 2 )
    else:
        res += L // 2
        M -= 2 * ( L // 2 )
        L -= 2 * ( L // 2 )
    
    # 2 * 1 + 4 * 2
    if L > N // 2:
        res += N // 2
        L -= N // 2
        N -= 2 * ( N // 2 )
    else:
        res += L
        N -= 2 * L
        L = 0
    
    # 2 * 3 + 4 * 1
    if L // 3 > N:
        res += N
        L -= 3 * N
        N = 0
    else:
        res += L // 3
        N -= L // 3
        L -= 3 * ( L // 3 )
    
    # 2 * 5
    res += L // 5

    return res

for case in cases:
    print( solve( case ) )