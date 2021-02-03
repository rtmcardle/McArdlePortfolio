# Search and Logic
This is a collection of Java code which utilizes the [codebase][1] associated with Russel and Norvig's [Artificial Intelligence: A Modern Approach][2].

## Directories

### [Java Basics](JavaBasics/)
A collection of custom written functions intended to establish familiarity with Java. The functions perform various vector and set operations on ArrayLists, such as union, inner product, recursively counting the number of embedded lists, and creating the powerset. 

### [Logic Program](LogicProgram/)
A program which utilizes AIMA first-order logic inference procedures in order to satisfy queries regarding relationships for an established family tree. The individuals and relevant relationships are defined in the [Domain Factory](family/DomainFactory.java) file. Logical definitions of complex familial relationships are defined in the [Knowledge Base](family/KnowledgeBaseFactory.java) along with givens and the fundamental Parent() relationship. This information is used to satisfy queries such as Uncle(x,y), which would return an x and y for which the Uncle() relationships holds.

### [MiniMax](MiniMax/)
An application of the MiniMax algorithm both with and without alpha/beta pruning. The algorithm is used to play the 'Blobs' game, a variation on Go in which the player desires the most stones on the board, stones must be placed adjacent to your own stones already in play, and the player may choose to move one of their pieces rather than place another. Definitiibs fir the board, pieces, actions, and algorithms are contained in the [blobs](MiniMax/blobs/) directory. The '*_results_submissions.txt' files contain the results of five match-ups for various combinations of random, MiniMax, and iterative deeping alpha beta algorithms. 

### [Search Problems](SearchProblems/)
Contained here are solvers for various search problems utilizing primarily A* and iterative deepening depth limited searches while exploring different heuristics for the given problems. Each application will output the solution path as well as diagnostic information about the searches, such as number of nodes expanded and past cost for the solution. 



[1]: https://github.com/aimacode/aima-java
[2]: https://www.pearson.com/us/higher-education/program/Russell-Artificial-Intelligence-A-Modern-Approach-4th-Edition/PGM1263338.html
