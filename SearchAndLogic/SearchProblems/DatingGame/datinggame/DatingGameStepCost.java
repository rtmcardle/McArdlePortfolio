package datinggame;

import datinggame.DatingGameAction;
import aima.core.agent.Action;
import aima.core.search.framework.problem.StepCostFunction;

/**
 * Returns one for every action.
 *
 * @author Ravi Mohan
 */
public class DatingGameStepCost implements StepCostFunction {

	public double c(Object stateFrom, Action a, Object stateTo) {

		DatingGameAction action = (DatingGameAction) a;

		int retVal = 0;
    if (DatingGameAction.RIGHT1.equals(action.getName())) {
      retVal = 1;
    } else if (DatingGameAction.RIGHT2.equals(action.getName())) {
      retVal = 1;
    } else if (DatingGameAction.RIGHT3.equals(action.getName())) {
      retVal = 2;
    } else if (DatingGameAction.LEFT1.equals(action.getName())) {
      retVal = 1;
    } else if (DatingGameAction.LEFT2.equals(action.getName())) {
      retVal = 1;
    } else if (DatingGameAction.LEFT3.equals(action.getName())) {
      retVal = 2;
    }
		return retVal;
	}
}
