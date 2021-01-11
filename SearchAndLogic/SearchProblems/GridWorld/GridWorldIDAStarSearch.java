import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.util.Comparator;
import java.util.ArrayList;

import gridworld.GridWorldCells;
import gridworld.GridWorldFunctionFactory;
import gridworld.GridWorldGoalTest;

import aima.core.agent.Action;
import aima.core.search.framework.Metrics;
import aima.core.search.framework.Node;
import aima.core.search.framework.NodeExpander;
import aima.core.search.framework.SearchForActions;
import aima.core.search.framework.evalfunc.HeuristicFunction;
import aima.core.search.framework.QueueFactory;
import aima.core.search.framework.SearchForStates;
import aima.core.search.framework.SearchForActions;
import aima.core.search.framework.SearchUtils;
import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.problem.Problem;
import aima.core.search.framework.qsearch.GraphSearch;
import aima.core.search.framework.qsearch.QueueSearch;
import aima.core.util.CancelableThread;
import aima.core.util.datastructure.XYLocation;


public class GridWorldIDAStarSearch {

  static GridWorldCells initialState = new GridWorldCells(new int[] { 0, 2, 0, 0, 0, 0, 1, 0, 0});

  public static void main(String[] args) {

    HeuristicFunction f = new EuclidianHeuristic();
    gridWorldWithIDAStarSearch(f);
  }

