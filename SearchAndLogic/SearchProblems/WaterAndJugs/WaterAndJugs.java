import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.io.PrintStream;
import java.io.IOException;

import waterjugs.WaterJugs;
import waterjugs.WaterAndJugsFunctionFactory;
import waterjugs.WaterAndJugsGoalTest;

import aima.core.agent.Action;
import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.SearchForActions;
import aima.core.search.framework.problem.Problem;
import aima.core.search.uninformed.IterativeDeepeningSearch;


public class WaterAndJugs {
  static WaterJugs initialState = new WaterJugs();

  public static void main(String[] args) {
    try {
      PrintStream outputFile = new PrintStream("./solution_output.txt");

      waterJugsIDLSSolution(outputFile);
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

  private static void waterJugsIDLSSolution(PrintStream outputFile) {
    System.out.println("\nWaterAndJugs Iterative DLS Solution");
    try {
      Problem problem = new Problem(initialState, WaterAndJugsFunctionFactory.getActionsFunction(),
          WaterAndJugsFunctionFactory.getResultFunction(), new WaterAndJugsGoalTest());
      SearchForActions search = new IterativeDeepeningSearch();
      SearchAgent agent = new SearchAgent(problem, search);
      printActions(agent.getActions());
      printInstrumentation(agent.getInstrumentation());
      // Outputs solution path to file
			printTitle("\r\nIterative DLS Solution Path\r\n\r\n",outputFile);
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
