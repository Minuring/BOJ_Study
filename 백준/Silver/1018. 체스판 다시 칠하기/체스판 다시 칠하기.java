import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        //단계별_브루트포스_체스판다시칠하기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        char[][] board = new char[N][];
        for(int i=0; i<N; i++){
            board[i] = br.readLine().replaceAll(" ","").toCharArray();
        }
        int min=64;
        for(int i=0; i+7<N; i++){
            for(int j=0; j+7<M; j++){
                int count = count(board,i,j);
                if(count<min) min = count;
            }
        }
        bw.write(Integer.toString(min));
        bw.close();
    }
    public static int count(char[][] table,int row,int col){
        char[][] compB = {{'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'}};
        char[][] compW = {{'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'},
                {'W','B','W','B','W','B','W','B'},
                {'B','W','B','W','B','W','B','W'}};
        int count=0;
        for(int i=0;i<8;i++){
            for(int j=0;j<8;j++){
                if(compB[i][j]!=table[row+i][col+j]) count++;
            }
        }
        int min = count;
        count = 0;
        for(int i=0;i<8;i++){
            for(int j=0;j<8;j++){
                if(compW[i][j]!=table[row+i][col+j]) count++;
            }
        }
        if(min>count) min = count;
        return min;
    }
}
