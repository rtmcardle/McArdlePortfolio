package eightpuzzle;

import aima.core.agent.impl.DynamicAction;

/**
 * Defines the actions of the EightPuzzle as movements of the gap
 */
public class EightPuzzleAction extends DynamicAction {
  public static final String UP = "Move Up";
  public static final String DOWN = "Move Down";
  public static final String LEFT = "Move Left";
  public static final String RIGHT = "Move Right";

	public static final String EIGHT_PUZZLE_STATE = "state";

	/**
	 * Creates an EightPuzzle action.
	 */
	public EightPuzzleAction(String type, String state) {
		super(type);
		setAttribute(EIGHT_PUZZLE_STATE, state);
	}

}
