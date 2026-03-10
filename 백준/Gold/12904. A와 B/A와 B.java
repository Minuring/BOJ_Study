import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var s = scanner.nextLine();
        var t = scanner.nextLine();

        backtrack(new StringBuilder(s), t);
        System.out.println(found ? 1 : 0);
    }

    static boolean found = false;

    private static void backtrack(StringBuilder s, String t) {
        if (s.toString().equals(t)) {
            found = true;
            return;
        }

        var v1 = new StringBuilder(s).append('A');
        if (!found && (t.contains(v1) || t.contains(new StringBuilder(v1).reverse()))) {
            backtrack(v1, t);
        }

        var v2 = new StringBuilder(s).reverse().append('B');
        if (!found && (t.contains(v2) || t.contains(new StringBuilder(v2).reverse()))) {
            backtrack(v2, t);
        }
    }
}
