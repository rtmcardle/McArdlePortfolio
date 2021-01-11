package waterjugs;

import java.util.ArrayList;
import java.util.List;

import aima.core.agent.Action;
import aima.core.agent.impl.DynamicAction;

public class WaterJugs {

  // Defines the WaterJugs class, their kinds of states, action, methods, etc.


  // Fill corresponding jug from the pump
  public static Action FillFour = new DynamicAction("FillFour");

  public static Action FillThree = new DynamicAction("FillThree");

  // Empties corresponding jug of water
  public static Action EmptyFour = new DynamicAction("EmptyFour");

  public static Action EmptyThree = new DynamicAction("EmptyThree");

  // Empties corresponding jug into the other jug, until the other is full
  public static Action FourToThree = new DynamicAction("FourToThree");

  public static Action ThreeToFour = new DynamicAction("ThreeToFour");


  private int[] state;


  //
  // PUBLIC METHODS
  //

  public WaterJugs() {
    state = new int[] {0,0};
  }

  public WaterJugs(int[] state) {
    this.state = new int[state.length];
    System.arraycopy(state, 0, this.state, 0, state.length);
  }

  public WaterJugs(WaterJugs copyJugs) {
    this(copyJugs.getState());
  }

  public int[] getState() {
    return state;
  }

  public int getFour(){
    return state[0];
  }

  public int getThree(){
    return state[1];
  }

  public void fillJugFour() {
    setValue(0, 4);
  }

  public void fillJugThree() {
    setValue(1,3);
  }

  public void emptyJugFour() {
    setValue(0,0);
  }

  public void emptyJugThree() {
    setValue(1,0);
  }

  public void fourToThree() {
    int water = getFour();
    int room = 3-getThree();

    if (water>=room) {
      setValue(0,getFour()-room);
      setValue(1,3);
    } else {
      setValue(0,0);
      setValue(1,getThree()+water);
    }
  }

  public void threeToFour() {
    int water = getThree();
    int room = 4-getFour();

    if (water>=room) {
      setValue(0,4);
      setValue(1,getThree()-room);
    } else {
      setValue(0,getFour()+water);
      setValue(1,0);
    }
  }

  public boolean canFillFour() {
    if (getFour() == 4) {
      return false;
    } else {
      return true;
    }
  }

  public boolean canFillThree() {
    if (getThree() == 3) {
      return false;
    } else {
      return true;
    }
  }

  public boolean canEmptyFour(){
    if (getFour() == 0) {
      return false;
    } else {
      return true;
    }
  }

  public boolean canEmptyThree() {
    if (getThree() == 0) {
      return false;
    } else {
      return true;
    }
  }


  @Override
  public boolean equals(Object o) {

    if (this == o) {
      return true;
    }
    if ((o == null) || (this.getClass() != o.getClass())) {
      return false;
    }
    WaterJugs aJugs = (WaterJugs) o;

    for (int i = 0; i < 2; i++) {
      if (this.state[i] != aJugs.state[i]) {
        return false;
      }
    }
    return true;
  }

  @Override
	public String toString() {
		String retVal = " ";
		for (int i  = 0; i < 2; i++) {
			retVal += state[i] + " ";
		}
		return retVal;
	}





  //
  // PRIVATE METHODS
  //

  private void setValue(int jug, int val) {
    state[jug] = val;
  }

}
