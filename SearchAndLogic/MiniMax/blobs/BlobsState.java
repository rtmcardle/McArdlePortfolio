package blobs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


import blobs.BlobsAction;

import aima.core.util.datastructure.XYLocation;

/**
 * A state of the Blobs game is characterized by a board containing
 * symbols X and O, the next player to move, and an utility information.
 *
 */
public class BlobsState implements Cloneable {
	public static final String O = "O";
	public static final String X = "X";
	public static final String EMPTY = "-";
	public boolean doublePass = false;
	//
  private int nSquares = 7; // nSquares represents the length of one side of the board
  private String[] board = new String[nSquares*nSquares];

	private String playerToMove = X;
	private double utility = 0; // positive: win for X, negative: win for O, 0: draw
	private boolean playerJustPassed = false;

	public void setBoard() {
		// Initializes a board for game start
		for (int i = 0; i<nSquares; i++) {
			for (int j = 0 ; j<nSquares; j++) {
				board[getAbsPosition(i,j)] = EMPTY;
			}
		}
		board[getAbsPosition(0,0)] = X;
		board[getAbsPosition(nSquares-1,nSquares-1)] = X;
		board[getAbsPosition(0,nSquares-1)] = O;
		board[getAbsPosition(nSquares-1,0)] = O;
	}

	public int getNSquares() {
		return nSquares;
	}

	public String getPlayerToMove() {
		return playerToMove;
	}

	public boolean isEmpty(XYLocation location) {
		return isEmpty(location.getXCoOrdinate(),location.getYCoOrdinate());
	}

	public boolean isEmpty(int col, int row) {
		if (((col<0) || (col>=nSquares)) ||
				((row<0) || (row>=nSquares))) {
					return false;
				} else {
					if ((col>=nSquares) || (row>=nSquares)){
						System.out.println(String.valueOf(col)+","+String.valueOf(row));
					}
					return board[getAbsPosition(col, row)] == EMPTY;
				}

	}

	public boolean isAdjacent(XYLocation place, String adjPlayer) {
		return isAdjacent(place.getXCoOrdinate(), place.getYCoOrdinate(),adjPlayer);
	}

	// return true if input space is adjacent to current players piece
	public boolean isAdjacent(int col, int row, String adjPlayer) {
		boolean retVal = false;
		for (int i = -1; i < 2; i++) {
			for (int j = -1; j < 2; j++) {
				int xVal = col+i;
				int yVal = row+j;
				if ((0<=xVal) && (xVal<nSquares) &&
						(0<=yVal) && (yVal<nSquares)) {
					if (getValue(xVal,yVal) == adjPlayer) {
						retVal = true;
					}
				}
			}
		}
		return retVal;
	}

	public String getValue(XYLocation place) {
		return getValue(place.getXCoOrdinate(), place.getYCoOrdinate());
	}

	public String getValue(int col, int row) {
		if ((0<=col) && (col<nSquares) &&
				(0<=row) && (row<nSquares)) {
					return board[getAbsPosition(col, row)];
		} else {
			return "Out of Bounds";
		}
	}

	public double getUtility(String player) {
		// defines utility as the difference between number of pieces
    // plus ~1/2 the number of 'place' moves available to you
		// minus ~1/2 those available to opponent
		// 3 potential 'place' moves must be gained to sacrifice
		// an immediate placement; 'a piece on the board is worth more
		// than two in the bush'
		String opp = "";
		if (player == X) {
			opp = O;
		} else {
			opp = X;
		}
		// counts place moves
		int numPlacePlayer = 0;
		int numPlaceEnemy = 0;
		for (XYLocation space : getUnMarkedPositions()) {
			if (isAdjacent(space,player)) {
				numPlacePlayer++;
			}
			if (isAdjacent(space,opp)) {
				numPlaceEnemy++;
			}
		}
		utility = (getNumberOf(player) - getNumberOf(opp))+0.49*(numPlacePlayer-numPlaceEnemy);

		return utility;
	}

	public void clear(XYLocation action) {
		clear(action.getXCoOrdinate(), action.getYCoOrdinate());
	}

	public void clear(int col, int row) {
		if (getValue(col,row) != EMPTY) {
			board[getAbsPosition(col,row)] = EMPTY;
		}
	}

