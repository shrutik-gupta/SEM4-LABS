print "Enter two numbers:'n";
$a = <STDIN>;
$b = <STDIN>;

print "Choose operation:\n1= add\n2=subtract";
$choice = <STDIN>;
if ($choice==1){
	$sum = $a + $b;
	print "$sum\n";
}
elsif ($choice==2){
	$sub = $a - $b;
	print "$sub\n";
}
