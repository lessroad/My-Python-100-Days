import turtle
import random

turtle.pensize(14)
turtle.pensize(3)
turtle.pencolor('black')
for i in range(1,255):
        #turtle.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        #turtle.color(8, 58, 114)
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        turtle.pencolor(r/100, g/100, b/100)
        # 向左转3度
        turtle.circle(i*10)
        turtle.pu()

        turtle.goto(0,-i*10)
        turtle.pd()
        # 向前走
        #turtle.forward(1)

turtle.mainloop()
print("测试")