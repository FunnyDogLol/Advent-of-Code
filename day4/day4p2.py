slines = []
with open("valss", "r") as file:
    slines = file.readlines()

wlines = []
with open("valsw", "r") as file:
    wlines = file.readlines()

for i in range(len(slines)):
    wlines[i] = wlines[i].split()
    slines[i] = slines[i].split()

ans = 0
def findwins(scratch: list, wins: list, num: int) -> list:
    global ans
    ans += 1
    ret = []
    for i in scratch:
        if i in wins:
            num += 1
            ret.append(newnum)

    return ret


def recfunc(scratchlines: list, winlines: list, num: int):
    try:
        for val in findwins(scratchlines[num], winlines[num], num + 1):
            recfunc(scratchlines, winlines, val - 1)
    except:
       pass

    return

for i in range(len(slines)):
    recfunc(slines, wlines, i)

print(ans)
