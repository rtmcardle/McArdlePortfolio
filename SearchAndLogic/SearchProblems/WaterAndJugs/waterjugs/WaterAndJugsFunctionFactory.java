package waterjugs;

import java.util.LinkedHashSet;
import java.util.Set;

import waterjugs.WaterJugsAction;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ActionsFunction;
import aima.core.search.framework.problem.ResultFunction;

public class WaterAndJugsFunctionFactory {
  private static ActionsFunction _actionsFunction = null;
  private static ResultFunction _resultFunction = null;

  public static ActionsFunction getActionsFunction() {
    if (null == _actionsFunction) {
      _actionsFunction = new WJActionsFunction();
    }
    return _actionsFunction;
  }

  public static ResultFunction getResultFunction() {
    if (null == _resultFunction) {
      _resultFunction = new WJResultFunction();
    }
    return _resultFunction;
  }

  private static class WJActionsFunction implements ActionsFunction {
    public Set<Action> actions(Object state) {
      WaterJugs jugs = (WaterJugs) state;

      Set<Action> actions = new LinkedHashSet<Action>();

      if (jugs.canFillFour()){
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.fillJugFour();
        actions.add(new WaterJugsAction(WaterJugsAction.FILLFOUR, newJugs.toString()));
      }
      if (jugs.canFillThree()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.fillJugThree();
        actions.add(new WaterJugsAction(WaterJugsAction.FILLTHREE, newJugs.toString()));
      }
      if (jugs.canEmptyFour()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.emptyJugFour();
        actions.add(new WaterJugsAction(WaterJugsAction.EMPTYFOUR, newJugs.toString()));
      }
      if (jugs.canEmptyThree()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.emptyJugFour();
        actions.add(new WaterJugsAction(WaterJugsAction.EMPTYTHREE, newJugs.toString()));
      }
      if (jugs.canFillFour() && jugs.canEmptyThree()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.threeToFour();
        actions.add(new WaterJugsAction(WaterJugsAction.THREETOFOUR, newJugs.toString()));
      }
      if (jugs.canFillThree() && jugs.canEmptyFour()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.fourToThree();
        actions.add(new WaterJugsAction(WaterJugsAction.FOURTOTHREE, newJugs.toString()));
      }

      return actions;
    }
  }

  private static class WJResultFunction implements ResultFunction {
    public Object result(Object s, Action action) {

      WaterJugsAction a = (WaterJugsAction) action;

      WaterJugs jugs = (WaterJugs) s;

      if (WaterJugsAction.FILLFOUR.equals(a.getName())
          && jugs.canFillFour()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.fillJugFour();
        return newJugs;
      } else if (WaterJugsAction.FILLTHREE.equals(a.getName())
          && jugs.canFillThree()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.fillJugThree();
        return newJugs;
      } else if (WaterJugsAction.EMPTYFOUR.equals(a.getName())
          && jugs.canEmptyFour()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.emptyJugFour();
        return newJugs;
      } else if (WaterJugsAction.EMPTYTHREE.equals(a.getName())
          && jugs.canEmptyThree()) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.emptyJugThree();
        return newJugs;
      } else if (WaterJugsAction.THREETOFOUR.equals(a.getName())
          && (jugs.canFillFour() && jugs.canEmptyThree())) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.threeToFour();
        return newJugs;
      } else if (WaterJugsAction.FOURTOTHREE.equals(a.getName())
          && (jugs.canFillThree() && jugs.canEmptyFour())) {
        WaterJugs newJugs = new WaterJugs(jugs);
        newJugs.fourToThree();
        return newJugs;
      }


      return s;
    }
  }
}
