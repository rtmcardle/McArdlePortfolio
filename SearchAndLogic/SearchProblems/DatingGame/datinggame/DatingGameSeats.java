package datinggame;

import java.util.ArrayList;
import java.util.List;

import aima.core.agent.Action;
import aima.core.agent.impl.DynamicAction;
import aima.core.util.datastructure.XYLocation;

/**
 * @author Ryan McArdle
 */
public class DatingGameSeats {

	// actions describe direction to move gap and number of people moved

	public static Action RIGHT1 = new DynamicAction("Right1");

	public static Action RIGHT2 = new DynamicAction("Right2");

	public static Action RIGHT3 = new DynamicAction("Right3");

	public static Action LEFT1 = new DynamicAction("Left1");

	public static Action LEFT2 = new DynamicAction("Left2");

	public static Action LEFT3 = new DynamicAction("Left3");

	private int[] state;

	//
	// PUBLIC METHODS
	//

	public DatingGameSeats() {
		// 0 = empty seat
		// 1 = male
		// 2 = female
		state = new int[] { 1, 1, 1, 0, 2, 2, 2 };
	}

	public DatingGameSeats(int[] state) {
		this.state = new int[state.length];
		System.arraycopy(state, 0, this.state, 0, state.length);
	}

	public DatingGameSeats(DatingGameSeats copyBoard) {
		this(copyBoard.getState());
	}

	public int[] getState() {
		return state;
	}

	public int getValueAt(int absPos) {
		return state[absPos];
	}



	public void moveGap(int direction, int moved) {
		// direction == 1 corresponds to gap moving right
		// direction == -1 corresponds to gap moving right 
		// moved is the number of spaces the gap moves
		// if moved == 1 or moved == 2, then cost == 1
		// if moved == 3, then cost == 2
		int gapPos = getGapPosition();
		int posToSwap = gapPos + (direction*(moved));
		int valueToSwap = getValueAt(posToSwap);

		setValue(gapPos, valueToSwap);
		setValue(posToSwap, 0);

	}

	// public List<Integer> getPositions() {
	// 	ArrayList<Integer> retVal = new ArrayList<Integer>();
	// 	for (int i = 0; i < 7; i++) {
	// 		int absPos = getPositionOf(i);
	// 		XYLocation loc = new XYLocation(getXCoord(absPos),
	// 				getYCoord(absPos));
	// 		retVal.add(loc);
	//
	// 	}
	// 	return retVal;
	// }

	// public void setBoard(List<XYLocation> locs) {
	// 	int count = 0;
	// 	for (int i = 0; i < locs.size(); i++) {
	// 		XYLocation loc = locs.get(i);
	// 		this.setValue(loc.getXCoOrdinate(), loc.getYCoOrdinate(), count);
	// 		count = count + 1;
	// 	}
	// }

	public boolean canMoveGap(Action where) {
		boolean retVal = true;
		int absPos = getGapPosition();
		if (where.equals(RIGHT1))
			retVal = (absPos < 6);
		else if (where.equals(RIGHT2))
			retVal = (absPos < 5);
		else if (where.equals(RIGHT3))
			retVal = (absPos < 4);
		else if (where.equals(LEFT1))
			retVal = (absPos > 0);
		else if (where.equals(LEFT2))
			retVal = (absPos > 1);
		else if (where.equals(LEFT3))
			retVal = (absPos > 2);
		return retVal;
	}

	@Override
	public boolean equals(Object o) {

		if (this == o) {
			return true;
		}
		if ((o == null) || (this.getClass() != o.getClass())) {
			return false;
		}
		DatingGameSeats aState = (DatingGameSeats) o;

		for (int i = 0; i < 7; i++) {
			if (this.getValueAt(i) != aState.getValueAt(i)) {
				return false;
			}
		}
		return true;
	}

	// @Override
	// public int hashCode() {
	// 	int result = 17;
	// 	for (int i = 0; i < 8; i++) {
	// 		int position = this.getPositionOf(i);
	// 		result = 37 * result + position;
	// 	}
	// 	return result;
	// }

	@Override
	public String toString() {
		String retVal = "";
		for (int i  = 0; i < 7; i++) {
			retVal += state[i] + " ";
		}
		return retVal;
	}

	//
	// PRIVATE METHODS
	//

	// private int getValueAt(int absPos) {
	// 	return state[absPos];
	// }

	private int getGapPosition() {
		int retVal = -1;
		for (int i = 0; i < 7; i++) {
			if (state[i] == 0) {
				retVal = i;
			}
		}
		return retVal;
	}

	// private int getPositionOf(int val) {
	//
	// 	return -1;
	// }

	private void setValue(int pos, int val) {
		state[pos] = val;
	}
}
