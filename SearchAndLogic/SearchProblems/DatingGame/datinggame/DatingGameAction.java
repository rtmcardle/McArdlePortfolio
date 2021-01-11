package datinggame;

import aima.core.agent.impl.DynamicAction;

/**
 *
 */
public class DatingGameAction extends DynamicAction {
  public static final String RIGHT1 = "Move Gap Right 1 Seat";
  public static final String RIGHT2 = "Move Gap Right 2 Seats";
  public static final String RIGHT3 = "Move Gap Right 3 Seats";
  public static final String LEFT1 = "Move Gap Left 1 Seat";
  public static final String LEFT2 = "Move Gap Left 2 Seats";
  public static final String LEFT3 = "Move Gap Left 3 Seats";

	public static final String DATING_GAME_STATE = "state";

	/**
	 * Creates a DatingGame action.
	 */
	public DatingGameAction(String type, String state) {
		super(type);
		setAttribute(DATING_GAME_STATE, state);
	}

}
