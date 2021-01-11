package eightpuzzle;

import java.util.LinkedHashSet;
import java.util.Set;

import eightpuzzle.EightPuzzleBoard;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ActionsFunction;
import aima.core.search.framework.problem.ResultFunction;

/**
 * @author Ravi Mohan
 * @author Ciaran O'Reilly
 */
public class EightPuzzleFunctionFactory {
	private static ActionsFunction _actionsFunction = null;
	private static ResultFunction _resultFunction = null;

	public static ActionsFunction getActionsFunction() {
		if (null == _actionsFunction) {
			_actionsFunction = new EPActionsFunction();
		}
		return _actionsFunction;
	}

	public static ResultFunction getResultFunction() {
		if (null == _resultFunction) {
			_resultFunction = new EPResultFunction();
		}
		return _resultFunction;
	}

	private static class EPActionsFunction implements ActionsFunction {
		public Set<Action> actions(Object state) {
			EightPuzzleBoard board = (EightPuzzleBoard) state;

			Set<Action> actions = new LinkedHashSet<Action>();

			if (board.canMoveGap(EightPuzzleBoard.UP)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapUp();
				actions.add(new EightPuzzleAction(EightPuzzleAction.UP, "\r\n" + newBoard.toString()));
			}
			if (board.canMoveGap(EightPuzzleBoard.DOWN)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapDown();
				actions.add(new EightPuzzleAction(EightPuzzleAction.DOWN, "\r\n" + newBoard.toString()));
			}
			if (board.canMoveGap(EightPuzzleBoard.LEFT)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapLeft();
				actions.add(new EightPuzzleAction(EightPuzzleAction.LEFT, "\r\n" + newBoard.toString()));
			}
			if (board.canMoveGap(EightPuzzleBoard.RIGHT)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapRight();
				actions.add(new EightPuzzleAction(EightPuzzleAction.RIGHT, "\r\n" + newBoard.toString()));
			}

			return actions;
		}
	}

	private static class EPResultFunction implements ResultFunction {
		public Object result(Object s, Action action) {

			EightPuzzleAction a = (EightPuzzleAction) action;

			EightPuzzleBoard board = (EightPuzzleBoard) s;

			if (EightPuzzleAction.UP.equals(a.getName())
					&& board.canMoveGap(EightPuzzleBoard.UP)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapUp();
				return newBoard;
			} else if (EightPuzzleAction.DOWN.equals(a.getName())
					&& board.canMoveGap(EightPuzzleBoard.DOWN)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapDown();
				return newBoard;
			} else if (EightPuzzleAction.LEFT.equals(a.getName())
					&& board.canMoveGap(EightPuzzleBoard.LEFT)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapLeft();
				return newBoard;
			} else if (EightPuzzleAction.RIGHT.equals(a.getName())
					&& board.canMoveGap(EightPuzzleBoard.RIGHT)) {
				EightPuzzleBoard newBoard = new EightPuzzleBoard(board);
				newBoard.moveGapRight();
				return newBoard;
			}

			// The Action is not understood or is a NoOp
			// the result will be the current state.
			return s;
		}
	}
}
