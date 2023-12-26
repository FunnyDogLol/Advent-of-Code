slines = []
with open("valss", "r") as file:
    slines = file.readlines()

wlines = []
with open("valsw", "r") as file:
    wlines = file.readlines()

ans = 0
for i in range(len(slines)):
    count = 0
    wvals = wlines[i].split()
    svals = slines[i].split()
    for sval in svals:
        if sval in wvals:
            count += 1
            for sval2 in svals[svals.index(sval)+1:]:
                if sval2 in wvals:
                    count = count * 2
            ans += count
            break

print(ans)
