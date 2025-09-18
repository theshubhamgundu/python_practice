s = input()
r = ""

for ch in s:
    if not (ord(ch) >= 48 and ord(ch) <= 57):   
        r=r + ch

print(r)
