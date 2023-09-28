import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[][] array = new char[5][];
        int maxcount=0;
        for(int i=0; i<5; i++){
            String line=br.readLine();
            int length = line.length();
            if(length>maxcount) maxcount=length;
            array[i]= new char[length];
            for(int j=0; j<length; j++){
                array[i][j] = line.charAt(j);
            }
        }
        for(int i=0; i<maxcount; i++){
            for(int j=0; j<5; j++){
                    if(array[j].length>i) bw.write(array[j][i]);
            }
        }
        bw.close();
    }
}
