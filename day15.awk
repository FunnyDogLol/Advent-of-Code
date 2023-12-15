#!/usr/bin/awk -f

BEGIN  {
	#create hashmap of ascii characters and their numerical values
	for(n = 0; n < 256; n++) ord[sprintf("%c" , n)] = n
}

#apply hash function to each character and sum them
function hashmath(word) {
	sum = 0
	for(j = 1; j <= length(word); j++){
		char = substr(word, j, 1)
        	char = ord[char]
        	sum += char
		sum = (sum * 17) % 256
	}
	return sum
}

#convert single character to ascii
{
	anssum = 0
	stringnum = split($0, strings, ",")
	for(i = 1; i <= stringnum; i++) {
		anssum += hashmath(strings[i])
	}
	print anssum
}
