echo Hello World

name="Shrutik"  # No spaces around '='

echo "My name is $name and my age is $age"

host=$(hostname)
echo "My hostname is $host"

echo "Enter your name?"
read yourName
echo "welcome $yourName"
echo "What is your age?"
read age

if [ $age -ge 18 ]
then
	echo "You can vote"
	for i in 1 2 3 4 5
	do
		echo "For tenure $i"
		echo "Choose a party:"
		echo "1 => INC"
		echo "2 => BJP"
		read choice
		case $choice in
			1) echo "voted to INC";;
			2) echo "voted to BJP";;
			*) echo "not a valid party"
		esac
	done
else
	echo "You cannot vote"
fi

count=0
num=10
while [ $count -le $num ]
do
	echo "Numbers are $count"
	let count++
done

#iterate values from a file

name="/home/shrutik/shell/names"

for values in $(cat $name)
do
	echo "Characters of hera pheri are: $values"
done
