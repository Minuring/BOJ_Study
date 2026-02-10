import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var line = scanner.nextLine();
        for (int i = 0; i < line.length(); i += 10) {
            var end = Math.min(i + 10, line.length());
            var substr = line.substring(i, end);
            System.out.println(substr);
        }
    }
}