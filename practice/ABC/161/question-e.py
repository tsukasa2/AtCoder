n, k, c = input().split()
n = int( n )
k = int( k )
c = int( c )
s = input()

def apply( k, c, s ):
    cnt = 0
    date = 0
    while date < len( s ):
        if s[ date ] == "x":
            date = date + 1
        elif s[ date ] == "o":
            cnt = cnt + 1
            date = date + c
            date = date + 1
        else:
            print("find invalid character: " + s[date])
            return False
    if cnt < k:
        return False
    else:
        return True
    
date = 0    
while date < len( s ):
    #print( s[:date] + s[date + 1:] )
    if not apply( k, c, s[:date] + s[date + 1:] ):
        print( date + 1 )
        date = date + c
        date = date + 1
    else:
        date = date + 1
