package datinggame;

import java.util.LinkedHashSet;
import java.util.Set;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ActionsFunction;
import aima.core.search.framework.problem.ResultFunction;

/**
 * @author Ravi Mohan
 * @author Ciaran O'Reilly
 */
public class DatingGameFunctionFactory {
	private static ActionsFunction _actionsFunction = null;
	private static ResultFunction _resultFunction = null;

	public static ActionsFunction getActionsFunction() {
		if (null == _actionsFunction) {
			_actionsFunction = new DGActionsFunction();
		}
		return _actionsFunction;
	}

	public static ResultFunction getResultFunction() {
		if (null == _resultFunction) {
			_resultFunction = new DGResultFunction();
		}
		return _resultFunction;
	}

	private static class DGActionsFunction implements ActionsFunction {
		public Set<Action> actions(Object state) {
			DatingGameSeats seats = (DatingGameSeats) state;

			Set<Action> actions = new LinkedHashSet<Action>();

			if (seats.canMoveGap(DatingGameSeats.RIGHT1)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(1,1);
				actions.add(new DatingGameAction(DatingGameAction.RIGHT1, newSeats.toString()));
			}
			if (seats.canMoveGap(DatingGameSeats.RIGHT2)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(1,2);
				actions.add(new DatingGameAction(DatingGameAction.RIGHT2, newSeats.toString()));
			}
			if (seats.canMoveGap(DatingGameSeats.RIGHT3)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(1,3);
				actions.add(new DatingGameAction(DatingGameAction.RIGHT3, newSeats.toString()));
			}
			if (seats.canMoveGap(DatingGameSeats.LEFT1)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(-1,1);
				actions.add(new DatingGameAction(DatingGameAction.LEFT1, newSeats.toString()));
			}
			if (seats.canMoveGap(DatingGameSeats.LEFT2)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(-1,2);
				actions.add(new DatingGameAction(DatingGameAction.LEFT2, newSeats.toString()));
			}
			if (seats.canMoveGap(DatingGameSeats.LEFT3)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(-1,3);
				actions.add(new DatingGameAction(DatingGameAction.LEFT3, newSeats.toString()));
			}

			return actions;
		}
	}

	private static class DGResultFunction implements ResultFunction {
		public Object result(Object s, Action action) {

			DatingGameAction a = (DatingGameAction) action;

			DatingGameSeats seats = (DatingGameSeats) s;

			if (DatingGameAction.RIGHT1.equals(a.getName())
					&& seats.canMoveGap(DatingGameSeats.RIGHT1)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(1,1);
				return newSeats;
			} else if (DatingGameAction.RIGHT2.equals(a.getName())
					&& seats.canMoveGap(DatingGameSeats.RIGHT2)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(1,2);
				return newSeats;
			} else if (DatingGameAction.RIGHT3.equals(a.getName())
					&& seats.canMoveGap(DatingGameSeats.RIGHT3)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(1,3);
				return newSeats;
			} else if (DatingGameAction.LEFT1.equals(a.getName())
					&& seats.canMoveGap(DatingGameSeats.LEFT1)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(-1,1);
				return newSeats;
			}
			else if (DatingGameAction.LEFT2.equals(a.getName())
					&& seats.canMoveGap(DatingGameSeats.LEFT2)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(-1,2);
				return newSeats;
			}
			else if (DatingGameAction.LEFT3.equals(a.getName())
					&& seats.canMoveGap(DatingGameSeats.LEFT3)) {
				DatingGameSeats newSeats = new DatingGameSeats(seats);
				newSeats.moveGap(-1,3);
				return newSeats;
			}

			// The Action is not understood or is a NoOp
			// the result will be the current state.
			return s;
		}
	}
}
