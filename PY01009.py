ip = input()
cntH = 0
cntT = 0
for i in ip:
    if i >= "A" and i <= "Z": cntH +=1
    else: cntT += 1

if cntT >= cntH: print(ip.lower())
else: print(ip.upper()) 