print "Enter index till you want fibonacci series: ";
$num=<STDIN>;

$a=0;
$b=1;
print "$a\n";

for ( $i = 2; $i <= $num ; $i++) {
	$temp = $b;
	$b = $a + $b;
	$a = $temp;
	print "$a\n";
}
