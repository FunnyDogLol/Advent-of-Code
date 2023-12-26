#!/usr/bin/awk -f

{
	valuesnum = split("1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine", numstrings)
	filenumstrings = split($0, strings, "\n")

	for(i = 1; i <= filenumstrings; i++) {
		string = strings[i]
		indexfirst = 0
		indexlast = 0
		stringfirst = ""
		stringlast = ""
		for (j = 1; j <= valuesnum; j++) {
			num = numstrings[j]
			first = index(string, num)
			last = 0
			if (first == 0){
				continue
			}
			if (((first < indexfirst) || (indexfirst == 0))) {
				indexfirst = first
				stringfirst = num
			}

			cur = index(string, num)
			newstr = string
			while (index(newstr, num) > 0) {
				cur = index(newstr, num)
				last = cur
				newstr = substr(newstr, cur + 1)
    			}

			if ((last > indexlast)) {
				indexlast = last
				stringlast = num
			}
			
		}
		print stringfirst  stringlast
	
	}
}
