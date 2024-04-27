import java.net.*;
import java.io.*;

class TCPServer {
    public static void main(String[] args){
        try{
            ServerSocket ss = new ServerSocket(9876);
            System.out.println("Connection started, waiting for client");
            while(true){
                Socket soc = ss.accept();
                BufferedReader inFromClient = new BufferedReader(new InputStreamReader(soc.getInputStream()));
                String str = inFromClient.readLine();
                int left = 0;
                int right = str.length() -1;
                String response = "Palindrome";
                while(right>left){
                    if(str.charAt(left)!=str.charAt(right)){
                        response="Not a palindrome";
                        break;
                    }
                    left++;
                    right--;
                }
                DataOutputStream outToClient = new DataOutputStream(soc.getOutputStream());
                outToClient.writeBytes(response+"\n");
            }
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}
