import java.io.*;
import java.util.*;
class Main {

    public static int[][] map;

    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var n = Integer.parseInt(br.readLine());
        map = new int[n][n];

        var k = Integer.parseInt(br.readLine());
        for (int i=0; i<k; i++) {
            var rc = br.readLine().split(" ");
            int r = Integer.parseInt(rc[0]);
            int c = Integer.parseInt(rc[1]);
            map[r-1][c-1] = 1;
        }

        var l = Integer.parseInt(br.readLine());
        
        String[] rotates = new String[10000];
        for (int i=0; i<l; i++) {
            var xd = br.readLine().split(" ");
            int x = Integer.parseInt(xd[0]);
            String d = xd[1].trim();
            rotates[x] = d;
        }

        var snake = new Snake();
        int i = 1;
        for ( ; i < 10000; i++) {
            boolean succeed = snake.move();
            if (!succeed) {
                break;
            }

            if ("L".equals(rotates[i])) {
                snake.rotate("L");
            } else if ("D".equals(rotates[i])) {
                snake.rotate("D");
            }
        }

        System.out.println(i);
    }


    static class Snake {

        public Pos pos = new Pos(0, 0);
        public Direction d = Direction.RIGHT;
        public List<Pos> poses = new ArrayList<>();

        public Snake() {
            poses.add(new Pos(0,0));
        }

        public boolean move() {
            Pos moved = pos.move(d);
            if (moved.isOut()) return false;
            if (poses.contains(moved)) return false;

            if (map[moved.r][moved.c] != 1) {
                poses.remove(0);
            } else {
                map[moved.r][moved.c] = 0;
            }
            pos = moved;
            poses.add(moved);
            return true;
        }

        public void rotate(String direction) {
            if (direction.equals("L")) {
                d = d.rotateLeft();
                return;
            }
            d = d.rotateRight();
        }

        public boolean isOut() {
            return pos.isOut();
        }
    }

    static class Pos {
        public int r = 0;
        public int c = 0;

        public Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public Pos move(Direction d) {
            return new Pos(r + d.dr, c + d.dc);
        }

        public boolean isOut() {
            return r < 0 || c < 0 || r >= map.length || c >= map.length;
        }

        public boolean equals(Object o) {
            if (!(o instanceof Pos)) {
                return false;
            }
            Pos that = (Pos) o;

            return this.r == that.r && this.c == that.c;
        }

        public int hashCode() {
            int result = Objects.hashCode(this.r);
            return 31 * result + Objects.hashCode(this.c);
        }
    }

    enum Direction {
        LEFT(-1, 0),
        RIGHT(1, 0),
        UP(0, -1),
        DOWN(0, 1);

        public final int dc;
        public final int dr;

        Direction(int dc, int dr) {
            this.dc = dc;
            this.dr = dr;
        }

        public Direction rotateLeft() {
            if (this == LEFT) return DOWN;
            if (this == RIGHT) return UP;
            if (this == UP) return LEFT;
            if (this == DOWN) return RIGHT;
            throw new IllegalArgumentException();
        }

        public Direction rotateRight() {
            if (this == LEFT) return UP;
            if (this == RIGHT) return DOWN;
            if (this == UP) return RIGHT;
            if (this == DOWN) return LEFT;
            throw new IllegalArgumentException();
        }
    }
}