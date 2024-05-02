echo "Choose a shape"
echo "1 = square"
echo "2 = rectangle"
echo "3 = circle"
read shape
case $shape in
	2) echo "Enter length & breadth:"
	read l
	read b
	let "area=$l * $b"
	echo "Area is $area";;
	1) echo "Enter side:"
	read s
	let "area=$s * $s"
	echo "Area is $area";;
	3) echo "Enter radius:"
	read r
	pi=3.14
	area=$(echo "scale=2; $pi*$r*$r"| bc)
	echo "Area is $area";;
	*) echo "Enter a valid shape";;
esac
