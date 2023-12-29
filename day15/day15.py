with open("authcode", "r") as file:
    authcode = file.read().strip().split(",")

print(len(authcode))

def hashmath(word):
    ret = 0
    for char in word:
        ret += ord(char)
        ret = (ret * 17) % 256
    return ret

boxes = [[] for _ in range(256)]
for code in authcode:
    if "-" in code:
        num = hashmath(code.split("-")[0])
        prefix = code.split("-")[0]
        boxes[num] = [val for val in boxes[num] if not val.startswith(prefix)]
    else:
        scode = code.split("=")[0]
        num = hashmath(scode)
        rep = False

        for val in boxes[num]:
            if scode in val:
                boxes[num][boxes[num].index(val)] = code
                rep = True
        if not rep:
            boxes[num].append(code)

ans = 0
for i in range(256):
    if len(boxes[i]) > 0:
        for j in range(len(boxes[i])):
                ans += (i + 1) * (j + 1) * int(boxes[i][j][-1])

print(ans)
