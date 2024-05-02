print "How many shapes do you want to calculate volume of?\n";
$num = <STDIN>;

for($i=0;$i<$num;$i++){
print "Enter shape:\n1 = cube\n2 = cuboid\n3 = sphere\n";
$shape = <STDIN>;
if($shape==1){
	print "Enter side:\n";
	$side = <STDIN>;
	$volume = $side * $side * $side;
	print "volume of cube is $volume\n";
}
elsif($shape==2){
	print "Enter length:\n";
	$l = <STDIN>;
	print "Enter breadth:\n";
	$b = <STDIN>;
	print "Enter height:\n";
	$h = <STDIN>;
	$volume = $l * $b * $h;
	print "volume of cuboid is $volume\n";
}
elsif($shape==3){
	print "Enter radius:\n";
	$r = <STDIN>;
	$volume = 4/3 * $r * $r * $r * 3.14;
	print "volume of sphere is $volume\n";
}
}
