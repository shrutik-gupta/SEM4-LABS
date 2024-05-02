echo "Enter principal amount:"
read p
echo "Enter time interval:"
read t
echo "Enter rate of interest:"
read r

si=$(echo "scale=2; $p * $r / 100 * $t" | bc)
echo "Simple interest is: $si"

ci=$(echo "scale=2; $p * ((1 + $r / 100) ^ $t) - $p" | bc)
echo "Compound interest is: $ci"
