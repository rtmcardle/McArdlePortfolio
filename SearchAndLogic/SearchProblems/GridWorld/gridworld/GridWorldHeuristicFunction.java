package gridworld;

import java.lang.Math;

import aima.core.search.framework.evalfunc.HeuristicFunction;
import aima.core.util.datastructure.XYLocation;

/**
 * @author Ravi Mohan
 *
 */
public class GridWorldHeuristicFunction implements HeuristicFunction {

	public double h(Object state) {
		GridWorldCells cells = (GridWorldCells) state;
		double retVal = 0;
		XYLocation loc = cells.getLocationOf(1);
		retVal += evaluateGridSLD(loc);
		return retVal;

	}

	public double evaluateGridSLD(XYLocation loc) {
		double retVal = 0;
		int xpos = loc.getXCoOrdinate();
		int ypos = loc.getYCoOrdinate();

    double xsquare = Math.pow(xpos - 0,2);
    double ysquare = Math.pow(ypos - 1,2);

    double sumOfSquares = xsquare + ysquare;

		retVal = Math.sqrt(sumOfSquares);

		return retVal;
	}
}
