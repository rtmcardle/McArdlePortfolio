package datinggame;

import datinggame.DatingGameSeats;
import aima.core.search.framework.evalfunc.HeuristicFunction;


/**
 * @author Ravi Mohan
 *
 */
public class DatingGameHeuristicFunction implements HeuristicFunction {

	public double h(Object state) {
		DatingGameSeats seats = (DatingGameSeats) state;
		int retVal = 0;
		for (int i = 1; i < 6; i++) {
			retVal += evaluateDatingGameHeuristicOf(i,seats);
		}
		return retVal;

	}

	public int evaluateDatingGameHeuristicOf(int i, DatingGameSeats seats) {

	/* Heuristic measures the M/F pairings and distance of gap from goal
	 * +1 to heuristic value for each same-gender pairing (ignoring the gap)
	 * +1/2 (round down) for each space out of place the gap is
	 * This heuristic (like Nilsson's) is not admissible
	 */

		int retVal = 0;
		int position = i;
		int currentValue = seats.getState()[i];

		if (currentValue == 0) {
			if (i != 6) {
				retVal = (6 - i)/2;
			}
		} else {
			int nextValue = seats.getValueAt(i+1);
			if ((nextValue == 0) && (i != 5)) {
				nextValue = seats.getValueAt(i+2);
			}
			if (currentValue == nextValue) {
				retVal += 1;
			}
		}
		return retVal;
	}

}
