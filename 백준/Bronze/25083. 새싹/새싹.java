import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        sb.append("         ,r'\"7\n");
        sb.append("r`-_   ,'  ,/\n");
        sb.append(" \\. \". L_r'\n");
        sb.append("   `~\\/\n");
        sb.append("      |\n");
        sb.append("      |\n");
        bw.write(sb.toString());
        bw.close();
    }
}
