echo "Choose a shape"
echo "1 = cube"
echo "2 = cuboid"
echo "3 = sphere"
read shape
case $shape in
	2) echo "Enter length, breadth & height:"
	read l
	read b
	let "v=$l * $b *$h"
	echo "volume is $v";;
	1) echo "Enter side:"
	read s
	let "v=$s * $s * $s"
	echo "volume is $v";;
	3) echo "Enter radius:"
	read r
	v=$(echo "scale=2; 4/3*(3.14)*$r*$r*$r"| bc)
	echo "volume is $v";;
	*) echo "Enter a valid shape";;
esac
