import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        var s = new Scanner(System.in).nextLine();
        var n = Integer.parseInt(s);
        var count = n / 5;
        if (n >= 25) count += n / 25;
        if (n >= 125) count += n / 125;
        System.out.println(count);
    }
}
