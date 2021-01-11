package eightpuzzle;

import eightpuzzle.EightPuzzleBoard;

// import aima.core.environment.eightpuzzle.EightPuzzleBoard;
import aima.core.search.framework.evalfunc.HeuristicFunction;
import aima.core.util.datastructure.XYLocation;

/**
 *
 */
public class NilssonsDistanceHeuristicFunction implements HeuristicFunction {

	public double h(Object state) {
		EightPuzzleBoard board = (EightPuzzleBoard) state;
		int retVal = 0;
		for (int i = 1; i < 9; i++) {
			XYLocation loc = board.getLocationOf(i);
			retVal += evaluateManhattanDistanceOf(i, loc);
		}

    retVal += evaluateSequenceScore(board);

		return retVal;

	}

	public int evaluateManhattanDistanceOf(int i, XYLocation loc) {
		int retVal = -1;
		int xpos = loc.getXCoOrdinate();
		int ypos = loc.getYCoOrdinate();
		switch (i) {

		case 1:
			retVal = Math.abs(xpos - 0) + Math.abs(ypos - 0);
			break;
		case 2:
			retVal = Math.abs(xpos - 0) + Math.abs(ypos - 1);
			break;
		case 3:
			retVal = Math.abs(xpos - 0) + Math.abs(ypos - 2);
			break;
		case 4:
			retVal = Math.abs(xpos - 1) + Math.abs(ypos - 2);
			break;
		case 5:
			retVal = Math.abs(xpos - 2) + Math.abs(ypos - 2);
			break;
		case 6:
			retVal = Math.abs(xpos - 2) + Math.abs(ypos - 1);
			break;
		case 7:
			retVal = Math.abs(xpos - 2) + Math.abs(ypos - 0);
			break;
		case 8:
			retVal = Math.abs(xpos - 1) + Math.abs(ypos - 0);
			break;

		}
		return retVal;
	}

  public int evaluateSequenceScore(EightPuzzleBoard board) {
    int sequence_score = 0;

    for (int x = 0; x < 3; x++) {
      for (int y = 0; y < 3; y++) {
        if ( x == 1 && y == 1) {continue;}
        int tile = board.getValueAt(new XYLocation(x,y));
        int next_tile = getNextTile(x,y,board);
        int successor = getProperSuccessor(tile);

        if (next_tile != successor) {
          sequence_score += 2;
        }
      }
    }
    return sequence_score;
  }

  private int getNextTile(int x, int y, EightPuzzleBoard board) {
    int nextTile = 0;
    if (x == 0 && y != 2) {
      nextTile = board.getValueAt(new XYLocation(x,y+1));
    } else if (x != 2 && y == 2) {
      nextTile = board.getValueAt(new XYLocation(x+1,y));
    } else if (x == 2 && y != 0) {
      nextTile = board.getValueAt(new XYLocation(x,y-1));
    } else if (x != 0 && y == 0) {
      nextTile = board.getValueAt(new XYLocation(x-1,y));
    }
    return nextTile;
  }

  private int getProperSuccessor(int tile) {
    if (tile == 8) {
      return 1;
    } else {
      return tile + 1;
    }
  }

}
