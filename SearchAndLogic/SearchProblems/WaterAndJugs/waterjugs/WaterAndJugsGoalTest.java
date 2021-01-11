package waterjugs;

import aima.core.search.framework.problem.GoalTest;

// Declares the goal state for WaterJugs and tests for it

public class WaterAndJugsGoalTest implements GoalTest {
  WaterJugs goal = new WaterJugs(new int[] {2,0});

  public boolean isGoalState(Object state) {
    WaterJugs jugs = (WaterJugs) state;
    return jugs.equals(goal);
  }
}
