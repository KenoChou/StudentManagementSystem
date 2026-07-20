import turtle
import time
import random


# ======================
# 游戏参数
# ======================

tizlik = 0.15
utuk = 0
zuigao = 0
oyun = False


# ======================
# 屏幕
# ======================

ekran = turtle.Screen()
ekran.title("🐍 Snake Game")
ekran.bgcolor("#1e272e")
ekran.setup(width=600, height=600)
ekran.tracer(0)



# ======================
# 菜单
# ======================

menu = turtle.Turtle()
menu.hideturtle()
menu.penup()


button = turtle.Turtle()
button.hideturtle()
button.penup()



def draw_box(x, y, w, h, color):

    button.goto(x-w/2, y-h/2)

    button.color(color)

    button.begin_fill()

    for i in range(2):
        button.forward(w)
        button.left(90)
        button.forward(h)
        button.left(90)

    button.end_fill()



def menu_goster():

    menu.clear()
    button.clear()


    menu.color("white")


    # 标题

    menu.goto(0,180)

    menu.write(
        "🐍 SNAKE GAME",
        align="center",
        font=("Arial",36,"bold")
    )


    menu.goto(0,130)

    menu.write(
        "Classic Snake",
        align="center",
        font=("Arial",18,"italic")
    )


    # 开始按钮

    draw_box(
        0,
        40,
        240,
        70,
        "#27ae60"
    )


    menu.goto(0,15)

    menu.write(
        "开始游戏",
        align="center",
        font=("Arial",24,"bold")
    )



    # 分数

    menu.goto(0,-70)

    menu.write(
        "最高分: {}".format(zuigao),
        align="center",
        font=("Arial",20)
    )



    # 操作

    menu.goto(0,-140)

    menu.write(
        "↑ ↓ ← → 控制移动",
        align="center",
        font=("Arial",16)
    )


    menu.goto(0,-180)

    menu.write(
        "吃红色食物增加分数",
        align="center",
        font=("Arial",14)
    )




# ======================
# 蛇头
# ======================

kelle = turtle.Turtle()

kelle.speed(0)

kelle.shape("square")

kelle.color("black")

kelle.penup()

kelle.goto(0,100)

kelle.direction="stop"



# ======================
# 食物
# ======================

awy = turtle.Turtle()

awy.speed(0)

awy.shape("circle")

awy.color("#e74c3c")

awy.penup()

awy.goto(0,0)



# ======================
# 尾巴
# ======================

guyruglar=[]



# ======================
# 分数
# ======================

yaz=turtle.Turtle()

yaz.speed(0)

yaz.color("white")

yaz.penup()

yaz.goto(0,260)

yaz.hideturtle()




# ======================
# 开始游戏
# ======================


def basla(x,y):

    global oyun
    global utuk


    # 点击按钮范围

    if -120 < x < 120 and 0 < y < 80:


        oyun=True

        utuk=0


        menu.clear()
        button.clear()


        kelle.goto(0,100)

        kelle.direction="stop"



        awy.goto(
            random.randint(-250,250),
            random.randint(-250,250)
        )



        yaz.clear()

        yaz.write(
            "分数: 0",
            align="center",
            font=("Arial",24,"bold")
        )



# ======================
# 移动
# ======================


def hereket():

    if kelle.direction=="up":

        kelle.sety(
            kelle.ycor()+20
        )


    if kelle.direction=="down":

        kelle.sety(
            kelle.ycor()-20
        )


    if kelle.direction=="left":

        kelle.setx(
            kelle.xcor()-20
        )


    if kelle.direction=="right":

        kelle.setx(
            kelle.xcor()+20
        )




def goUp():

    if kelle.direction!="down":

        kelle.direction="up"



def goDown():

    if kelle.direction!="up":

        kelle.direction="down"



def goLeft():

    if kelle.direction!="right":

        kelle.direction="left"



def goRight():

    if kelle.direction!="left":

        kelle.direction="right"




ekran.listen()

ekran.onkey(goUp,"Up")

ekran.onkey(goDown,"Down")

ekran.onkey(goLeft,"Left")

ekran.onkey(goRight,"Right")

ekran.onclick(basla)



# 显示菜单

menu_goster()



# ======================
# 游戏循环
# ======================


while True:


    ekran.update()



    if oyun:



        # 撞墙

        if (
            kelle.xcor()>280 or
            kelle.xcor()<-280 or
            kelle.ycor()>280 or
            kelle.ycor()<-280
        ):


            oyun=False


            if utuk > zuigao:

                zuigao=utuk



            for g in guyruglar:

                g.goto(1000,1000)


            guyruglar.clear()


            kelle.goto(0,100)

            kelle.direction="stop"


            yaz.clear()


            menu_goster()



        # 吃食物

        if kelle.distance(awy)<20:


            awy.goto(

                random.randint(-250,250),

                random.randint(-250,250)

            )


            utuk +=10



            yaz.clear()

            yaz.write(

                "分数: {}".format(utuk),

                align="center",

                font=("Arial",24,"bold")

            )



            new=turtle.Turtle()

            new.speed(0)

            new.shape("square")

            new.color("white")

            new.penup()


            guyruglar.append(new)




        # 更新尾巴


        for i in range(len(guyruglar)-1,0,-1):

            x=guyruglar[i-1].xcor()

            y=guyruglar[i-1].ycor()


            guyruglar[i].goto(x,y)



        if len(guyruglar)>0:


            guyruglar[0].goto(

                kelle.xcor(),

                kelle.ycor()

            )



        hereket()


        time.sleep(tizlik)