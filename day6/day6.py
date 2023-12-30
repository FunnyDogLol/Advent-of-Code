with open(r"times") as file:
    times = file.readlines()
for i in range(2):
    times[i] = times[i].strip().split()
    times[i].pop(0)

wcount = [0] * len(times[i])
for i, rtime in enumerate(times[0]):
    ptime = 0
    while ptime < int(rtime):
        ptime += 1
        distance = ptime * (int(rtime) - ptime)
        if distance > int(times[1][i]):
            wcount[i] += 1

ans = 1
for n in wcount:
    ans *= n

print(ans)
