import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.io.PrintStream;
import java.io.IOException;

import datinggame.DatingGameSeats;
import datinggame.DatingGameFunctionFactory;
import datinggame.DatingGameGoalTest;
import datinggame.DatingGameHeuristicFunction;
import datinggame.DatingGameStepCost;

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

public class DatingGame {
	static DatingGameSeats initialState = new DatingGameSeats(new int[] { 1, 1, 1, 0, 2, 2, 2 });
	// static DatingGameSeats initialState = new DatingGameSeats(new int[] { 2, 1, 2, 1, 0, 1, 2 });


	public static void main(String[] args) {
		try {
			PrintStream outputFile = new PrintStream("./solution_output.txt");

			datingGameIDLS(outputFile);
			datingGameAStar(outputFile);
		} catch (IOException e) {
			e.printStackTrace();
		}


	}

	private static void datingGameIDLS(PrintStream outputFile) {
		System.out.println("\nDating Game Iterative DLS -->");
		try {
			Problem problem = new Problem(initialState, DatingGameFunctionFactory.getActionsFunction(),
					DatingGameFunctionFactory.getResultFunction(), new DatingGameGoalTest(), new DatingGameStepCost());
			SearchForActions search = new IterativeDeepeningSearch();
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
			// Outputs solution path to file
			printTitle("Iterative DLS Solution Path\r\n\r\n",outputFile);
      printActionsToFile(agent.getActions(),outputFile);
			printInstrumentationToFile(agent.getInstrumentation(),outputFile);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void datingGameAStar(PrintStream outputFile) {
		System.out.println("\nDating Game AStar Search -->");
		try {
			Problem problem = new Problem(initialState, DatingGameFunctionFactory.getActionsFunction(),
					DatingGameFunctionFactory.getResultFunction(), new DatingGameGoalTest(), new DatingGameStepCost());
			SearchForActions search = new AStarSearch(new GraphSearch(), new DatingGameHeuristicFunction());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
			// Outputs solution path to file
			printTitle("\r\n\r\nA* Solution Path\r\n\r\n",outputFile);
      printActionsToFile(agent.getActions(),outputFile);
			printInstrumentationToFile(agent.getInstrumentation(),outputFile);
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

	private static void printActionsToFile(List<Action> actions, PrintStream outputFile) {
		for (int i = 0; i < actions.size(); i++) {
			String action = actions.get(i).toString();
			outputFile.append(action + "\r\n");
		}
	}

	private static void printInstrumentationToFile(Properties properties, PrintStream outputFile) {
		Iterator<Object> keys = properties.keySet().iterator();
		while (keys.hasNext()) {
			String key = (String) keys.next();
			String property = properties.getProperty(key);
			outputFile.append(key + " : " + property + "\r\n");
		}

	}

	private static void printTitle(String title, PrintStream outputFile) {
		outputFile.append(title);
	}

}
