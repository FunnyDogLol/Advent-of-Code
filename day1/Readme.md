Command to get the first script to run -

awk -f day1.awk vals2 | awk '{ sum += $1 } END { print sum }' 
For some reason summing the values within the file was broken so I did it with two consecutive awk commands. no clue why it worked that way.
