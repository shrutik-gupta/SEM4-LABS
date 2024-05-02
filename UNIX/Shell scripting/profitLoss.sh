echo "Enter cost price of good: "
read cp
echo "Enter selling price of good: "
read sp

let "change=$sp - $cp"

if [ $cp -gt $sp ]
then
	echo "loss is $change"
else
	echo "profit is $change"
fi
