import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        bw.write(Integer.toString((a+b)%c));
        bw.newLine();
        bw.write(Integer.toString(((a%c)+(b%c))%c));
        bw.newLine();
        bw.write(Integer.toString((a*b)%c));
        bw.newLine();
        bw.write(Integer.toString(((a%c)*(b%c))%c));
        bw.newLine();

        bw.close();
    }
}
