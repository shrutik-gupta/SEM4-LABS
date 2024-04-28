import java.net.*;
import java.io.*;

class UDPServer{
    public static void main(String[] args){
        try{
            DatagramSocket soc = new DatagramSocket(8901);
            while(true){
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                soc.receive(receivePacket);

                String str = new String(receivePacket.getData(), 0, receivePacket.getLength());
                int count = 0;
                    for(int i=0; i<str.length(); i++){
                        if (str.charAt(i) == 'a' | str.charAt(i) == 'e' | str.charAt(i) == 'i' | str.charAt(i) == 'o' | str.charAt(i) == 'u'){
                            count+=1;
                        }
                    }
                    String result = "total vowels are "+count;

                byte[] sendData = new byte[1024];
                sendData=result.getBytes();
                InetAddress IPAddr = receivePacket.getAddress();
                int port = receivePacket.getPort();

                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddr, port);
                soc.send(sendPacket);
            }

        } catch(Exception e){
            System.out.println(e);
        }
    }
}