package blobs;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;

import blobs.BlobsState;
import blobs.BlobsAction;
import blobs.BlobsFunctionFactory;

import aima.core.agent.Action;
import aima.core.search.adversarial.Game;
import aima.core.util.datastructure.XYLocation;

/**
 * An implementation of the Blobs game for use with
 * experiments with the Minimax algorithm.
 *
 */
public class BlobsGame implements Game<BlobsState, BlobsAction, String> {

	BlobsState initialState = new BlobsState();

	@Override
	public BlobsState getInitialState() {
		initialState.setBoard();
		System.out.println(initialState.toString());
		return initialState;
	}

	@Override
	public String[] getPlayers() {
		return new String[] { BlobsState.X, BlobsState.O };
	}

	@Override
	public String getPlayer(BlobsState state) {
		return state.getPlayerToMove();
	}

	@Override
	public List<BlobsAction> getActions(BlobsState state) {
		Set<Action> actionSet = BlobsFunctionFactory.getActionsFunction().actions((Object) state);
		List<BlobsAction> retVal = new ArrayList<BlobsAction>();
		for (Action action : actionSet) {
			retVal.add((BlobsAction) action);
		}
		return retVal;
	}

	@Override
	public BlobsState getResult(BlobsState state, BlobsAction action) {
		Object retVal = new BlobsState();
		retVal = BlobsFunctionFactory.getResultFunction().result((Object) state,action);
		return (BlobsState) retVal;

	}

	@Override
	public boolean isTerminal(BlobsState state) {
    boolean retVal = false;
    // true when only available 'Position' is to pass
    // or if two passes have occurred consecutively
    if (state.getUnMarkedPositions().size() == 0 || state.hasDoublePass()) {
      retVal = true;
    }
    return retVal;
	}

	@Override
	public double getUtility(BlobsState state, String player) {
		double result = state.getUtility(player);
		return result;
	}

	public String getWinner(BlobsState state) {
		String currWinner = "";
		if (isTerminal(state)){
			int currMax = 0;
			for (String player : getPlayers()) {
				int numPieces = state.getNumberOf(player);
				if (numPieces > currMax) {
					currMax = numPieces;
					currWinner = player+" wins!";
				} else if (numPieces == currMax) {
					currWinner = "Draw!";
				}
			}
		}
		return currWinner;
	}
}
