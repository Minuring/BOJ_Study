import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));

        var board = new int[100][100];

        var count= Integer.parseInt(br.readLine());
        for(int i=0; i<count; i++) {
        	var split = br.readLine().split(" ");
        	var col = Integer.parseInt(split[0]);
        	var row = Integer.parseInt(split[1]);
        	fill(board, col, row);
        }

        var sum = 0;
        for(int i=0; i<100; i++) {
        	for(int j=0; j<100; j++) {
        		sum += board[i][j];
        	}
        }
        System.out.print(sum);
    }

    static void fill(int[][] board, int r, int c) {
    	for(int i=r; i<r+10; i++) {
    		for(int j=c; j<c+10; j++) {
    			board[i][j] = 1;
    		}
    	}
    }
}