import java.net.*;
import java.io.*;

class UDPClient  {
    public static void main(String[] args){
        try{
            DatagramSocket soc = new DatagramSocket();

            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
            String str = inFromUser.readLine();  //input from user

            byte[] sendData = new byte[1024];
            sendData = str.getBytes();  //converted string to byte for sending
            
            InetAddress IPAddr = InetAddress.getLocalHost();  
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length,IPAddr,9876);
            soc.send(sendPacket);  //sending packet to server

            byte[] receiveData = new byte[1024];
            DatagramPacket receivePacket= new DatagramPacket(receiveData, receiveData.length);  //recieving data from server in bytes
            soc.receive(receivePacket);

            String outputStr = new String(receivePacket.getData(),0,receivePacket.getLength());  //converting recieved bytes to string
            System.out.println("From Server: "+outputStr);

        } catch(Exception e){
            System.out.println(e);
        }
    }
}
