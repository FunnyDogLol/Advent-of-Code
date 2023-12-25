Command to get the first script to run -

awk -f day1.awk vals2 | awk '{ sum += $1 } END { print sum }' 
For some reason summing the values within the file was broken so I did it with two consecutive awk commands. no clue why it worked that way.

Command for second script to run -

awk -f day1p2.awk vals | awk '{
    gsub(/one/, 1);
    gsub(/two/, 2);
    gsub(/three/, 3);
    gsub(/four/, 4);
    gsub(/five/, 5);
    gsub(/six/, 6);
    gsub(/seven/, 7);
    gsub(/eight/, 8);
    gsub(/nine/, 9);
    print;
}' | awk '{ sum += $1 } END { print sum }'

second script also had issues with printing when it was meant to be saving variables, very odd and super annoying
