Ryan McArdle 
Assignment 3

The main code file is Blobs.java. This class will call 3 methods; startBlobsRandomVsRandom(), startBlobsRandomVsMinimaxCutoff(), startBlobsMinimaxCutoffVsIDAlphaBeta(). 


Each of these methods will run 5 matches with the relevant agent match-ups. The MinimaxCutoff algorithm always plays as X. Each produces a corresponding output file, '*_results.txt,' with the results of the match-ups. There are 3 '*_results_submission.txt' files which already contain output results.


The Minimax algorithm is set to seaerch to a depth of 3-ply for the sake of moderate quickness of calculation, particularly in the middle-game. The Alpha-Beta algorithm is set with a cut-off calculation time of 15 seconds for similar reasons, keeping it somewhat on par with the Minimax algorithm. 


The utility function (defined in BlobsState.java, ln 112) values each piece on the board more than the opponent as 1 point, with space where a place could be placed as slightly less that 1/2 a point. Given the opportunity to place a piece or move a piece, the move should be selected only if it provides 3 or more potential placements. Enemey potential placement spaces are also worth negative the same value. 