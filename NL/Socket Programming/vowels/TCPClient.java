import java.net.*;
import java.io.*;

class TCPClient{
    public static void main(String[] args){
        try {
            Socket soc = new Socket("localhost",8081);

            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
            String str = inFromUser.readLine();

            DataOutputStream outToServer = new DataOutputStream(soc.getOutputStream());
            outToServer.writeBytes(str+"\n");

            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            String outputStr = inFromServer.readLine();

            System.out.println("From server: "+outputStr);

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}