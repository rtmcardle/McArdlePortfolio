import java.util.Iterator;
import java.util.List;
import java.util.Properties;

import gridworld.GridWorldCells;
import gridworld.GridWorldFunctionFactory;
import gridworld.GridWorldGoalTest;
import gridworld.GridWorldHeuristicFunction;

import aima.core.agent.Action;
import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.SearchForActions;
import aima.core.search.framework.problem.Problem;
import aima.core.search.framework.qsearch.GraphSearch;
import aima.core.search.informed.AStarSearch;
import aima.core.search.uninformed.IterativeDeepeningSearch;

/**
 * @author Ravi Mohan
 *
 */

public class GridWorld {
	static GridWorldCells initialState = new GridWorldCells(new int[] { 0, 2, 0, 0, 0, 0, 1, 0, 0 });

	public static void main(String[] args) {
		gridWorldAStar();
	}

	// private static void gridWorldIDAStar() {
	// 	System.out.println("\nGrid World Iterative Deepening A* -->");
	// 	try {
	// 		//Problem problem = new GridWorldProblem(initialState, goalState,
	// 		//		GridWorldFunctionFactory.getResultFunction(), new GridWorldGoalTest(), new GridWorldStepCost());
	// 		SearchForActions search = new IterativeDeepeningSearch();
  //     SearchForStates states = new SearchForStates();
	// 		GriddWorldAgent agent = new GridWorldAgent(problem, search);
	// 		printActions(agent.getActions());
	// 		printInstrumentation(agent.getInstrumentation());
	// 	} catch (Exception e) {
	// 		e.printStackTrace();
	// 	}
  //
	// }

	private static void gridWorldAStar() {
		System.out.println("\nGrid World AStar Search -->");
		try {
			Problem problem = new Problem(initialState, GridWorldFunctionFactory.getActionsFunction(),
					GridWorldFunctionFactory.getResultFunction(), new GridWorldGoalTest());
			SearchForActions search = new AStarSearch(new GraphSearch(), new GridWorldHeuristicFunction());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
		} catch (Exception e) {
			e.printStackTrace();
		}

	}


	private static void printInstrumentation(Properties properties) {
		Iterator<Object> keys = properties.keySet().iterator();
		while (keys.hasNext()) {
			String key = (String) keys.next();
			String property = properties.getProperty(key);
			System.out.println(key + " : " + property);
		}

	}

	private static void printActions(List<Action> actions) {
		for (int i = 0; i < actions.size(); i++) {
			String action = actions.get(i).toString();
			System.out.println(action);
		}
	}

}
