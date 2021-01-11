import blobs.BlobsGame;
import blobs.BlobsState;
import blobs.BlobsAction;
import blobs.BlobsFunctionFactory;
import blobs.BlobsMinimaxCutoffSearch;
import blobs.BlobsRandomSearch;

import java.io.PrintStream;
import java.io.IOException;


import aima.core.search.adversarial.AdversarialSearch;
import aima.core.search.adversarial.AlphaBetaSearch;
import aima.core.search.adversarial.MinimaxSearch;
import aima.core.util.datastructure.XYLocation;
import aima.core.search.adversarial.IterativeDeepeningAlphaBetaSearch;

/**
 * Applies Minimax search and alpha-beta pruning to find optimal moves for the
 * Blobs game.
 *
 */

public class Blobs {
	public static void main(String[] args) {
		System.out.println("BLOBS");
		System.out.println("");

		startBlobsRandomVsRandom();
		startBlobsRandomVsMinimaxCutoff();
		startBlobsMinimaxCutoffVsIDAlphaBeta();
	}

	private static void startBlobsRandomVsRandom() {
		try {
			PrintStream outputFile = new PrintStream("./random_random_results.txt");

			for (int i = 1; i<=5; i++){
				System.out.println("BLOBS RANDOM VS RANDOM CUTOFF GAME\n");
				BlobsGame game = new BlobsGame();
				BlobsState currState = game.getInitialState();

				// Creates agents
				AdversarialSearch<BlobsState, BlobsAction> xRand = BlobsRandomSearch.createFor(game);
				AdversarialSearch<BlobsState, BlobsAction> yRand = BlobsRandomSearch.createFor(game);

				// Plays game
				while (!(game.isTerminal(currState))) {
					System.out.println(game.getPlayer(currState) + " playing ... ");
					BlobsAction action = null;
					if (game.getPlayer(currState) == "X") {
						action = xRand.makeDecision(currState);
					} else {
						action = yRand.makeDecision(currState);
					}
					currState = game.getResult(currState, action);
					System.out.println(currState.toString());
				}

				// Outputs results
				outputFile.append("Game "+String.valueOf(i)+" Result: \r\n");
				outputFile.append(game.getWinner(currState)+"\r\n");
				outputFile.append(currState.toString()+"\r\n\r\n");
				System.out.println("BLOBS MINIMAX VS RANDOM GAME DONE");
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void startBlobsRandomVsMinimaxCutoff() {
		try {
			PrintStream outputFile = new PrintStream("./random_minimax_results.txt");

			for (int i = 1; i<=5; i++){
				System.out.println("BLOBS RANDOM VS MINIMAX CUTOFF GAME\n");
				int cutoff = 3;
				BlobsGame game = new BlobsGame();
				BlobsState currState = game.getInitialState();

				// Creates agents
				AdversarialSearch<BlobsState, BlobsAction> xMinimax = BlobsMinimaxCutoffSearch.createFor(game,cutoff);
				AdversarialSearch<BlobsState, BlobsAction> yRand = BlobsRandomSearch.createFor(game);

				// Plays game
				while (!(game.isTerminal(currState))) {
					System.out.println(game.getPlayer(currState) + " playing ... ");
					BlobsAction action = null;
					if (game.getPlayer(currState) == "X") {
						action = xMinimax.makeDecision(currState);
					} else {
						action = yRand.makeDecision(currState);
					}
					// System.out.println(action);
					currState = game.getResult(currState, action);
					System.out.println(currState.toString());
				}

				// Outputs result
				outputFile.append("Game "+String.valueOf(i)+" Result: \r\n");
				outputFile.append(game.getWinner(currState)+"\r\n");
				outputFile.append(currState.toString()+"\r\n\r\n");
				System.out.println("BLOBS MINIMAX VS RANDOM GAME DONE");
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void startBlobsMinimaxCutoffVsIDAlphaBeta() {
		try {
			PrintStream outputFile = new PrintStream("./minimax_abpruning_results.txt");

			for (int i = 1; i<=5; i++){
				System.out.println("BLOBS MINIMAX CUTOFF VS ID ALPHA-BETA GAME\n");
				int cutoff = 3;
				BlobsGame game = new BlobsGame();
				BlobsState currState = game.getInitialState();

				double utilMax = Double.POSITIVE_INFINITY;
				double utilMin = Double.NEGATIVE_INFINITY;
				int time = 15;

				// Creates agents
				AdversarialSearch<BlobsState, BlobsAction> xMinimax = BlobsMinimaxCutoffSearch.createFor(game,cutoff);
				AdversarialSearch<BlobsState, BlobsAction> yIDABPrune = IterativeDeepeningAlphaBetaSearch.createFor(game,utilMin,utilMax,time);

				// Plays game
				while (!(game.isTerminal(currState))) {
					System.out.println(game.getPlayer(currState) + " playing ... ");
					BlobsAction action = null;
					if (game.getPlayer(currState) == "X") {
						action = xMinimax.makeDecision(currState);
					} else {
						action = yIDABPrune.makeDecision(currState);
					}
					// System.out.println(action);
					// System.out.println()
					currState = game.getResult(currState, action);
					System.out.println(currState.toString());
				}

				// Outputs results
				outputFile.append("Game "+String.valueOf(i)+" Result: \r\n");
				outputFile.append(game.getWinner(currState)+"\r\n");
				outputFile.append(currState.toString()+"\r\n\r\n");
				System.out.println("BLOBS MINIMAX CUTOFF VS ID ALPHA-BETA GAME DONE");
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