  public static void gridWorldWithIDAStarSearch(HeuristicFunction hf) {

    try{
      Problem gridWorldProblem = new Problem(initialState, GridWorldFunctionFactory.getActionsFunction(),
          GridWorldFunctionFactory.getResultFunction(), new GridWorldGoalTest());
      IterativeDeepeningAStarSearch search = new IterativeDeepeningAStarSearch(new GraphSearch(), hf);
      SearchAgent agent = new SearchAgent(gridWorldProblem, search);
      printActions(agent.getActions());
      printInstrumentation(agent.getInstrumentation());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static class EuclidianHeuristic implements HeuristicFunction {
    // evaluates the Euclidean Straight Line Distance between
    // the agent and the goal

    public double h(Object state) {
      GridWorldCells cells = (GridWorldCells) state;
      double retVal = 0;
      retVal += evaluateEuclideanHeuristic(cells);
      return retVal;
    }

    public double evaluateEuclideanHeuristic(GridWorldCells state) {
      double retVal = 0;
      XYLocation agent = state.getLocationOf(1);
      XYLocation goal = state.getLocationOf(2);

      int xDist = Math.abs(agent.getXCoOrdinate() - goal.getXCoOrdinate());
      int yDist = Math.abs(agent.getYCoOrdinate() - goal.getYCoOrdinate());

      double distance = Math.sqrt(Math.pow(xDist,2) + Math.pow(yDist,2));
      retVal = distance;

      return retVal;
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

  public static class DepthLimitAStarSearch implements SearchForActions, SearchForStates {

    private final QueueSearch implementation;
    private final Comparator<Node> comparator;
    private final int limit;
    private final NodeExpander nodeExpander = new NodeExpander();
    private final Metrics metrics = new Metrics();
    private final HeuristicFunction heuristicFunction;

    // Allows an AStar Search to be defined with a given limit of f-cost
    public DepthLimitAStarSearch(QueueSearch impl, HeuristicFunction hf, Integer limit) {
      implementation = impl;
      this.heuristicFunction = hf;
      comparator = createComparator(hf);
      this.limit = limit;
    }

    private static Comparator<Node> createComparator(final HeuristicFunction hf) {
  		return new Comparator<Node>() {
  			public int compare(Node n1, Node n2) {
  				double f1 = hf.h(n1);
  				double f2 = hf.h(n2);
  				return Double.compare(f1, f2);
  			}
  		};
  	}

    @Override
    public List<Action> findActions(Problem p) {
      implementation.getNodeExpander().useParentLinks(true);
      Node node = implementation.findNode(p, QueueFactory.<Node>createPriorityQueue(comparator));
      // if the f value of the evaluated node is greater than the limit, return null node
      if (heuristicFunction.h(node) > limit) {
        return null;
      } else { //else continue as usual
        return node == null ? SearchUtils.failure() : SearchUtils.getSequenceOfActions(node);
      }
    }

    @Override
    public Object findState(Problem p ) {
      implementation.getNodeExpander().useParentLinks(false);
      Node node = implementation.findNode(p, QueueFactory.<Node>createPriorityQueue(comparator));
      // if the f value of the evaluated node is greater than the limit, return null node
      if (heuristicFunction.h(node) > limit) {
        return null;
      } else { // continue as usual
        return node == null ? null : node.getState();
      }
    }

    public Comparator<Node> getComparator() {
      return comparator;
    }


    // @Override
    public void findNode(Problem p ) {
      //private method doing recursive DLS useful here; return cutoff node
      return;
    }

    @Override
    public NodeExpander getNodeExpander() {
      return implementation.getNodeExpander();
    }

    @Override
    public Metrics getMetrics(){
      return implementation.getMetrics();
    }


  }

  public static class IterativeDeepeningAStarSearch implements SearchForActions, SearchForStates {

    private final QueueSearch implementation;
    private final Comparator<Node> comparator;
    private final NodeExpander nodeExpander = new NodeExpander();
    private final Metrics metrics = new Metrics();
    private final HeuristicFunction heuristicFunction;
    private final ArrayList<String> searchTrees = new ArrayList();

    public IterativeDeepeningAStarSearch(QueueSearch impl, HeuristicFunction hf) {
      implementation = impl;
      heuristicFunction = hf;
      comparator = createComparator(hf);
    }

    private static Comparator<Node> createComparator(final HeuristicFunction hf) {
  		return new Comparator<Node>() {
  			public int compare(Node n1, Node n2) {
  				double f1 = hf.h(n1);
  				double f2 = hf.h(n2);
  				return Double.compare(f1, f2);
  			}
  		};
  	}

    @Override
    public List<Action> findActions(Problem p) {
      implementation.getNodeExpander().useParentLinks(true);
      Node node = implementation.findNode(p, QueueFactory.<Node>createPriorityQueue(comparator));
      return node == null ? SearchUtils.failure() : SearchUtils.getSequenceOfActions(node);
    }

    @Override
    public Object findState(Problem p) {
      implementation.getNodeExpander().useParentLinks(false);
      Node node = implementation.findNode(p, QueueFactory.<Node>createPriorityQueue(comparator));
      return node == null ? null : node.getState();
    }

    // @Override
    public Node findNode(Problem p ) {
      // write loop; each iteration creates DepthLimitAStarSearch
      // call its findNode(p)
      // update this' metrics by DepthLimitAStarSearch metrics
      // add it to the search tree
      Node bestNode = null;
      for (int i = 1; i < Integer.MAX_VALUE; i++) {
        try {
          SearchForActions search = new DepthLimitAStarSearch(implementation, heuristicFunction, i);
          SearchAgent agent = new SearchAgent(p, search);
          if (implementation.findNode(p,  QueueFactory.<Node>createPriorityQueue(createComparator(heuristicFunction))) == null) {
            continue;
          } else {
            bestNode = implementation.findNode(p,  QueueFactory.<Node>createPriorityQueue(createComparator(heuristicFunction)));
            searchTrees.addAll(addActions(agent.getActions()));
            break;
          }
        } catch (Exception e) {
          e.printStackTrace();
        }


      }
      return bestNode;
    }

    public List<String> addActions(List<Action> actions) {
      ArrayList<String> retList = new ArrayList<String>();
      for (int i = 0; i < actions.size(); i++) {
  			String action = actions.get(i).toString();
  			retList.add(action);
  		}
      return retList;
    }

    @Override
    public NodeExpander getNodeExpander(){
      return implementation.getNodeExpander();
    }

    // @Override
    public Metrics getMetrics() {
      return implementation.getMetrics();
    }

  }


  public static class TrivialHeuristic implements HeuristicFunction {

    public double h(Object state) {
      GridWorldCells cells = (GridWorldCells) state;
      int retVal = 0;
      retVal += evaluateTrivialHeuristic(cells);
      return retVal;
    }

    public int evaluateTrivialHeuristic(GridWorldCells state) {
      // evaluates the sum of distances in both x and y axes
      // between the agent and the goal

      int retVal = 0;
      XYLocation agent = state.getLocationOf(1);
      XYLocation goal = state.getLocationOf(2);

      int xDist = Math.abs(agent.getXCoOrdinate() - goal.getXCoOrdinate());
      int yDist = Math.abs(agent.getYCoOrdinate() - goal.getYCoOrdinate());

      retVal += xDist + yDist;

      return retVal;

    }
  }


}
