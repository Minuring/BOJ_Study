import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int timesum=0;
        double sum=0;
        for(int i=0; i<20; i++){
            String[] line = bf.readLine().split(" ");
            double time = Double.parseDouble(line[1]);
            timesum += time;
            switch(line[2]){
                case "A+": sum += time*4.5; break;
                case "A0": sum += time*4.0; break;
                case "B+": sum += time*3.5; break;
                case "B0": sum += time*3.0; break;
                case "C+": sum += time*2.5; break;
                case "C0": sum += time*2.0; break;
                case "D+": sum += time*1.5; break;
                case "D0": sum += time*1.0; break;
                case "F": break;
                default:
                    timesum -= time;
            }
        }
        bw.write(String.format("%.6f",timesum==0?0:sum/timesum));
        bw.close();
    }
}