import java.net.*;
import java.io.*;
class TCPServer {
    public static void main(String[] args){
        try{
            ServerSocket ss = new ServerSocket(1234);
            while(true){
                Socket soc = ss.accept();

                BufferedReader inFromClient= new BufferedReader(new InputStreamReader(soc.getInputStream()));
                String str = inFromClient.readLine();

                String result = new StringBuilder(str).reverse().toString();

                DataOutputStream outToClient = new DataOutputStream(soc.getOutputStream());
                outToClient.writeBytes(result+"\n");
            }
        } catch(Exception e){
            System.out.println(e);
        }
    }    
}
