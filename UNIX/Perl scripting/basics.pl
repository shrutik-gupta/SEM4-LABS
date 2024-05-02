print "Hello World\n";

#scaler

$name="S-h-r-u-t-i-k";
$age="18";

print "your name is $name and your age is  $age\n";

#array

@names=("vikas","shrutik","shriya");
@ages=(50,18,21);

print "$names[0] 's age is $ages[0]\nstored in \$names[0] & \$ages[0]\n";
print "$names[1] 's age is $ages[1]\nstored in \$names[1] & \$ages[1]\n";
print "$names[2] 's age is $ages[2]\nstored in \$names[2] & \$ages[2]\n";
#\ is an escape sequence

#hashes

%emp_data=('shrutik',18,'vikas',50,'shriya',21); #key value pairs

print "\$emp_data{'shrutik'} : $emp_data{'shrutik'}\n";
print "\$emp_data{'vikas'} : $emp_data{'vikas'}\n";
print "\$emp_data{'shriya'} : $emp_data{'shriya'}\n";

#strings

$str="12AB34C";

print ($str * 2,"\n");
print ("t" x 5,"\n");

$str++;
print($str);

#lists

@list = ('ramu',"abdul","jake");

print "\$list[1] = \$list[-3] = $list[-3] \n";
print "\$list[2] = \$list[-2] = $list[-2] \n";
print "\$list[3] = \$list[-1] = $list[-1] \n";

@new_list[0,1] = @list[1,2]; #newlist ke 0 and 1 indexx pe old list ka 1 and 2 index ka vaalues store karo
print "$new_list[0]\n$new_list[1]\n";

@num_list=(1..10);
print(@num_list,"\n");

@num_list1=(4..9,2,13,12);
print(@num_list1,"\n");
@sorted_num_list = sort @num_list1;
print("@sorted_num_list\n"); #" " adds spaces between elements

@str_list=(ab..ag);
print(@str_list,"\n");
@descend_str_list = reverse sort @str_list;
print("@descend_str_list\n");

$joined_str = join(" ","this","is","a","string","made","using","list");
print "$joined_str\n";
$joined_list=join(" ",@num_list,"thanks");
print "$joined_list\n";

@split_array = split(/-/, $name); # - is the character around which split the string, // means split from whereever there is a space
print("@split_array\n");

#conditional statements
if ($age>=18) {
	print "$name can vote\n";
}
elsif ($age<18) {
	print "$name cannot vote\n";
}

$a = 22;
unless ($a<20) {
	print "$a is greater  than 20\n";
}

#loops
for($a=10;$a<20;$a++){
	print "value of a using for loop is $a\n";
}
$b=40;
while($b<50){
	print "value of a using while loop is $b\n";
	$b++;
}

$size= @names;
for($i=0;$i<$size;$i++){
	print "$names[$i]\n";
}
