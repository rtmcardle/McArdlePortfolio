package datinggame;

import datinggame.DatingGameSeats;
import aima.core.search.framework.problem.GoalTest;

/**
 * @author Ravi Mohan
 *
 */
public class DatingGameGoalTest implements GoalTest {
	DatingGameSeats goal = new DatingGameSeats(new int[] { 1, 2, 1, 2, 1,
				2, 0 });

	public boolean isGoalState(Object state) {
		DatingGameSeats seats = (DatingGameSeats) state;
		// System.out.println(seats.toString());
		return seats.equals(goal);
	}
}
