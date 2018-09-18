/* ComputerMove.java
 * Alex Wolfe
 *
 * Implements AI to play against an opponent at BoardGameOthello.
 */

package computerPlayer;

import BoardGame.BoardGameOthello;
import java.awt.Color;
import java.util.ArrayList;
import java.util.Random;

public class ComputerMove {

    private BoardGameOthello board;
    final static Color P1_COLOR = new Color(222,222,222);
    final static Color P2_COLOR = new Color(24,24,24);

    public ComputerMove(BoardGameOthello boardGame) {
        this.board = boardGame;
    }

    public void test_successor_Fn() {
        ArrayList successors = board.successor_Fn();
        System.out.println("Current board has possible successor moves: ");
        for (int i=0;i<successors.size();i++) {
            BoardGameOthello temp = (BoardGameOthello)successors.get(i);
            System.out.println("   " + temp.getMostRecentMove());
        }
    }

    public void test_minimaxValue() {
        System.out.println("Best move for MAX has value " + maxValue(board));
        System.out.println("Best move for MIN has value " + minValue(board));
    }

    public BoardGameOthello miniMaxDecision() {
        ArrayList successors = board.successor_Fn();
        int value;
        //System.out.println(board.getCurrentColor());
        if (successors.size()==0) {
            System.out.println("This shouldn't happen..");
        }
        if (board.getCurrentColor().equals(P2_COLOR)) {
            BoardGameOthello maxMove = (BoardGameOthello)successors.get(0);
            value = maxValue(maxMove);
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello) successors.get(i);
                if (value<maxValue(temp)) {
                maxMove = temp;
                }
            }
            return maxMove;
        } else {
            BoardGameOthello minMove = (BoardGameOthello)successors.get(0);
            value = minValue(minMove);
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello) successors.get(i);
                if (value>minValue(temp)) {
                    minMove = temp;
                }
            }
            return minMove;
        }
    }

    public boolean cutoffTest(BoardGameOthello state, int depth) {
        if (state.terminalTest() || state.getDepthCounter()==depth){
            return true;
        }

        return false;

    }

    public int maxValue(BoardGameOthello state) {
        int maxValue;
        //System.out.println("state has depth" + state.getDepthCounter() + " board has depth " + board.getDepthCounter());
        if (cutoffTest(state, board.getDepthCounter()+3)) {
            return state.utility();
        } else {
            maxValue = -10000;
            ArrayList successors = state.successor_Fn();
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello)successors.get(i);
                maxValue = Math.max(minValue(temp), maxValue);
            }
            return maxValue;
        }
    }

    public int minValue(BoardGameOthello state) {
        int minValue;
        //System.out.println("checking minvalue of board with depth "+state.getDepthCounter());
        if (cutoffTest(state, board.getDepthCounter()+3)) {
            return state.utility();
        } else {
            minValue = 10000;
            ArrayList successors = state.successor_Fn();
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello)successors.get(i);
                minValue = Math.min(maxValue(temp), minValue);
            }
            return minValue;
        }
    }

    public BoardGameOthello ab_Search() {
        ArrayList successors = board.successor_Fn();
        int value;
        if (board.getCurrentColor().equals(P2_COLOR)) { //Find move for MAX player.
            BoardGameOthello maxMove = (BoardGameOthello)successors.get(0);
            value = ab_maxValue(maxMove, -10000, 10000);
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello) successors.get(i);
                if (value<ab_maxValue(temp, -10000, 10000)) {
                maxMove = temp;
                }
            }
            return maxMove;
        } else { //Find move for MIN player.
            BoardGameOthello minMove = (BoardGameOthello)successors.get(0);
            value = ab_minValue(minMove, -10000, 10000);
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello) successors.get(i);
                if (value>ab_minValue(temp, -10000, 10000)) {
                    minMove = temp;
                }
            }
            return minMove;
        }
    }

    public int ab_maxValue(BoardGameOthello state, int alpha, int beta) {
        int maxValue;
        if (cutoffTest(state, board.getDepthCounter()+3)) {
            return state.utility();
        } else {
            maxValue = -10000;
            ArrayList successors = state.successor_Fn();
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello)successors.get(i);
                maxValue = Math.max(ab_minValue(temp, alpha, beta), maxValue);
                if (maxValue>beta) {
                    return maxValue;
                }
                alpha = Math.max(alpha, maxValue);
            }
            return maxValue;
        }
    }

    public int ab_minValue(BoardGameOthello state, int alpha, int beta) {
        int minValue;
        if (cutoffTest(state, board.getDepthCounter()+3)) {
            return state.utility();
        } else {
            minValue = 10000;
            ArrayList successors = state.successor_Fn();
            for (int i=0; i<successors.size(); i++) {
                BoardGameOthello temp = (BoardGameOthello)successors.get(i);
                minValue = Math.min(ab_maxValue(temp, alpha, beta), minValue);
                if (minValue<alpha) {
                    return minValue;
                }
                beta = Math.min(beta, minValue);
            }
            return minValue;
        }
    }

    public void makeMove(BoardGameOthello newBoard) {
        board.replaceBoard(newBoard);
        board.resetStatusbar();
        if (board.terminalTest()) {
            board.gameOver();
            board.repaint();
        }
    }

    public void makeMove_random() {
        ArrayList successors = board.successor_Fn();
        Random generator = new Random();
        BoardGameOthello randomMove = (BoardGameOthello)successors.get(generator.nextInt(successors.size()));

        makeMove(randomMove);

    }

    public void makeMove_LargestNumberOfDiscs() {
        ArrayList successors = board.successor_Fn();
        BoardGameOthello largestNumBoard = (BoardGameOthello) successors.get(0);
        for (int i=0; i<successors.size(); i++) {
            BoardGameOthello tempBoard = (BoardGameOthello) successors.get(i);
            if (tempBoard.getScoreOfColor(board.getCurrentColor())>largestNumBoard.getScoreOfColor(board.getCurrentColor())) {
                largestNumBoard = tempBoard;
            }
        }

        makeMove(largestNumBoard);

    }

    public void makeMove_using_miniMaxDecision() {
        makeMove(miniMaxDecision());
    }

    public void makeMove_using_ab_Search() {
        makeMove(ab_Search());
    }

}
