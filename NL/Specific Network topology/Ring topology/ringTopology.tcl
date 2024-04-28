set ns [new Simulator]
set nf [open ringTopology.nam w]
$ns namtrace-all $nf
set nr [open ringTopology.tr w]
$ns trace-all $nr

proc finish {} {
	global ns nf nr
	$ns flush-trace
	close $nf
	exec nam ringTopology.nam &
	exit 0
}

for {set i 0} {$i < 10} {incr i} {
	set n($i) [$ns node]
}

for {set i 0} {$i < 9} {incr i} {
	$ns duplex-link $n($i) $n([expr $i+1]) 2Mb 10ms DropTail
}

$ns duplex-link $n(9) $n(0) 2Mb 10ms DropTail

set tcp [new Agent/TCP]
$ns attach-agent $n(0) $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n(9) $sink
$ns connect $tcp $sink
$tcp set fid_ 1

set ftp [new Application/FTP]
$ftp attach-agent $tcp 

set udp [new Agent/UDP]
$ns attach-agent $n(2) $udp
set null [new Agent/Null]
$ns attach-agent $n(6) $null
$ns connect $udp $null
$udp set fid_ 2

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packet_size_ 1000
$cbr set rate_ 1Mb

$ns at 0.5 "$cbr start"
$ns at 1.0 "$ftp start"
$ns at 4.0 "$cbr stop"
$ns at 4.5 "$ftp stop"
$ns at 5.0 "finish"
$ns run
