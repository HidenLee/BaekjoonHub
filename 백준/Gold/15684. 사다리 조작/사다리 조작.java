import java.util.*;
import java.io.*;
public class Main{
	static int N, M, H;
	static boolean[][] isConnect;
	
	public static void main(String[] args) throws Exception{
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st = new StringTokenizer(br.readLine());
	    N = Integer.parseInt(st.nextToken());
	    M = Integer.parseInt(st.nextToken());
	    H = Integer.parseInt(st.nextToken());
	    isConnect = new boolean[N][H];
	    
	    int a,b;
	    for(int i=0; i<M; i++){
	        st = new StringTokenizer(br.readLine());
	        a = Integer.parseInt(st.nextToken()) - 1;
	        b = Integer.parseInt(st.nextToken()) - 1;
	        isConnect[b][a] = true;
	    }
	    
	    for(int i=0; i<=3; i++){
	        if(comb(0,0,i)){
	            System.out.print(i);
	            return;
	        }
	    }
	    System.out.print(-1);
	}
	
	private static boolean comb(int start, int cnt, int n){
	    if(cnt == n){
	        return isEnd();
	    }
	    for(int i=0; i<N-1; i++){
	        for(int j=0; j<H; j++){
	            if(isConnect[i][j]){
	                continue;
	            }
	            if((i > 0 && isConnect[i-1][j]) || (i<N-2 && isConnect[i+1][j])){
	                continue;
	            }
	            isConnect[i][j] = true;
	            if(comb(i*H+j+1, cnt + 1, n)){
	                return true;
	            }
	            isConnect[i][j] = false;
	        }
	    }
	    return false;
	}
	
	private static boolean isEnd(){
	    int num;
	    for(int i=0; i<N; i++){
	        num = i;
	        for(int j=0; j<H; j++){
	            if(num>0 && isConnect[num-1][j]){
	                num -= 1;
	            }else if(isConnect[num][j]){
	                num += 1;
	            }
	        }
	        if(num != i){
	            return false;
	        }
	    }
	    return true;
	}
}