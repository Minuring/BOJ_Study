import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] line = scanner.nextLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int B = Integer.parseInt(line[2]);

        int[][] world = new int[N][M];
        int maxHeight = 0;
        for (int i = 0; i < N; i++) {
            String[] split = scanner.nextLine().split(" ");
            world[i] = Arrays.stream(split)
                    .mapToInt(Integer::parseInt)
                    .toArray();
            int maxH = Arrays.stream(world[i]).max().getAsInt();
            maxHeight = Math.max(maxHeight, maxH);
        }

        int minTime = Integer.MAX_VALUE;
        int minTimeHeight = -1;

        for (int h = 0; h <= maxHeight; h++) {
            int time = 0;
            int blocks = B;
            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int diff = Math.abs(h - world[i][j]);
                    if (world[i][j] > h) {
                        time += (diff * 2); // 파내기
                        blocks += diff;
                    }
                    if (world[i][j] < h) {
                        blocks -= diff;
                        time += diff;
                    }
                }
            }

            if (blocks >= 0 && time <= minTime) {
                minTime = time;
                minTimeHeight = h;
            }
        }

        System.out.println(minTime + " " + minTimeHeight);
    }
}
