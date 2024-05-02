print "Enter cost price:\n";
$cp = <STDIN>;

print "Enter selling price:\n";
$sp = <STDIN>;

$change = $sp - $cp;

if($cp>$sp){
	print "Loss is $change\n";
}
elsif($cp<$sp){
	print "profit is $change\n";
}
