with open(r"times") as file:
    times = file.readlines()

for i in range(2):
    times[i] = times[i].strip().split()
    times[i].pop(0)
    times[i] = int(''.join(times[i]))

start = False
end = False
j = times[0]
ptime = 0

while ptime < times[0]:
    ptime += 1
    j -= 1
    sdist = ptime * (int(times[0]) - ptime)
    edist = j * (times[1] - j)
    if sdist >= times[1]:
        start = ptime

    if edist >= times[1]:
        end = j

    if start and end:
        print(end - start + 1)
        break
