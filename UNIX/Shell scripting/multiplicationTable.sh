echo "Enter a number whose multiplication table you want"
read num

for i in {1..10}
do
	let result=$(echo "$i * $num" | bc)
	echo "$num x $i = $result"
done
