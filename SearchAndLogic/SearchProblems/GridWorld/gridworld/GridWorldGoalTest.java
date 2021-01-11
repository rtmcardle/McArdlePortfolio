package gridworld;

import gridworld.GridWorldCells;
import aima.core.search.framework.problem.GoalTest;

/**
 * @author Ravi Mohan
 *
 */
public class GridWorldGoalTest implements GoalTest {
	GridWorldCells goal = new GridWorldCells(new int[] { 0, 1, 0, 0, 0,
				0, 0, 0, 0 });

	public boolean isGoalState(Object state) {
		GridWorldCells cells = (GridWorldCells) state;
		return cells.equals(goal);
	}
}
