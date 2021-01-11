package blobs;

import java.util.List;
import java.util.Random;

import aima.core.search.adversarial.AdversarialSearch;
import aima.core.search.adversarial.Game;
import aima.core.search.framework.Metrics;

/**
 * Based upon the following:
 * Artificial Intelligence A Modern Approach (3rd Edition): page 169.<br>
 *
 * <pre>
 * <code>
 * function MINIMAX-DECISION(state) returns an action
 *   return argmax_[a in ACTIONS(s)] MIN-VALUE(RESULT(state, a))
 *
 * function MAX-VALUE(state) returns a utility value
 *   if TERMINAL-TEST(state) then return UTILITY(state)
 *   v = -infinity
 *   for each a in ACTIONS(state) do
 *     v = MAX(v, MIN-VALUE(RESULT(s, a)))
 *   return v
 *
 * function MIN-VALUE(state) returns a utility value
 *   if TERMINAL-TEST(state) then return UTILITY(state)
 *     v = infinity
 *     for each a in ACTIONS(state) do
 *       v  = MIN(v, MAX-VALUE(RESULT(s, a)))
 *   return v
 * </code>
 * </pre>
 *
 * Figure 5.3 An algorithm for calculating minimax decisions. It returns the
 * action corresponding to the best possible move, that is, the move that leads
 * to the outcome with the best utility, under the assumption that the opponent
 * plays to minimize utility. The functions MAX-VALUE and MIN-VALUE go through
 * the whole game tree, all the way to the leaves, to determine the backed-up
 * value of a state. The notation argmax_[a in S] f(a) computes the element a of
 * set S that has the maximum value of f(a).
 *
 *
 * @author Ruediger Lunde
 *
 * @param <STATE>
 *            Type which is used for states in the game.
 * @param <ACTION>
 *            Type which is used for actions in the game.
 * @param <PLAYER>
 *            Type which is used for players in the game.
 */
public class BlobsRandomSearch<STATE, ACTION, PLAYER> implements
		AdversarialSearch<STATE, ACTION> {

	public final static String METRICS_NODES_EXPANDED = "nodesExpanded";

	private Game<STATE, ACTION, PLAYER> game;
	private Metrics metrics = new Metrics();

	/** Creates a new search object for a given game. */
	public static <STATE, ACTION, PLAYER> BlobsRandomSearch<STATE, ACTION, PLAYER> createFor(
			Game<STATE, ACTION, PLAYER> game) {
		return new BlobsRandomSearch<STATE, ACTION, PLAYER>(game);
	}

	public BlobsRandomSearch(Game<STATE, ACTION, PLAYER> game) {
		this.game = game;
	}

	@Override
	public ACTION makeDecision(STATE state) {
		metrics = new Metrics();
		ACTION result = null;
    List<ACTION> playerActions = game.getActions(state);
    Random rand = new Random();
    int randIndex = rand.nextInt(playerActions.size());
		result = playerActions.get(randIndex);
		return result;
	}

	@Override
	public Metrics getMetrics() {
		return metrics;
	}
}
