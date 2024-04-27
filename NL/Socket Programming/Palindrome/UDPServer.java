import java.net.*;
import java.io.*;
class UDPServer{
    public static void main(String[] args){
        try{
            DatagramSocket soc= new DatagramSocket(1234);
            while(true){
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                soc.receive(receivePacket);

                String str = new String(receivePacket.getData(), 0, receivePacket.getLength());
                int flag=1;
                int left=0;
                int right= str.length()-1;
                String response;
                while(right>left){
                    if (str.charAt(left)!=str.charAt(right)){
                        flag=0;
                        break;
                    }
                    left++;
                    right--;
                }
                if(flag==0){
                    response = "Not a palindrome";
                }
                else{
                    response = "Palindrome";
                }

                byte[] sendData = new byte[1024];
                sendData = response.getBytes();

                InetAddress IPAddr = receivePacket.getAddress();
                int port = receivePacket.getPort();

                DatagramPacket sendPacket = new DatagramPacket(sendData,sendData.length,IPAddr,port);
                soc.send(sendPacket);
            }
        } catch(Exception e){
            System.out.println(e);
        }
    }
}