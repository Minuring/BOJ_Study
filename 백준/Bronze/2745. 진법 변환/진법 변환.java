import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s[] = br.readLine().split(" ");

        byte B=Byte.parseByte(s[1]); //입력 수의 진법
        String number=s[0];

        int res = 0;
        int mul=1;
        for(int i=number.length()-1; i>=0; i--, mul*=B){
            int tmp=0;
            if (Character.isUpperCase(number.charAt(i))) {
                tmp = number.charAt(i)-55;
            }else{
                tmp = number.charAt(i)-48;
            }
            res += tmp*mul;
        }
        bw.write(Integer.toString(res));
        bw.close();
    }
}
