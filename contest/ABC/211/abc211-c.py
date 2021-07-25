S = str( input().split() )
MOD = 10 ** 9 + 7

from collections import Counter
count = Counter()

for c in reversed( S ):
    if c == "i":
        count[ c ] += 1
    elif c == "a":
        count[ c ] += count[ "i" ]
    elif c == "d":
        count[ c ] += count[ "a" ]
    elif c == "u":
        count[ c ] += count[ "d" ]
    elif c == "k":
        count[ c ] += count[ "u" ]
    elif c == "o":
        count[ c ] += count[ "k" ]
    elif c == "h":
        count[ c ] += count[ "o" ]
    elif c == "c":
        count[ c ] += count[ "h" ]
    
    count[ c ] %= MOD

print( count[ "c" ] )