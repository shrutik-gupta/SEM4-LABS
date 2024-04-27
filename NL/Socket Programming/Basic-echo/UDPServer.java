import java.net.*;
import java.io.*;

class UDPServer {
    public static void main(String[] args){
        try{
            DatagramSocket soc = new DatagramSocket(9876);
            while(true){
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                soc.receive(receivePacket);  //receiving packet from client in bytes

                String str = new String(receivePacket.getData(),0, receivePacket.getLength());  //converting received packet in bytes to string
                System.out.println("Recieved: "+str);
                
                byte[] sendData = new byte[1024];
                sendData = str.getBytes();  //converting data to be sent to client in bytes

                InetAddress IPAddr = receivePacket.getAddress();
                int port = receivePacket.getPort();

                DatagramPacket sendPacket = new DatagramPacket(sendData,sendData.length, IPAddr, port); //sending data to client in bytes
                soc.send(sendPacket);
            }
        } catch(Exception e){
            System.out.println(e);
        }
    }    
}