	public void pass() {
		if (!playerJustPassed) {
			playerJustPassed = true;
			playerToMove = (playerToMove == X ? O : X);
		} else {
			playerToMove = (playerToMove == X ? O : X);
			doublePass = true;
		}
	}

	public boolean hasDoublePass() {
		if (doublePass){
			return true;
		} else {
			return false;
		}
	}

	public void place(XYLocation action) {
		place(action.getXCoOrdinate(), action.getYCoOrdinate());
	}

	public void place(int col, int row) {
		if ((0<=col) && (col<nSquares) &&
				(0<=row) && (row<nSquares) &&
				(getValue(col,row) == EMPTY)) {
					board[getAbsPosition(col, row)] = playerToMove;
					playerJustPassed = false;
					playerToMove = (playerToMove == X ? O : X);
		}
	}

	public void move(XYLocation start, XYLocation end) {
		int startCol = start.getXCoOrdinate();
		int startRow = start.getYCoOrdinate();
		int endCol = end.getXCoOrdinate();
		int endRow = end.getYCoOrdinate();
		if ((0<=endCol) && (endCol<nSquares) &&
				(0<=endRow) && (endRow<nSquares) &&
				(getValue(endCol,endRow) == EMPTY)) {
					clear(start);
					place(end);
		}
	}

	public int getNumberOfMarkedPositions() {
		int retVal = 0;
		for (int col = 0; col < nSquares; col++) {
			for (int row = 0; row < nSquares; row++) {
				if (!(isEmpty(col, row))) {
					retVal++;
				}
			}
		}
		return retVal;
	}

  public int getNumberOf(String player) {
    int retVal = 0;
    for (int col = 0; col <nSquares; col++) {
      for (int row = 0; row < nSquares; row++) {
        if (getValue(col,row) == player) {
          retVal += 1;
        }
      }
    }
    return retVal;
  }

	public List<XYLocation> getUnMarkedPositions() {
		List<XYLocation> result = new ArrayList<XYLocation>();
		for (int col = 0; col < nSquares; col++) {
			for (int row = 0; row < nSquares; row++) {
				if (isEmpty(col, row)) {
					result.add(new XYLocation(col, row));
				}
			}
		}
		return result;
	}

	public List<XYLocation> getMarkedPositions() {
		List<XYLocation> result = new ArrayList<XYLocation>();
		for (int col = 0; col < nSquares; col++) {
			for (int row = 0; row < nSquares; row++) {
				if (!isEmpty(col, row)) {
					result.add(new XYLocation(col, row));
				}
			}
		}
		return result;
	}

	public List<XYLocation> getPlayerPieces(String player) {
		ArrayList<XYLocation> pieces = new ArrayList<XYLocation>();
		for (XYLocation piece : getMarkedPositions()) {
			if (getValue(piece) == getPlayerToMove()) {
				pieces.add(piece);
			}
		}
		return pieces;
	}

	@Override
	public BlobsState clone() {
		BlobsState copy = null;
		try {
			copy = (BlobsState) super.clone();
			copy.board = Arrays.copyOf(board, board.length);
		} catch (CloneNotSupportedException e) {
			e.printStackTrace(); // should never happen...
		}
		return copy;
	}

	@Override
	public boolean equals(Object anObj) {
		if (anObj != null && anObj.getClass() == getClass()) {
			BlobsState anotherState = (BlobsState) anObj;
			for (int i = 0; i < nSquares*nSquares; i++) {
				if (board[i] != anotherState.board[i]) {
					return false;
				}
			}
			return true;
		}
		return false;
	}

	@Override
	public int hashCode() {
		// Need to ensure equal objects have equivalent hashcodes (Issue 77).
		return toString().hashCode();
	}

	@Override
	public String toString() {
		StringBuilder strBuilder = new StringBuilder();
		for (int row = 0; row < nSquares; row++) {
			for (int col = 0; col < nSquares; col++) {
				strBuilder.append(getValue(col, row) + " ");
			}
			strBuilder.append("\n");
		}
		return strBuilder.toString();
	}

	//
	// PRIVATE METHODS
	//

	private int getAbsPosition(int col, int row) {
		if (((col<0) || (col>=nSquares)) ||
				((row<0) || (row>=nSquares))) {
					return -1;
		} else {
			return row * nSquares + col;
		}
	}
}
