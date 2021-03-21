n = int( input() )
s = str( input() )

s = s + "x"
ABC_count = 0
for i in range( n + 1 - 3 ):
    if s[i:i+3] == "ABC":
        ABC_count += 1

print( ABC_count )