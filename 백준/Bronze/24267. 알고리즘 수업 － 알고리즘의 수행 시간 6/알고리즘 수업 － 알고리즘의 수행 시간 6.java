import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        System.out.printf("%d\n3", (long)n*(n-1)*(n-2)/6);
    }
}