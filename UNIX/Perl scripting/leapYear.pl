print "Enter year: ";
$year = <STDIN>;

if ($year % 4 == 0 && $year % 100 != 0){
	print "Leap year\n";
}
else{
	print "Not a leap year\n";
}
