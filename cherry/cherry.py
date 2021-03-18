import turtle
import random
import time


# 画樱花的躯干
def tree(branch, t):
    time.sleep(0.0008)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 2)
        else:
            t.color('sienna')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branch - 10 * b, t)
        t.left(40 * a)
        tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


# 掉落的花瓣
def petal(m, t):
    for i in range(m):
        a = 200 - 380 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def write(t):
    t.up()
    t.goto(0, -110)
    t.pencolor('black')
    t.write("Ivy J.\n\n暖春三月，樱花纷纷落落，\n花瓣唱着歌，飘向你心窝。\n愿它的香气能令你的心情快乐，\n愿你拥有樱花般灿烂的生活！^_^",
            font=('华文楷体', 16, 'italic'))


"""
     .Turtle:注意字母的大写,用于生成一个 turtle 对象
     .mainloop:保持画布窗口不消失,用在最后
     .mode:"logo",初始位置指向北（上）;"standard",初始位置指向东方（右）
     .fillcolor:设置要填充的颜色
     .color(p1, p2):p1 画笔整体颜色; p2 由画笔画出的图形的填充颜色
     
     turtle.backward(distance):沿当前反方向,画笔绘制distance距离
     turtle.forward(distance):沿当前方向,画笔绘制distance距离

     turtle.right(degree):顺时针移动degree度
     turtle.left(degree):逆时针移动degree度
     .seth/setheading(angle):设置当前朝向为angle角度,若模式为“logo”,则顺时针旋转;若模式为“standard”,则逆时针旋转
     .heading:返回当前放置的角度
     
     .pu/penup/up:抬笔
     .pd/pendown/down:落笔
     
     .goto/setposition/setpos:移动到相对于画布中心点的坐标位置(x,y),画布是一个以初始位置为原点的坐标系
     .setx/sety:保持一个坐标不变,移到到另一个坐标,移动的距离是相对于原点来计算的
     .xcor/ycor:返回当前箭头所处位置的橫纵坐标
     
     .home:让画笔回到初始位置(原点),同时绘制
     .reset:抹去之前所有的痕迹,重新绘画,恢复箭头的初始状态
     .clear:抹去之前所有的痕迹,但是保持箭头的初始状态
     .circle:一个输入参数时画圆,两个时画弧长,三个参数时画多边形
     .pensize:设置画笔大小
     .speed:设置画笔移动速度,0为最快速度
     .undo:撤销上一次操作
     .write:绘制文本 
     .getscreen:获取画布对象,对画布进行操作
 """
try:
    myWin = turtle.Screen()
    myWin.title("樱花 ^_^")
    myWin.tracer(5, 2)
    # 隐藏画笔
    turtle.hideturtle()
    turtle.setx(-120)
    turtle.left(90)
    # 抹去之前所有的痕迹,但是保持箭头的初始状态
    turtle.clear()
    turtle.up()
    turtle.backward(150)
    turtle.down()
    turtle.color('sienna')
    # 画樱花的躯干
    tree(60, turtle)
    # 掉落的花瓣
    petal(210, turtle)
    # 写字
    write(turtle)
    turtle.done()
except (turtle.Terminator, BaseException):
    pass
