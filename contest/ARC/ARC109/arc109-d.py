T = int( input() )
case = []
for _ in range( T ):
    ax, ay, bx, by, cx, cy = list( map( int, input().split() ) )
    case.append( ( ( ax, ay ), ( bx, by ), ( cx, cy ) ) )

def solve( abc ):
    ( ax, ay ), ( bx, by ), ( cx, cy ) = abc
    goal_x = min( [ ax, bx, cx ] )
    goal_y = min( [ ay, by, cy ] )
    if goal_x == 0 and goal_y == 0:
        if ( ax, ay ) == ( 1, 1 ) or ( bx, by ) == ( 1, 1 ) or ( cx, cy ) == ( 1, 1 ):
            return 1
        else:
            return 0
    else:
        if goal_x < 0 or goal_y < 0:
            return 2 * max( abs( goal_x ), abs( goal_y ) )
        else:
            return 2 * max( abs( goal_x ), abs( goal_y ) ) + 1


for c in case:
    print( solve( c ) )