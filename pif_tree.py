from turtle import *
from random import *

hideturtle()
tracer(0)
pu()
goto(0, -300)
pd()
left(90)
thick = 16
pensize(thick)
color('#694612')
speed(1000)

axiom = '22220'
axmtemp = ''
itr = 12
angle = 15
dl = 10
stc = []
transl = {'1': '21', '0': '1[-20]+20'}

for i in range(itr):
    for ch in axiom:
        if ch in transl:
            axmtemp += transl[ch]
        else:
            axmtemp += ch
    axiom = axmtemp
    axmtemp = ''

for ch in axiom:
    if ch == '+':
        right(angle - randint(-13, 13))
    elif ch == '-':
        left(angle - randint(-13, 13))
    elif ch == '0':
        stc.append(pensize())
        pensize(4)
        r = randint(0, 10)
        if r < 3:
            color('#009900')
        elif r > 6:
            color('green')
        else:
            color('#20BB00')
        fd(dl-2)
        pensize(stc.pop())
        color('#694612')
    elif ch == '1':
        if randint(0, 10) > 4:
            fd(dl)
    elif ch == '2':
        if randint(0, 10) > 4:
            fd(dl)
    elif ch == '[':
        thick *= 0.75
        pensize(thick)
        stc.append(thick)
        stc.append(xcor())
        stc.append(ycor())
        stc.append(heading())
    elif ch == ']':
        pu()
        setheading(stc.pop())
        sety(stc.pop())
        setx(stc.pop())
        thick = stc.pop()
        pensize(thick)
        pd()
update()
mainloop()