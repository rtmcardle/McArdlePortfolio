package gridworld;

import java.util.LinkedHashSet;
import java.util.Set;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ActionsFunction;
import aima.core.search.framework.problem.ResultFunction;

/**
 * @author Ravi Mohan
 * @author Ciaran O'Reilly
 */
public class GridWorldFunctionFactory {
	private static ActionsFunction _actionsFunction = null;
	private static ResultFunction _resultFunction = null;

	public static ActionsFunction getActionsFunction() {
		if (null == _actionsFunction) {
			_actionsFunction = new GWActionsFunction();
		}
		return _actionsFunction;
	}

	public static ResultFunction getResultFunction() {
		if (null == _resultFunction) {
			_resultFunction = new GWResultFunction();
		}
		return _resultFunction;
	}

	private static class GWActionsFunction implements ActionsFunction {
		public Set<Action> actions(Object state) {
			GridWorldCells cells = (GridWorldCells) state;

			Set<Action> actions = new LinkedHashSet<Action>();

			if (cells.canMoveAgent(GridWorldCells.UP)) {
				actions.add(GridWorldCells.UP);
			}
			if (cells.canMoveAgent(GridWorldCells.DOWN)) {
				actions.add(GridWorldCells.DOWN);
			}
			if (cells.canMoveAgent(GridWorldCells.LEFT)) {
				actions.add(GridWorldCells.LEFT);
			}
			if (cells.canMoveAgent(GridWorldCells.RIGHT)) {
				actions.add(GridWorldCells.RIGHT);
			}

			return actions;
		}
	}

	private static class GWResultFunction implements ResultFunction {
		public Object result(Object s, Action a) {
			GridWorldCells cells = (GridWorldCells) s;

			if (GridWorldCells.UP.equals(a)
					&& cells.canMoveAgent(GridWorldCells.UP)) {
				GridWorldCells newCells = new GridWorldCells(cells);
				newCells.moveAgentUp();
				return newCells;
			} else if (GridWorldCells.DOWN.equals(a)
					&& cells.canMoveAgent(GridWorldCells.DOWN)) {
				GridWorldCells newCells = new GridWorldCells(cells);
				newCells.moveAgentDown();
				return newCells;
			} else if (GridWorldCells.LEFT.equals(a)
					&& cells.canMoveAgent(GridWorldCells.LEFT)) {
				GridWorldCells newCells = new GridWorldCells(cells);
				newCells.moveAgentLeft();
				return newCells;
			} else if (GridWorldCells.RIGHT.equals(a)
					&& cells.canMoveAgent(GridWorldCells.RIGHT)) {
				GridWorldCells newCells = new GridWorldCells(cells);
				newCells.moveAgentRight();
				return newCells;
			}

			// The Action is not understood or is a NoOp
			// the result will be the current state.
			return s;
		}
	}
}
