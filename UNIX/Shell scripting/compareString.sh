echo "Enter string one:"
read str1

echo "Enter string two:"
read str2

if [ $str1 == $str2 ]
then
	echo "strings are same"
else
	echo "strings are different"
fi
