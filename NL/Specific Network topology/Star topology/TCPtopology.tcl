set ns [new Simulator]
#Create a simulator object

$ns color 1 Cyan
#Define colour for data flow for visualization purposes.

set nf [open TCPtopology.nam w]
$ns namtrace-all $nf
#Opens a trace file for Network Animator (NAM) and sets up NAM tracing.

set np [open TCPtopology.tr w]
$ns trace-all $np
#Opens a trace file for network simulation events.

#Define a 'finish' procedure
proc finish {} {
        global ns nf np
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Execute NAM on the trace file        
	exec nam TCPtopology.nam &
        exit 0
}
#Defines a procedure called finish to handle finishing the simulation, including closing trace files and executing NAM.

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
#Creates four nodes in the simulation.

$ns duplex-link $n0 $n2 2Mb 10ms RED
$ns duplex-link $n1 $n2 2Mb 10ms RED
$ns duplex-link $n2 $n3 1.7Mb 20ms RED
#Creates duplex links between the nodes.
#Here, $n0, $n1, $n2, $n3 are the 4 nodes, 2Mb, 2Mb, 1.7Mb specifies bandwidth, 10ms, 10ms, 20ms specifies delay and RED(Random early detetction) is a queue algorithm.

$ns queue-limit $n2 $n3 8
#Set Queue Size of link (n2-n3) to 8

$ns duplex-link-op $n0 $n2 orient left-up
$ns duplex-link-op $n1 $n2 orient left-down
$ns duplex-link-op $n2 $n3 orient left
#Specifies visual properties of links for NAM, such as orientation and queue position.

$ns duplex-link-op $n2 $n3 queuePos 1.5
#Monitor the queue for link (n2-n3). (for NAM) #0.5 = 45DEG

set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
$ns connect $tcp $sink
$tcp set fid_ 1
#Setup a TCP connection 

set ftp [new Application/FTP]
$ftp attach-agent $tcp
#Setup a FTP traffic over TCP connection

$ns at 1.0 "$ftp start"
$ns at 4.0 "$ftp stop"
#Schedule events for the FTP agent
#1.0, 4.0 are different time intervals for events to happen

$ns at 4.5 "$ns detach-agent $n0 $tcp ; $ns detach-agent $n3 $sink"
#Detach tcp and sink agents

$ns at 5.0 "finish"
#Call the finish procedure after 5 seconds of simulation time

$ns run
#Run the simulation

