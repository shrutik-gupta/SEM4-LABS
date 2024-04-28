import java.net.*;
import java.io.*;

class TCPServer{
    public static void main(String[] args){
        try {
            ServerSocket ss= new ServerSocket(8081);
            while(true){
                Socket soc = ss.accept();

                BufferedReader inFromClient = new BufferedReader(new InputStreamReader(soc.getInputStream()));
                String str = inFromClient.readLine();

                int count = 0;
                for(int i=0; i<str.length(); i++){
                    if (str.charAt(i) == 'a' | str.charAt(i) == 'e' | str.charAt(i) == 'i' | str.charAt(i) == 'o' | str.charAt(i) == 'u'){
                        count+=1;
                    }
                }
                String result = "total vowels are +count;

                DataOutputStream outToClient = new DataOutputStream(soc.getOutputStream());
                outToClient.writeBytes(result+"\n");
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}