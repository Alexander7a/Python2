num =int(input("vvedi trehznachnoe chislo "))
n = (num % 10 ** 1) // 10 ** 0 # c
n1 = (num % 10 ** 2) // 10 ** 1 # b
n2 = (num % 10 ** 3) // 10 ** 2 # a
if n != n1 and n != n2 and n1 != n2:
    print("razlichni")
else:
    print("ne razlichni")