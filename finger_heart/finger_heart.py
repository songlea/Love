import turtle

try:
    # 窗口的大小与标题
    turtle.Screen().setup(width=500, height=400)
    turtle.Screen().title("来自一个喜欢你的小哥哥")

    # 改变重心的位置,使而已更合理
    turtle.goto(-50, 0)
    # 起始的L型轮廓
    turtle.left(90)
    turtle.fd(70)
    turtle.right(180)
    turtle.fd(40)
    # 第一节手指轮廓
    turtle.circle(10, -180)
    turtle.left(180)
    turtle.fd(30)
    turtle.left(180)
    turtle.fd(30)
    # 第二节手指轮廓
    turtle.left(180)
    turtle.circle(10, -180)
    turtle.left(180)
    turtle.fd(30)
    turtle.left(180)
    turtle.fd(30)
    # 第三节手指轮廓
    turtle.right(180)
    turtle.circle(10, -180)
    turtle.left(180)
    turtle.fd(30)
    # 手掌轮廓
    turtle.left(180)
    turtle.circle(40, -180)
    # 食指轮廓
    turtle.left(180)
    turtle.fd(70)
    turtle.left(180)
    turtle.circle(10, -180)
    # 食指指甲轮廓
    turtle.left(90)
    turtle.pu()
    turtle.fd(10)
    turtle.pd()
    turtle.fd(10)
    turtle.left(180)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(10)
    # 移动到食指中间位置准备画大拇指
    turtle.pu()
    turtle.left(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(40)
    turtle.pd()
    # 大拇指轮廓
    turtle.right(90)
    turtle.fd(30)
    turtle.circle(10, 180)
    turtle.fd(30)
    # 移到到食指与大拇指中间准备画心
    turtle.pu()
    turtle.left(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(20)
    # 画心并填充红色
    turtle.right(30)
    turtle.fd(10)
    turtle.left(180)
    turtle.pd()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(5, -180)
    turtle.left(180)
    turtle.circle(5, -180)
    turtle.right(210)
    turtle.fd(20)
    turtle.right(120)
    turtle.fd(20)
    turtle.end_fill()
    # 移到新位置
    turtle.pu()
    turtle.goto(50, 50)
    # 写字
    turtle.write(arg="Ivy J. \n 开心每一天", move=True, font=("宋体", 18, "italic"))
    turtle.bk(5)
    # 画完后不会自动关闭窗口
    turtle.done()
except (turtle.Terminator, BaseException):
    pass
