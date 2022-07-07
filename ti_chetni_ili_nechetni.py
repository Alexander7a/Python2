a = int(input( proverka chetnosti ))
b = int(input())
c = int(input())
shetchik = 0
if a // 2 == a / 2:
    shetchik = shetchik + 1
if b // 2 == b / 2:
    shetchik = shetchik + 1
if c % 2 == 0:  # proverka chetnosti
    shetchik = shetchik + 1
print(shetchik)