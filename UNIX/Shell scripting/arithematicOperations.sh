echo "Enter two numbers:"
read a
read b

echo "What do you want to do"
echo "1 = Addition"
echo "2 = Subtraction"
echo "3 = Multiplication"
echo "4 = Division"
read choice

case $choice in
	1)
	let sum=$(echo "$a+$b"| bc)
	echo "Sum is $sum";;	
	
	2)
	let sub=$(echo "$a-$b"| bc)
	echo "Difference is $sub";;	


	3)
	let mul=$(echo "$a * $b"| bc)
	echo "Product is $mul";;	


	4)
	let div=$(echo "$a / $b"| bc)
	echo "Division is $div";;	
esac
