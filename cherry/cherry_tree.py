import random
import turtle


# 在坐标(x,y)处画爱心
def love(x, y):
    lv = turtle.Turtle()
    # 处于复杂图形时,隐藏turtle能明显加快绘制速度
    lv.hideturtle()
    lv.up()
    # 定位到(x,y)
    lv.goto(x, y)

    # 画圆弧
    def curve_move():
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
    lv.speed(6)
    turtle.delay(1)
    lv.pensize(1)
    # 开始画爱心
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(22)
    curve_move()
    lv.left(120)
    curve_move()
    lv.forward(22)
    lv.write("我-你", font=("Arial", 10, "normal"), align="center")
    # 画完复位
    lv.left(140)
    lv.end_fill()


def tree(branch_length, _turtle):
    # 剩余树枝太少要结束递归
    if branch_length > 5:
        # 如果树枝剩余长度较短则变绿
        if branch_length < 20:
            _turtle.color("green")
            _turtle.pensize(random.uniform((branch_length + 5) / 4 - 2, (branch_length + 6) / 4 + 5))
            _turtle.down()
            _turtle.forward(branch_length)
            # 传输现在turtle的坐标
            love(_turtle.xcor(), _turtle.ycor())
            _turtle.up()
            _turtle.backward(branch_length)
            _turtle.color("brown")
            return
        _turtle.pensize(random.uniform((branch_length + 5) / 4 - 2, (branch_length + 6) / 4 + 5))
        _turtle.down()
        _turtle.forward(branch_length)
        # 以下递归
        ang = random.uniform(15, 45)
        _turtle.right(ang)
        # 随机决定减小长度
        tree(branch_length - random.uniform(12, 16), _turtle)
        _turtle.left(2 * ang)
        # 随机决定减小长度
        tree(branch_length - random.uniform(12, 16), _turtle)
        _turtle.right(ang)
        _turtle.up()
        _turtle.backward(branch_length)


# 树下花瓣
def petal(m, _turtle):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        _turtle.up()
        _turtle.forward(b)
        _turtle.left(90)
        _turtle.forward(a)
        _turtle.down()
        _turtle.color("lightcoral")
        _turtle.circle(1)
        _turtle.up()
        _turtle.backward(a)
        _turtle.right(90)
        _turtle.backward(b)


def write_fonts():
    t.penup()
    t.goto(-300, -300)
    t.pencolor('black')
    t.write("纪念相识一个月，余生的快乐希望与你一起！^_^", font=('方正行黑简体', 20, 'normal'))


try:
    myWin = turtle.Screen()
    myWin.title("来自一个喜欢你的小哥哥")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    t.pensize(32)
    t.forward(60)
    tree(100, t)
    # 花瓣往下一点
    t.goto(0, -200)
    petal(200, t)
    # 写字
    write_fonts()
    turtle.done()
except (turtle.Terminator, BaseException):
    pass
