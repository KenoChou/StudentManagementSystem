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


def shoot():
    bullet = turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.goto(player.xcor(), player.ycor() + 20)
    bullet.dy = 15
    bullets.append(bullet)


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

    x = random.randint(-250, 250)
    enemy.goto(x, 350)

    enemy.dy = random.randint(2, 5)

    enemies.append(enemy)


# ======================
# 移动玩家
# ======================
def move_left():
    x = player.xcor()
    x -= 30

    if x < -270:
        x = -270

    player.setx(x)


def move_right():
    x = player.xcor()
    x += 30

    if x > 270:
        x = 270

    player.setx(x)


# ======================
# 分数
# ======================
score = 0

score_text = turtle.Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(-280, 350)


def update_score():
    score_text.clear()
    score_text.write(
        f"Score: {score}",
        font=("Arial", 18, "normal")
    )


# ======================
# 键盘控制
# ======================
screen.listen()

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")


# ======================
# 碰撞检测
# ======================
def collision(a, b):
    return a.distance(b) < 20


# ======================
# 游戏循环
# ======================
game_over = False

enemy_timer = 0


while not game_over:

    screen.update()

    time.sleep(0.02)


    # 创建敌机
    enemy_timer += 1

    if enemy_timer > 50:
        create_enemy()
        enemy_timer = 0


    # 子弹移动
    for bullet in bullets[:]:

        bullet.sety(
            bullet.ycor() + bullet.dy
        )


        # 删除飞出屏幕子弹
        if bullet.ycor() > 400:
            bullet.hideturtle()
            bullets.remove(bullet)



    # 敌机移动
    for enemy in enemies[:]:

        enemy.sety(
            enemy.ycor() - enemy.dy
        )


        # 敌机撞玩家
        if collision(enemy, player):

            game_over = True


        # 敌机掉落
        if enemy.ycor() < -400:

            enemy.hideturtle()
            enemies.remove(enemy)


    # 子弹击中敌机
    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if collision(bullet, enemy):

                bullet.hideturtle()
                enemy.hideturtle()

                bullets.remove(bullet)
                enemies.remove(enemy)

                score += 10
                update_score()

                break



# ======================
# 游戏结束
# ======================
game_text = turtle.Turtle()
game_text.color("white")
game_text.penup()
game_text.hideturtle()

game_text.write(
    "GAME OVER",
    align="center",
    font=("Arial", 36, "bold")
)


screen.mainloop()