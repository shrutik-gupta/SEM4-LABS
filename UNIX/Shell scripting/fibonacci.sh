echo "Enter number of terms in fibonacci series:"
read num

a=0
b=1
i=2

echo "Series is:"
echo "$a"

while [ $i -le $num ]
do
    temp=$b
    b=$((a + b))
    a=$temp
    echo "$a"
    i=$(($i+1))
done

