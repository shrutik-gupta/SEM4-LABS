import java.net.*;
import java.io.*;

public class TCPServer {
	public static void main(String[] args){
		try{
			ServerSocket ss = new ServerSocket(1234);
			while(true){
				Socket soc = ss.accept();
				BufferedReader inFromServer = new BufferedReader(new InputStreamReader(soc.getInputStream()));
				String str = inFromServer.readLine();
				
				int num = Integer.parseInt(str);
				int fact=1;
				for(int i=1; i<=num;i++){
					fact=fact*i;	
				}
				String result = "Factorial is: "+fact;

				DataOutputStream outToClient= new DataOutputStream(soc.getOutputStream());
				outToClient.writeBytes(result+"\n");
			}	
		} catch(Exception e){
			System.out.println(e);
		}
	
	}
}