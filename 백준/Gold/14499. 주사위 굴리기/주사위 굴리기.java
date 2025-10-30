import java.io.*;
import java.util.*;

class Main {

    static int N,M,X,Y,K;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        // 코드 작성
        var br = new BufferedReader(new InputStreamReader(System.in));
        var s = br.readLine().split(" ");

        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        map = new int[N][M];

        X = Integer.parseInt(s[2]);
        Y = Integer.parseInt(s[3]);
        var dice = new Dice(X, Y);

        K = Integer.parseInt(s[4]);
        for(int i=0; i<N; i++) {
            map[i] = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        }

        int[] cmd = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        for(int i=0; i<K; i++) {
            int d = cmd[i];
            if (d == 1) {
                //east
                dice.rollEast();
            } else if (d == 2) {
                //west
                dice.rollWest();
            } else if (d == 3) {
                //north
                dice.rollNorth();
            } else {
                //south
                dice.rollSouth();
            }
        }
    }

    static class Dice {
        int n, e, w, s, u, d;
        int r, c;

        public Dice(int r, int c) {
            this.r = r;
            this.c = c;
        }

        private void controllMap() {
            if (map[r][c] == 0) {
                map[r][c] = d;
            } else {
                d = map[r][c];
                map[r][c] = 0;
            }
            System.out.println(u);
        }

        public void rollNorth() {
            if (r == 0) return;
            int tmp = n;
            n = u;
            u = s;
            s = d;
            d = tmp;

            r--;
            controllMap();
        }

        public void rollSouth() {
            if (r == N-1) return;
            int tmp = s;
            s = u;
            u = n;
            n = d;
            d = tmp;

            r++;
            controllMap();
        }

        public void rollWest() {
            if (c==0) return;
            int tmp = u;
            u = e;
            e = d;
            d = w;
            w = tmp;

            c--;
            controllMap();
        }

        public void rollEast() {
            if (c==M-1) return;
            int tmp = u;
            u = w;
            w = d;
            d = e;
            e = tmp;

            c++;
            controllMap();
        }
    }
}