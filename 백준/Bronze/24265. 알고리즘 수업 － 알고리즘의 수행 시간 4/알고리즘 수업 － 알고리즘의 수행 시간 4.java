import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        long count = 0;
        for (int i = 1; i <= n; i++) {
            count = count + (i - 1);
        }
        System.out.println(count);
        System.out.println(2);
    }
}
