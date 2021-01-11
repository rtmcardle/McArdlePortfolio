package blobs;

import aima.core.agent.impl.DynamicAction;
import aima.core.util.datastructure.XYLocation;

/**
 * Defines the actions of the Blobs game as
 * movements or placement of pieces
 */
public class BlobsAction extends DynamicAction {
  public static final String PASS = "Pass";
  public static final String PLACE = "Place";
  public static final String MOVEUP = "MoveUp";
  public static final String MOVEUPRIGHT = "MoveUpRight";
  public static final String MOVERIGHT = "MoveRight";
  public static final String MOVEDOWNRIGHT = "MoveDownRight";
  public static final String MOVEDOWN = "MoveDown";
  public static final String MOVEDOWNLEFT = "MoveDownLeft";
  public static final String MOVELEFT = "MoveLeft";
  public static final String MOVEUPLEFT = "MoveUpLeft";
  public static final String JUMPUP = "JumpUp";
  public static final String JUMPUPRIGHT = "JumpUpRight";
  public static final String JUMPRIGHT = "JumpRight";
  public static final String JUMPDOWNRIGHT = "JumpDownRight";
  public static final String JUMPDOWN = "JumpDown";
  public static final String JUMPDOWNLEFT = "JumpDownLeft";
  public static final String JUMPLEFT = "JumpLeft";
  public static final String JUMPUPLEFT = "JumpUpLeft";

  public static final String POSITION = "position";
	public static final String BLOBS_STATE = "state";

	/**
	 * Creates Blobs actions.
	 */

   public BlobsAction(String type, XYLocation position, String state) {
     super(type);
     setAttribute(POSITION, position);
     setAttribute(BLOBS_STATE, state);
   }

}
