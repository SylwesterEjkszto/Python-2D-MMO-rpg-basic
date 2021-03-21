s = {"chuj":"cipa", "pizda":"chuj"}
s.clear()
d={"frytki":"ziemniaki", "kartofle":"schabowy"}

for key in d:
    s[key] = d[key]
print(s)
print(d)