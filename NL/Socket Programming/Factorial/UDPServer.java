import java.net.*;
import java.io.*;

class UDPServer{
    public static void main(String[] args){
        try{
            DatagramSocket soc = new DatagramSocket(4567);
            while(true){
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                soc.receive(receivePacket);

                String str = new String(receivePacket.getData(), 0, receivePacket.getLength());
                int num = Integer.parseInt(str);
                int fact=1;
                for(int i=1; i<=num;i++){
                    fact = fact*i;
                }
                String result = "factorial is: "+fact;

                byte[] sendData = new byte[1024];
                sendData = result.getBytes();

                InetAddress IPAddr = receivePacket.getAddress();
                int port = receivePacket.getPort();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length,IPAddr,port);
                soc.send(sendPacket);
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }
}
