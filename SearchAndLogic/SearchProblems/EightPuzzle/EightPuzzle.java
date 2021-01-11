//package aima.gui.demo.search;

import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.io.PrintStream;
import java.io.IOException;

import eightpuzzle.NMaxSwapHeuristicFunction;
import eightpuzzle.NilssonsDistanceHeuristicFunction;
import eightpuzzle.ManhattanHeuristicFunction;
import eightpuzzle.MisplacedTilleHeuristicFunction;
import eightpuzzle.EightPuzzleGoalTest;
import eightpuzzle.EightPuzzleFunctionFactory;
import eightpuzzle.EightPuzzleBoard;

import aima.core.agent.Action;
// import aima.core.environment.eightpuzzle.EightPuzzleBoard;
// import aima.core.environment.eightpuzzle.EightPuzzleFunctionFactory;
// import aima.core.environment.eightpuzzle.ManhattanHeuristicFunction;
// import aima.core.environment.eightpuzzle.MisplacedTilleHeuristicFunction;
import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.SearchForActions;
import aima.core.search.framework.problem.Problem;
import aima.core.search.framework.qsearch.GraphSearch;
import aima.core.search.informed.AStarSearch;


/**
 * @author Ravi Mohan
 *
 */

public class EightPuzzle {
	static EightPuzzleBoard figure1 = new EightPuzzleBoard(new int[] { 3, 5, 1, 8, 2, 6, 0, 7, 4 });;

	public static void main(String[] args) {
		try {
			PrintStream outputFile = new PrintStream("./solution_output.txt");

			eightPuzzleAStarManhattan(outputFile);
			eightPuzzleAStarMisplaced(outputFile);
			eightPuzzleAStarNMaxSwap(outputFile);
			eightPuzzleAStarNilssons(outputFile);

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void eightPuzzleAStarManhattan(PrintStream outputFile) {
		System.out.println("\nEightPuzzleDemo AStar Search (ManhattanHeursitic)-->");
		try {
			Problem problem = new Problem(figure1, EightPuzzleFunctionFactory.getActionsFunction(),
					EightPuzzleFunctionFactory.getResultFunction(), new EightPuzzleGoalTest());
			SearchForActions search = new AStarSearch(new GraphSearch(), new ManhattanHeuristicFunction());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
			// Outputs solution path to file

      // System.setOut(outputFile);
			// System.out.println("A* Manhattan Solution Path\r\n");
			printTitle("A* Manhattan Solution Path\r\n\r\n",outputFile);
      printActionsToFile(agent.getActions(),outputFile);
			printInstrumentationToFile(agent.getInstrumentation(),outputFile);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void eightPuzzleAStarMisplaced(PrintStream outputFile) {
		System.out.println("\nEightPuzzleDemo AStar Search (MisplacedTilleHeursitic)-->");
		try {
			Problem problem = new Problem(figure1, EightPuzzleFunctionFactory.getActionsFunction(),
					EightPuzzleFunctionFactory.getResultFunction(), new EightPuzzleGoalTest());
			SearchForActions search = new AStarSearch(new GraphSearch(), new MisplacedTilleHeuristicFunction());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
			// Outputs solution path to file
			printTitle("\r\n\r\nA* Misplaced Solution Path\r\n\r\n",outputFile);
      printActionsToFile(agent.getActions(),outputFile);
			printInstrumentationToFile(agent.getInstrumentation(),outputFile);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void eightPuzzleAStarNMaxSwap(PrintStream outputFile) {
		System.out.println("\nEightPuzzleDemo AStar Search (NMaxSwapHeursitic)-->");
		try {
			Problem problem = new Problem(figure1, EightPuzzleFunctionFactory.getActionsFunction(),
					EightPuzzleFunctionFactory.getResultFunction(), new EightPuzzleGoalTest());
			SearchForActions search = new AStarSearch(new GraphSearch(), new NMaxSwapHeuristicFunction());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
			// Outputs solution path to file
			printTitle("\r\n\r\nA* n-Max Swap Solution Path\r\n\r\n",outputFile);
      printActionsToFile(agent.getActions(),outputFile);
			printInstrumentationToFile(agent.getInstrumentation(),outputFile);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void eightPuzzleAStarNilssons(PrintStream outputFile) {
		System.out.println("\nEightPuzzleDemo AStar Search (NillsonsDistanceHeursitic)-->");
		try {
			Problem problem = new Problem(figure1, EightPuzzleFunctionFactory.getActionsFunction(),
					EightPuzzleFunctionFactory.getResultFunction(), new EightPuzzleGoalTest());
			SearchForActions search = new AStarSearch(new GraphSearch(), new NilssonsDistanceHeuristicFunction());
			SearchAgent agent = new SearchAgent(problem, search);
			printActions(agent.getActions());
			printInstrumentation(agent.getInstrumentation());
			// Outputs solution path to file
			printTitle("\r\n\r\nA* Nilsson's Solution Path\r\n\r\n",outputFile);
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
			System.out.println(action + "\r\n");
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
