###############################################################
####	Automandala Class
####	Ryan McArdle
####	Original: Dec.  2018
####	Refresh: Dec.  2020
####	
####	A class intended for the exploration of different
####	cellular automata rules and initial seeds for
####	generating mandala patters.
####
####	Definitions for each of the seeds can be found in
####	Seeds.py, and the different rule sets can be found
####	in Rules.py.
####
###############################################################
import matplotlib
from matplotlib.animation import PillowWriter
import numpy as np
import matplotlib.pyplot as plt
import Seeds, Util
import itertools
import os

class Mandala(object):

    def __init__(self, N=201):
        """
        Initializes parameters which define grid size etc.

        :param height: the number of cells along the vertical
        :param width: the number of cells along the horizontal
        """

        # height = width if height is None else height

        self.width = N
        self.height = N

        # Sets grid
        self.grid = np.zeros((N,N)) ## Ensure ordering correct here
        self.oldgrid = self.grid.copy()
        # self.newgrid = self.grid.copy()
        self.center = (int(N // 2)-1,int(N // 2)-1)

        # Sets values
        self.off = 0
        self.on = 1
        self.vals = (0,1)
        return

    def update(self,frame,period,rules,*args,**kwargs):
        
        # print(frame)
        if frame == 2*period-1:
            print('stop')
            # self.ani.event_source.stop()
            plt.close()
        self.newgrid = self.grid.copy()
       

        for x,y in itertools.product(range(self.width),range(self.height)):
            if frame <= 2 * period:
                adj = Util.adj8(self.grid,self.width,x,y)
                if self.grid[x,y] == self.on:
                    if (adj < rules[0]) or (adj > rules[1]):
                        self.newgrid[x,y] = 0
                else:
                    if adj == 1 and frame == 0:
                        self.newgrid[x,y] = self.on
                    if adj >= rules[2]:
                        self.newgrid[x,y] = self.on
           
            ## Optional additional 'phases' to the automata, to
            #  express different behaviors over time. Requires
            #  updating to the current version.
            #
            # elif frame>2 * period:
            #     adj = Util.adj4(self.grid,self.width,x,y)
            #     oldadj = Util.oldadj4(self.oldgrid,self.width,x,y)
            #     if self.grid[x,y] == self.on and self.oldgrid[x,y] == self.on:
            #         if adj == 1:
            #             if oldadj != 1:
            #                 self.newgrid[x,y] = np.random.choice(self.vals, p=[0.1, 0.9])
            #         if adj == 2:
            #             self.newgrid[x,y] = np.random.choice(self.vals, p=[0.995, 0.005])
            #         if adj == 3:
            #             drop = (1 / ((frame - period) * 50))
            #             self.newgrid[x,y] = np.random.choice(self.vals, p=[1 - drop, drop])
            #         if adj == 4:
            #             self.newgrid[x,y] = self.on
            #     elif self.grid[x,y] == self.on and self.oldgrid[x,y] == self.on:
            #         if adj == 1:
            #             self.newgrid[x,y] = np.random.choice(self.vals, p=[0.99,0.01])
            #         if adj == 2:
            #             self.newgrid[x,y] = np.random.choice(self.vals, p=[0.995, 0.005])
            #         if adj >= 3:
            #             self.newgrid[x,y] = 1
            #     elif self.grid[x,y] == self.on and self.oldgrid[x,y] == self.on:
            #         self.newgrid[x,y] == self.on
            #     elif adj >= 1:
            #         self.newgrid[x,y] = np.random.choice(self.vals, p=[0.001,0.999])
            # elif frame>=period*3:
            #     adj = Util.adj8(self.grid,self.width,x,y)
            #     if self.grid[x,y] == self.on:
            #         if (adj < 2) or (adj > 3):
            #             self.newgrid[x,y] = np.random.choice(self.vals, p=[0.2, 0.8])
            #     else:
            #         if adj == 3:
            #             self.newgrid[x,y] = np.random.choice(self.vals, p=[0.8, 0.2])

        self.mat.set_data(self.grid)
        self.oldgrid = self.grid.copy()
        self.grid = self.newgrid
        return[self.mat]
        
    def animate(self,seed,rule):
        period = 100
        fig, self.ax = plt.subplots()
        self.mat = self.ax.matshow(self.grid)
        self.mat.set_cmap('gray')
        self.ani = matplotlib.animation.FuncAnimation(fig,self.update,init_func=seed,fargs=(period,rule),frames=3*period,interval=1,blit=False,repeat=False)
        if not os.path.exists('./automatagifs/'):
            os.mkdir('./automatagifs')
        self.ani.save(f'./automatagifs/{rule}.gif', writer=PillowWriter(fps=60))


def main():
    print('test')
    seed = 'center9'
    rules = [[a,b,c] for a in range(1,8) for b in range(a,8) for c in range(a,b)]
    # rules = [[2,4,2,2],[3,4,3,3]]
    for rule in rules: 
        mandala = Mandala(N=201)
        seed= Seeds.seed9(Seeds.cent(),mandala)
        print(rule)
        mandala.animate(seed,rule)


if __name__=='__main__':
    main()

