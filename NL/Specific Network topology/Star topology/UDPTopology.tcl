set ns [new Simulator]
#Create a simulator object

$ns color 2 Green
#Define colour for flow id 2(fid_ 2).

set nf [open UDPTopology.nam w]
$ns namtrace-all $nf
#Opens a trace file for Network Animator (NAM) and sets up NAM tracing.

set np [open UDPTopology.tr w]
$ns trace-all $np
#Opens a trace file for network simulation events.

proc finish {} {
        global ns nf np
        $ns flush-trace
        #Close the NAM trace file
        close $nf
        #Execute NAM on the trace file        
	exec nam UDPTopology.nam &
        exit 0
}
#Defines a procedure called finish to handle finishing the simulation, including closing trace files and executing NAM.

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
#Creates four nodes in the simulation.

#Create links between the nodes
$ns duplex-link $n0 $n2 2Mb 10ms RED
$ns duplex-link $n1 $n2 2Mb 10ms RED
$ns duplex-link $n2 $n3 1.7Mb 20ms RED
#Creates duplex links between the nodes
#Here, $n0, $n1, $n2, $n3 are the 4 nodes, 2Mb, 2b=Mb, 1.7Mb specifies bandwidth, 10ms, 10ms, 20ms specifies delay and RED(Random early detetction) is a queue algorithm.

$ns queue-limit $n2 $n3 8
#Set Queue Size of link (n2-n3) to 8

$ns duplex-link-op $n0 $n2 orient left-up
$ns duplex-link-op $n1 $n2 orient left-down
$ns duplex-link-op $n2 $n3 orient left
#Specifies visual properties of links for NAM, such as orientation and queue position.

$ns duplex-link-op $n2 $n3 queuePos 1.5
#Monitor the queue for link (n2-n3). (for NAM) #0.5 = 45DEG	

set udp [new Agent/UDP]
$ns attach-agent $n1 $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $udp $null
$udp set fid_ 2
#Setup a UDP connection and NULL agents	

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
#Setup a CBR traffic over UDP connection

$cbr set packet_size_ 1000
#setting packet size to 1000

$cbr set rate_ 1mb
#setting bit rate to 1mb

$cbr set random_ false
#setting random false means no noise

$ns at 0.1 "$cbr start"
$ns at 4.5 "$cbr stop"
#Schedule events for the CBR agent
#0.,4.5 are different time intervals for events to happen

$ns at 5.0 "finish"
#Call the finish procedure after 5 seconds of simulation time

$ns run
#Runs the simulation

