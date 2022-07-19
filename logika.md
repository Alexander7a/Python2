# logicheskie operatori
в пайтоне есть 3 вида логических операторов,
с помощью них можно создавать сложные условия
- `and` - logcheskoe umnozhenie, eto kak soius i
- `or` - logicheskoe slozhenie, eto kak ili
- `not` - logicheskoe otritsanie, eto kak net

`age = int(input())
klass = int(input())
if age >= 7 and klass >= 6:
    print("dostup otkrit")
else:
print("dostup zakrit")`

shtobi znachenie virazheniya s operatotom **(and)** 
bilo istinnim, oba usloviya doljni bit istinnimi

`````python
aktiviti = input()
aktiviti2 = input()
if aktiviti == piton or aktiviti2 == book:
    print("molodec")
else:
    print("vse ravno molodec")
`````

`````python
age = int(input())
if not (age < 18): 
    print("dostup est")
else:
    print("dostup poel")
`````
### приорететы логических операторов:
1)not
2)and
3)or