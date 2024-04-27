import java.net.*;
import java.io.*;

class UDPClient{
    public static void main(String[] args){
        try{
            DatagramSocket soc = new DatagramSocket();

            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(System.in));
            String str = inFromClient.readLine();

            byte[] sendData = new byte[1024];
            sendData = str.getBytes();

            InetAddress IPAddr = InetAddress.getLocalHost();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddr, 8888);
            soc.send(sendPacket);

            byte[] receiveData = new byte[1024];
            DatagramPacket receivePacket= new DatagramPacket(receiveData, receiveData.length);
            soc.receive(receivePacket);

            String outputStr = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("From Server: "+outputStr);

        }catch(Exception e){
            System.out.println(e);
        }
    }   
}
