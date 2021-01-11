package blobs;

import java.util.List;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Set;

import blobs.BlobsState;
import blobs.BlobsAction;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ActionsFunction;
import aima.core.search.framework.problem.ResultFunction;
import aima.core.util.datastructure.XYLocation;

/**
 */
public class BlobsFunctionFactory {
	private static ActionsFunction _actionsFunction = null;
	private static ResultFunction _resultFunction = null;

	public static ActionsFunction getActionsFunction() {
		if (null == _actionsFunction) {
			_actionsFunction = new BActionsFunction();
		}
		return _actionsFunction;
	}

	public static ResultFunction getResultFunction() {
		if (null == _resultFunction) {
			_resultFunction = new BResultFunction();
		}
		return _resultFunction;
	}

	private static class BActionsFunction implements ActionsFunction {
		public Set<Action> actions(Object state) {
			BlobsState board = (BlobsState) state;

			Set<Action> retVal = new LinkedHashSet<Action>();

      // Adds pass action
  		BlobsState newBoard = board.clone();
      newBoard.pass();
  		retVal.add(new BlobsAction(BlobsAction.PASS, new XYLocation(-1,-1), "\n"+toString()));
  		// Gets open spaces and player pieces
  		List<XYLocation> openSpaces = board.getUnMarkedPositions();
  		List<XYLocation> playerPieces = board.getPlayerPieces(board.getPlayerToMove());
  		// Adds 'place' moves
  		for (XYLocation place : openSpaces) {
  			if (board.isAdjacent(place,board.getPlayerToMove())) {
					newBoard = board.clone();
          newBoard.place(place);
  				retVal.add(new BlobsAction(BlobsAction.PLACE, place, "\n"+newBoard.toString()));
  			}
  		}
      // Adds 'move' and 'jump' moves
      for (XYLocation piece : playerPieces) {
        // Considers spaces adjacent to pieces
        for (int i = -1 ; i <= 1; i++) {
          for (int j = -1 ; j <= 1; j++) {
            //Considers 'move' actions
            XYLocation moveTo = null;
            int moveToX = piece.getXCoOrdinate()+i;
            int moveToY = piece.getYCoOrdinate()+j;
            if ((0<=moveToX) && (moveToX<board.getNSquares()) &&
        				(0<=moveToY) && (moveToY<board.getNSquares())) {
                  moveTo = new XYLocation(piece.getXCoOrdinate()+i,piece.getYCoOrdinate()+j);
                } else {
                  continue;
                }
            String moveType = " ";
            // if (board.isEmpty(moveTo)) {
            if (openSpaces.contains(moveTo)){
              switch (i) {
                case (-1):
                  switch(j) {
                    case(-1):
                      moveType = BlobsAction.MOVEUPLEFT;
                      break;
                    case(0):
                      moveType = BlobsAction.MOVELEFT;
                      break;
                    case(1):
                      moveType = BlobsAction.MOVEDOWNLEFT;
                      break;
                  }
                case(0):
                  switch(j){
                    case(-1):
                      moveType = BlobsAction.MOVEUP;
                      break;
                    case(0):
                      continue;
                    case(1):
                      moveType = BlobsAction.MOVEDOWN;
                      break;
                  }
                case(1):
                  switch(j){
                    case(-1):
                      continue;
                      // moveType = BlobsAction.MOVEUPRIGHT;
                      // break;
                    case(0):
                      moveType = BlobsAction.MOVERIGHT;
                      break;
                    case(1):
                      continue;
                      // moveType = BlobsAction.MOVEDOWNRIGHT;
                      // break;
                  }
              }
							newBoard = board.clone();
              newBoard.move(piece,moveTo);
              retVal.add(new BlobsAction(moveType,piece,"\n"+newBoard.toString()));
            } else if (!(board.getValue(moveTo) == board.getPlayerToMove())){
              // Considers 'jump' actions
              XYLocation jumpTo = new XYLocation(piece.getXCoOrdinate()+(2*i),piece.getYCoOrdinate()+(2*j));
              String jumpType = "";
              if (board.isEmpty(jumpTo)) {
                switch (i) {
                  case (-1):
                    switch(j) {
                      case(-1):
                        moveType = BlobsAction.JUMPUPLEFT;
                        break;
                      case(0):
                        moveType = BlobsAction.JUMPLEFT;
                        break;
                      case(1):
                        moveType = BlobsAction.JUMPDOWNLEFT;
                        break;
                    }
                  case(0):
                    switch(j){
                      case(-1):
                        moveType = BlobsAction.JUMPUP;
                        break;
                      case(0):
                        continue;
                      case(1):
                        moveType = BlobsAction.JUMPDOWN;
                        break;
                    }
                  case(1):
                    switch(j){
                      case(-1):
                        continue;
                        // moveType = BlobsAction.JUMPUPRIGHT;
                        // break;
                      case(0):
                        moveType = BlobsAction.JUMPRIGHT;
                        break;
                      case(1):
                        continue;
                        // moveType = BlobsAction.JUMPDOWNRIGHT;
                        // break;
                    }
                }
                // Adds valid jumps to list
								newBoard = board.clone();
                newBoard.move(piece,jumpTo);
                retVal.add(new BlobsAction(moveType,piece,"\r\n"+newBoard.toString()));
              } else {
                continue;
              }
            } else {
              continue;
            }
          }
        }
      }
      return retVal;
    }
  }

