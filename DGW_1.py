#a, b = input().split('\40')
#a = int(a)
#b = int(b)
a = 2
b = 2

def foo_2a():
    print(a>b)
foo_2a()

def foo_3a():
    global c
    if a > b:
        c = 1
    else:
        c = 0
    print(c)
foo_3a()

def foo_3b():
    global max
    if c == 1:
        max = a
    else:
        max = b
    print(max)
foo_3b()

print( max, '>', b) if max==a else print( max, '>', a)

flag = False
def foo_3aNew():
    global c
    if a > b:
        c = 1
    elif a < b:
        c = 0
    else:
        flag = True
    print(c)
    print(flag)
foo_3aNew()

def foo_3bNew():
    global max
    if c == 1:
        max = a
        print(max)
    elif c == 0:
        max = b
        print(max)
    else:
        flag = True
        print('Числа равны')
        print(flag)
    foo_3bNew()