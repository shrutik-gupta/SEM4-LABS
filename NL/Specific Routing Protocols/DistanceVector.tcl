set ns [new Simulator]

set nf [open DistanceVector.nam w]
$ns namtrace-all $nf

set nr [open DistanceVector.tr w]
$ns trace-all $nr

proc finish {} {
	global ns nf nr
	$ns flush-trace
	close $nf
	exec nam DistanceVector.nam &
	exit 0
}

for {set i 0} {$i < 4} {incr i} {
	set n($i) [$ns node]
}

for {set i 0} {$i<3} {incr i} {
	$ns duplex-link $n($i) $n([expr $i+1]) 2Mb 10ms DropTail
} 
$ns duplex-link $n(3) $n(0) 2Mb 10ms DropTail

set tcp [new Agent/TCP]
$ns attach-agent $n(0) $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n(2) $sink
$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp

$ns rtproto DV
$ns rtmodel-at 2.0 down $n(1) $n(2)
$ns rtmodel-at 3.0 up $n(1) $n(2)

$ns at 1.0 "$ftp start"
$ns at 4.0 "$ftp stop"
$ns at 5.0 "finish"
$ns run
