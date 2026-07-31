import turtle
import random
import time


# ======================
# 游戏窗口
# ======================
screen = turtle.Screen()
screen.title("Python Turtle 飞机大战")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)


# ======================
# 玩家飞机
# ======================
player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.goto(0, -300)
player.setheading(90)


# ======================
# 子弹
# ======================
bullets = []


score = 0


def create_bullet(x, y, color="yellow", size=1):

    bullet = turtle.Turtle()
    bullet.shape("circle")
    bullet.color(color)
    bullet.shapesize(size, size)
    bullet.penup()
    bullet.speed(0)
    bullet.goto(x, y)

    bullet.dy = 15

    bullets.append(bullet)



# ======================
# 发射系统
# ======================
def shoot():

    global score

    # 500分 激光
    if score >= 500:

        create_bullet(
            player.xcor(),
            player.ycor()+30,
            "cyan",
            0.5
        )


    # 200分 三发
    elif score >= 200:

        create_bullet(
            player.xcor()-20,
            player.ycor()+20
        )

        create_bullet(
            player.xcor(),
            player.ycor()+30
        )

        create_bullet(
            player.xcor()+20,
            player.ycor()+20
        )


    # 100分 双发
    elif score >= 100:

        create_bullet(
            player.xcor()-10,
            player.ycor()+20
        )

        create_bullet(
            player.xcor()+10,
            player.ycor()+20
        )


    # 普通单发
    else:

        create_bullet(
            player.xcor(),
            player.ycor()+20
        )



# ======================
# 敌机
# ======================
enemies = []


def create_enemy():

    enemy = turtle.Turtle()

    enemy.shape("square")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)

    enemy.goto(
        random.randint(-250,250),
        350
    )

    enemy.dy=random.randint(2,5)

    enemies.append(enemy)



# ======================
# 玩家移动
# ======================
def move_left():

    x=player.xcor()-30

    if x<-270:
        x=-270

    player.setx(x)



def move_right():

    x=player.xcor()+30

    if x>270:
        x=270

    player.setx(x)



# ======================
# 分数
# ======================
score_text=turtle.Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(-280,350)



def update_score():

    score_text.clear()

    weapon="单发"

    if score>=100:
        weapon="双发"

    if score>=200:
        weapon="三发"

    if score>=500:
        weapon="激光"

    if score>=1000:
        weapon="自动连射"

    score_text.write(
        f"Score:{score}  Weapon:{weapon}",
        font=("Arial",16,"normal")
    )



update_score()



# ======================
# 键盘
# ======================
screen.listen()

screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right,"Right")
screen.onkeypress(shoot,"space")



# ======================
# 碰撞
# ======================
def collision(a,b):

    return a.distance(b)<20



# ======================
# 游戏循环
# ======================
game_over=False

enemy_timer=0

auto_timer=0


while not game_over:


    screen.update()

    time.sleep(0.02)



    # 自动射击
    if score>=1000:

        auto_timer+=1

        if auto_timer>10:

            shoot()

            auto_timer=0



    # 创建敌机

    enemy_timer+=1

    if enemy_timer>50:

        create_enemy()

        enemy_timer=0



    # 子弹移动

    for bullet in bullets[:]:

        bullet.sety(
            bullet.ycor()+bullet.dy
        )


        if bullet.ycor()>400:

            bullet.hideturtle()

            bullets.remove(bullet)




    # 敌机移动

    for enemy in enemies[:]:

        enemy.sety(
            enemy.ycor()-enemy.dy
        )


        if collision(enemy,player):

            game_over=True



        if enemy.ycor()<-400:

            enemy.hideturtle()

            enemies.remove(enemy)




    # 子弹碰撞

    for bullet in bullets[:]:

        for enemy in enemies[:]:


            if collision(bullet,enemy):

                bullet.hideturtle()

                enemy.hideturtle()


                bullets.remove(bullet)

                enemies.remove(enemy)


                score+=10

                update_score()

                break




# ======================
# 游戏结束
# ======================
game_text=turtle.Turtle()

game_text.color("white")

game_text.penup()

game_text.hideturtle()


game_text.write(
    "GAME OVER",
    align="center",
    font=("Arial",36,"bold")
)


screen.mainloop()