	private static class BResultFunction implements ResultFunction {
    // returns the state of the board after taking an action
		public Object result(Object s, Action a) {

			BlobsAction action = (BlobsAction) a;
      String actionType = action.getName();
      XYLocation piece = (XYLocation) action.getAttribute(BlobsAction.POSITION);
      XYLocation moveTo = new XYLocation(-1,-1);

			BlobsState board = (BlobsState) s;
      BlobsState newBoard = board.clone();

      switch (actionType) {
        case BlobsAction.PASS:
          newBoard.pass();
          return newBoard;
        case BlobsAction.PLACE:
          newBoard.place(piece);
          return newBoard;
        case BlobsAction.MOVEUPLEFT:
          moveTo = new XYLocation(piece.getXCoOrdinate()-1, piece.getYCoOrdinate()-1);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVEUP:
          moveTo = new XYLocation(piece.getXCoOrdinate(), piece.getYCoOrdinate()-1);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVEUPRIGHT:
          moveTo = new XYLocation(piece.getXCoOrdinate()+1, piece.getYCoOrdinate()-1);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVELEFT:
          moveTo = new XYLocation(piece.getXCoOrdinate()-1, piece.getYCoOrdinate());
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVERIGHT:
          moveTo = new XYLocation(piece.getXCoOrdinate()+1, piece.getYCoOrdinate());
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVEDOWNLEFT:
          moveTo = new XYLocation(piece.getXCoOrdinate()-1, piece.getYCoOrdinate()+1);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVEDOWN:
          moveTo = new XYLocation(piece.getXCoOrdinate(), piece.getYCoOrdinate()+1);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.MOVEDOWNRIGHT:
          moveTo = new XYLocation(piece.getXCoOrdinate()+1, piece.getYCoOrdinate()+1);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPUPLEFT:
          moveTo = new XYLocation(piece.getXCoOrdinate()-2, piece.getYCoOrdinate()-2);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPUP:
          moveTo = new XYLocation(piece.getXCoOrdinate(), piece.getYCoOrdinate()-2);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPUPRIGHT:
          moveTo = new XYLocation(piece.getXCoOrdinate()+2, piece.getYCoOrdinate()-2);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPLEFT:
          moveTo = new XYLocation(piece.getXCoOrdinate()-2, piece.getYCoOrdinate());
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPRIGHT:
          moveTo = new XYLocation(piece.getXCoOrdinate()+2, piece.getYCoOrdinate());
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPDOWNLEFT:
          moveTo = new XYLocation(piece.getXCoOrdinate()-2, piece.getYCoOrdinate()+2);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPDOWN:
          moveTo = new XYLocation(piece.getXCoOrdinate(), piece.getYCoOrdinate()+2);
          newBoard.move(piece,moveTo);
          return newBoard;
        case BlobsAction.JUMPDOWNRIGHT:
          moveTo = new XYLocation(piece.getXCoOrdinate()+2, piece.getYCoOrdinate()+2);
          newBoard.move(piece,moveTo);
          return newBoard;
        }

			// The Action is not understood or is a NoOp
			// the result will be the current state.
			return newBoard;
		}
	}
}
