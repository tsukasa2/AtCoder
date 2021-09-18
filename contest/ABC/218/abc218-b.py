P = list( map( int, input().split() ) )

abc = "abcdefghijklmnopqrstuvwxyz"
ans = ""
for p in P:
    ans += abc[ p - 1 ]

print( ans )