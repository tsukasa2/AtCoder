S = str( input() )

T = ""
for c in reversed( S ):
    if c == "6":
        T += "9"
    elif c == "9":
        T += "6"
    else:
        T += c

print( T )