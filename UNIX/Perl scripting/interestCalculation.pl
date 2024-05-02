print "Enter principal amount:\n";
$p = <STDIN>;

print "Enter time duration:\n";
$t = <STDIN>;

print "Enter rate of interest:\n";
$r = <STDIN>;

$si = $p * $r/100 * $t;
print "Simple interest is $si\n";

$ci =  $p * ((1+$r/100) ** $t) - $p;
print "Compound interest is $ci\n";
