num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))
num4 = int(input("num4 = "))
if num1 < num2:
    if num1 < num3:
        if num1 < num4:
            print(num1,"samoe malenkoe")
        else:
            print(num4," samoe malenkoe")
    else:
        if num3 < num4:
            print(num3," samoe malenkoe")
        else:
            print(num4, " samoe malenkoe")
else:
    if num2 < num3:
        if num2 < num4:
            print(num2," samoe malenkoe")
        else:
            print(num4, " samoe malenkoe")
    else:
        if num3 < num4:
            print(num3, " samoe malenkoe")
        else:
            print(num4, " samoe malenkoe")
