package eightpuzzle;

import java.util.ArrayList;

import eightpuzzle.EightPuzzleBoard;

// import aima.core.environment.eightpuzzle.EightPuzzleBoard;
import aima.core.search.framework.evalfunc.HeuristicFunction;
import aima.core.util.datastructure.XYLocation;

/**
 * @author Ravi Mohan
 *
 */
public class NMaxSwapHeuristicFunction implements HeuristicFunction {

	public double h(Object state) {
		EightPuzzleBoard board = (EightPuzzleBoard) state;
    int numMisplaced = getNumberOfMisplacedTiles(board);
    int numCycloids = getNumberOfCycloids(board);
    double hValue = numMisplaced + numCycloids - 1;
		return hValue;
	}

	private int getNumberOfMisplacedTiles(EightPuzzleBoard board) {
		int numberOfMisplacedTiles = 0;
		if (!(board.getLocationOf(0).equals(new XYLocation(1, 1)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(1).equals(new XYLocation(0, 0)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(2).equals(new XYLocation(0, 1)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(3).equals(new XYLocation(0, 2)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(4).equals(new XYLocation(1, 2)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(5).equals(new XYLocation(2, 2)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(6).equals(new XYLocation(2, 1)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(7).equals(new XYLocation(2, 0)))) {
			numberOfMisplacedTiles++;
		}
		if (!(board.getLocationOf(8).equals(new XYLocation(1, 0)))) {
			numberOfMisplacedTiles++;
		}
		// Subtract the gap position from the # of misplaced tiles
		// as its not actually a tile (see issue 73).
		if (numberOfMisplacedTiles > 0) {
			numberOfMisplacedTiles--;
		}
		return numberOfMisplacedTiles;
	}

  private int getNumberOfCycloids(EightPuzzleBoard board) {
    int numberOfCycloids = 0;
    ArrayList counted_tiles = new ArrayList<Integer>();
    EightPuzzleBoard goal = new EightPuzzleGoalTest().goal;
    for (int i = 0; i < 9; i++) {
      int tile = board.getState()[i];
      if (!(counted_tiles.contains(tile)) && tile != goal.getState()[i]) {
        countCycloid(board, tile, counted_tiles, goal);
        numberOfCycloids++;
      }
    }
    return numberOfCycloids;
  }

  private void countCycloid(EightPuzzleBoard board, int tile,
        ArrayList counted_tiles, EightPuzzleBoard goal) {
    if (counted_tiles.contains(tile)) {
      return;
    } else {
      counted_tiles.add(tile);
      countCycloid(board, board.getValueAt(goal.getLocationOf(tile)),
            counted_tiles, goal);
    }
  }
}
