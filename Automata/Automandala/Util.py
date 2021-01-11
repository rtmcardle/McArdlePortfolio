###############################################################
####	Automandala Utility Functions
####	Ryan McArdle
####	Original: Dec.  2018
####	Refresh: Dec.  2020
####	
####	Fuctions defined to count the number of active 
####    neighbors for a give cell for the Automandala
####    class.
####
###############################################################


def adj4(grid,N,x,y):
    tot=(grid[(x-1)%N,y]+
        grid[x,(y-1)%N]+
        grid[x,(y+1)%N]+
        grid[(x+1)%N,y])/1
    return tot


def adj8(grid,N,x,y):
    tot=(grid[(x-1)%N,(y-1)%N]+grid[(x-1)%N,y]+
        grid[(x-1)%N,(y+1)%N]+grid[x,(y-1)%N]+
        grid[x,(y+1)%N]+grid[(x+1)%N,(y-1)%N]+
        grid[(x+1)%N,y]+grid[(x+1)%N,(y+1)%N])/1
    return tot


def oldadj4(oldgrid,N,x,y):
    tot=(oldgrid[(x-1)%N,y]+
        oldgrid[x,(y-1)%N]+
        oldgrid[x,(y+1)%N]+
        oldgrid[(x+1)%N,y])/1
    return tot