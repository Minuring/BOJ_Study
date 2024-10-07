class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        
        int p = minToSec(pos);
        int opSt = minToSec(op_start);
        int opEnd = minToSec(op_end);
        int videoLen = minToSec(video_len);
        
        if (opSt <= p && opEnd >= p) p = opEnd;
        for (String cmd : commands) {
            if ("prev".equals(cmd)){
                p = p >= 10 ? p-10 : 0;
            }else{
                p = (videoLen-p) >= 10 ? p+10 : videoLen;
            }
            
            if (opSt <= p && opEnd >= p) p = opEnd;
        }
        
        String answer = String.format("%02d:%02d", p/60, p%60);
        return answer;
    }
    
    private int minToSec(String mmss){
        String[] ms = mmss.split(":");
        int result = 0;
        result += 60*Integer.parseInt(ms[0]);
        result += Integer.parseInt(ms[1]);
        return result;
    }
}