import java.net.*;
import java.io.*;

class TCPServer {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(6789);
            System.out.println("Server started, waiting for connections...");
            while (true) {
                Socket soc = ss.accept();
                System.out.println("Connection established...");

                BufferedReader inFromClient = new BufferedReader(new InputStreamReader(soc.getInputStream())); //gets input from client
                String str = inFromClient.readLine(); //reads input from client
 
                DataOutputStream outToClient = new DataOutputStream(soc.getOutputStream()); //sends outpuut to client
                outToClient.writeBytes(str + "\n"); //write output to client
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}

