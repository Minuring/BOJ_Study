class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[][] delta = new int[][]{{0, 1},{1, 0},{-1, 0},{0, -1}};
        for (int i=0; i<4; i++) {
            int dh = delta[i][0];
            int dw = delta[i][1];
            if(h+dh >= board.length || w+dw >= board.length || h+dh < 0 || w+dw < 0) continue;
            
            if(board[h][w].equals(board[h+dh][w+dw])) answer++;
        }
        
        return answer;
    }
}