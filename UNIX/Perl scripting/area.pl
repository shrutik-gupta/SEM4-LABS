print "How many shapes do you want to calculate area of?\n";
$num = <STDIN>;

for($i=0;$i<$num;$i++){
print "Enter shape:\n1 = square\n2 = rectangle\n3 = circle\n";
$shape = <STDIN>;

if($shape==1){
	print "Enter side:\n";
	$side = <STDIN>;
	$area = $side * $side;
	print "Area of square is $area\n";
}
elsif($shape==2){
	print "Enter length:\n";
	$l = <STDIN>;
	print "Enter breadth:\n";
	$b = <STDIN>;
	$area = $l * $b;
	print "Area of rectangle is $area\n";
}
elsif($shape==3){
	print "Enter radius:\n";
	$r = <STDIN>;
	$area = $r * $r * 3.14;
	print "Area of circle is $area\n";
}
}
