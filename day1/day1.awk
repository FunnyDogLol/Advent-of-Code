#!/usr/bin/awk -f

{
	ansnum = 0
	filevals = split($0, strings, "\n")
	for(i = 1; i <= filevals; i++) {
		first = ""
		last = ""
		for(j = 1; j <= length(strings[i]); j++){
			char = substr(strings[i], j, 1)
			if (char ~ /^[0-9]+$/) {
				if (first == "") {
					first = char
				}

				last = char
			}
		}
		val = first last
		print val
	}
}
