Ryan McArdle


Each problem is contained within its own subfolder. They contain the main java file which is to be compiled and run (e.g. WaterAndJugs.java, EightPuzzle.java, etc.) and subfolders which contain my written supporting classes (heuristics, action definitions, etc.) and an aima subfolder to help avoid any complications due to classpath issues. 

Solution paths and sequences of actions are all output to files titled "solution_output.txt," which contain actions taken, intermediate steps, and instrumentation information (path costs, nodes expanded, etc.). 


2. Eight Puzzle

Nilsson's Distance is the only heuristic which did not find an optimal path, return a path of cost 24 as opposed to 20. However, it did expand the fewest nodes at 388. 
Manhattan distance returned an optimal path with 420 expanded nodes, while other optimal heuristics required 1790 and 66237 nodes to find the path.


3. Dating Game

My defined heuristic for this problem penalizes states for same-gender pairings of contestants (similar to Nilsson's heuristic) and for the gap being away from its final state. As Nilsson's was not admissible, I believe this is not either. It does find optimal soultions for this initial state and others tested. 

IDLS and A* (with my heuristic) both found paths of cost 6 (optimal) for this initial state. IDLS required 66 nodes expanded while A* required 93. This seems to indicate that my heuristic is lacking and could be better formulated. 


4. Grid World

I did not complete this problem. There are two included main java files, 'GridWorld.java' and 'GridWorldIDAStarSearch.java'. 
'GridWorld.java' solves the enviroment using standard A* search with a Euclidean SLD Heuristic, to indicate that the environment has been formulated properly. 
'GridWorldIDAStarSearch.java' contains most of the formulation for an IDA* process. The findNode() method in the DepthLimitAStarSearch method is incomplete, as I could not find an appropriate example as to the appropriate structure of this method. The project will compile, but it will not complete running due to this incomplete method. 