import turtle
import random
import time


# =====================
# 初始化窗口
# =====================

screen = turtle.Screen()
screen.setup(600,800)
screen.bgcolor("black")
screen.title("Turtle 飞机大战")

screen.tracer(0)



# =====================
# 玩家飞机
# =====================

player = turtle.Turtle()

player.shape("triangle")
player.color("cyan")

player.penup()

player.goto(0,-300)

player_speed=30



# =====================
# 子弹
# =====================

bullets=[]


def shoot():

    b=turtle.Turtle()

    b.shape("square")
    b.color("yellow")

    b.shapesize(
        0.5,
        0.1
    )

    b.penup()

    b.goto(
        player.xcor(),
        player.ycor()+20
    )


    bullets.append(b)




# =====================
# 敌机
# =====================

enemies=[]


class Enemy:


    def __init__(self):

        self.obj=turtle.Turtle()

        self.obj.shape("square")

        self.obj.color("red")

        self.obj.penup()


        self.obj.goto(

            random.randint(-250,250),

            350

        )


        # 下落速度

        self.speed_y=random.randint(2,5)


        # 横向速度

        self.speed_x=random.choice(
            [-3,-2,-1,1,2,3]
        )



    def move(self):


        x=self.obj.xcor()

        y=self.obj.ycor()


        x+=self.speed_x

        y-=self.speed_y



        # 左右反弹

        if x>270 or x<-270:

            self.speed_x*=-1



        self.obj.goto(
            x,
            y
        )





# =====================
# 玩家移动
# =====================


def left():

    x=player.xcor()-player_speed

    if x>-270:

        player.goto(
            x,
            player.ycor()
        )



def right():

    x=player.xcor()+player_speed

    if x<270:

        player.goto(
            x,
            player.ycor()
        )



screen.listen()

screen.onkeypress(
    left,
    "Left"
)

screen.onkeypress(
    right,
    "Right"
)


screen.onkeypress(
    shoot,
    "space"
)




# =====================
# 分数
# =====================


score=0


score_text=turtle.Turtle()

score_text.color("white")

score_text.penup()

score_text.goto(
    -280,
    350
)

score_text.hideturtle()



def update_score():

    score_text.clear()

    score_text.write(

        f"Score:{score}",

        font=(
            "Arial",
            20,
            "normal"
        )

    )





# =====================
# 游戏循环
# =====================


enemy_timer=0


while True:


    screen.update()



    # 创建敌机

    enemy_timer+=1


    if enemy_timer>40:

        enemies.append(
            Enemy()
        )

        enemy_timer=0




    # 子弹移动

    for b in bullets[:]:

        b.sety(
            b.ycor()+15
        )


        if b.ycor()>400:

            bullets.remove(b)

            b.hideturtle()




    # 敌机移动

    for e in enemies[:]:

        e.move()



        if e.obj.ycor()<-400:

            enemies.remove(e)

            e.obj.hideturtle()




    # 碰撞检测

    for b in bullets[:]:

        for e in enemies[:]:


            if abs(
                b.xcor()-e.obj.xcor()
            )<30 and abs(
                b.ycor()-e.obj.ycor()
            )<30:


                score+=10

                update_score()


                b.hideturtle()

                e.obj.hideturtle()


                bullets.remove(b)

                enemies.remove(e)


                break



    time.sleep(0.02)