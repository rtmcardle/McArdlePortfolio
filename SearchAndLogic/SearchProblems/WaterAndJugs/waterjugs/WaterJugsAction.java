package waterjugs;

import aima.core.agent.impl.DynamicAction;

/**
 *
 */
public class WaterJugsAction extends DynamicAction {
  public static final String FILLFOUR = "Fill Four Gallon";
  public static final String FILLTHREE = "Fill Three Gallon";
  public static final String EMPTYFOUR = "Empty Four Gallon";
  public static final String EMPTYTHREE = "Empty Three Gallon";
  public static final String FOURTOTHREE = "Pour Four into Three";
  public static final String THREETOFOUR = "Pour Three into Four";

	public static final String WATER_JUG_STATE = "state";

	/**
	 * Creates a WaterJug action.
	 */
	public WaterJugsAction(String type, String state) {
		super(type);
		setAttribute(WATER_JUG_STATE, state);
	}

}
