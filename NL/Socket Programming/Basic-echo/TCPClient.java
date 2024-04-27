import java.net.*;
import java.io.*;
class TCPClient {
    public static void main(String[] args) {
        try {
            Socket soc = new Socket("localhost", 6789);
            System.out.println("Enter a string: ");
            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));   //takes user input
            //System.in -> reads 1 byte, InputStreamReader -> byte stream to character stream(reads one char at a time), BufferedReader -> reads entire string
            String str = inFromUser.readLine(); //reads the input
            DataOutputStream outToServer = new DataOutputStream(soc.getOutputStream()); //sends user input to server
            outToServer.writeBytes(str+'\n'); //writes user input to server
            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            String outputStr = inFromServer.readLine();
            System.out.println("FROM SERVER: "+outputStr);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
