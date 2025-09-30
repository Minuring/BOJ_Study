import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    private static final Scanner sc = new Scanner(System.in);
    private static int N;
    private static double pe;
    private static double pw;
    private static double ps;
    private static double pn;
    private static double sum_of_probabilities;

    public static void main(String[] args) {
        var split = sc.nextLine().split(" ");
        N = Integer.parseInt(split[0]);
        pe = Integer.parseInt(split[1]) * 0.01;
        pw = Integer.parseInt(split[2]) * 0.01;
        ps = Integer.parseInt(split[3]) * 0.01;
        pn = Integer.parseInt(split[4]) * 0.01;

        var now = new Pos(0, 0);
        var visited = new HashSet<Pos>();
        move(0, 1, now, visited);
        System.out.println(sum_of_probabilities);
    }

    private static void move(int movedCount, double probability, Pos now, Set<Pos> visited) {
        if (visited.contains(now)) return;

        if (movedCount == N) {
            sum_of_probabilities += probability;
            return;
        }

        visited.add(now);
        if (pe != 0.0) move(movedCount + 1, probability * pe, new Pos(now.x + 1, now.y), visited);
        if (pw != 0.0) move(movedCount + 1, probability * pw, new Pos(now.x - 1, now.y), visited);
        if (ps != 0.0) move(movedCount + 1, probability * ps, new Pos(now.x, now.y + 1), visited);
        if (pn != 0.0) move(movedCount + 1, probability * pn, new Pos(now.x, now.y - 1), visited);
        visited.remove(now);
    }

    private static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public final boolean equals(Object o) {
            if (!(o instanceof Pos)) {
                return false;
            }
            
            Pos pos = (Pos) o;
            return x == pos.x && y == pos.y;
        }

        @Override
        public int hashCode() {
            int result = x;
            result = 31 * result + y;
            return result;
        }
    }
}
