N, M = map( int, input().split() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

R = 10000
A += [ 0 for _ in range( R ) ]
B += [ 0 for _ in range( R ) ]

i = 0
j = 0
A_dic = {}
B_dic = {}
d = 0
ans = 0
while i <= N or j <= M:
    if A[ i ] not in A_dic:
        A_dic[ A[ i ] ] = i
    if B[ j ] not in B_dic:
        B_dic[ B[ j ] ] = j

    if A[ i ] in B_dic:
        j = B_dic[ A[ i ] ]
        A_dic = {}
        B_dic = {}
        ans += d
        d = -1
    elif B[ j ] in A_dic:
        i = A_dic[ B[ j ] ]
        A_dic = {}
        B_dic = {}
        ans += d
        d = -1
    
    i += 1
    j += 1
    d += 1

print( ans )