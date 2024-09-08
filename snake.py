def main():
    import turtle
    import time
    import random
    delay, score, high_score = 0.15, 0, 0
    wn = turtle.Screen()
    
    wn.bgcolor(0, 0, 0)
    wn.title("Snake")
    
    head = turtle.Turtle()
    head.shape('square')
    head.color(1, 1, 1)
    head.penup()
    head.goto(0,0)
    head.direction = 'Stop'
    
    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color(1, 0.3, 0.793)
    food.penup()
    food.goto(0, 100)
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color(1, 1, 1)
    pen.penup()
    pen.hideturtle()
    pen.setpos(0, (wn.window_height()//2)-75)    
    def update_score():
        pen.clear()
        pen.setpos(0, (wn.window_height()//2)-75)
        pen.write("Score : {} \nHigh Score : {} ".format(score, high_score), align="center", font=("times new roman", 18, "bold"))
    update_score()
    def update_food():
        x = random.randint((-(wn.window_width()//2))+75, (wn.window_width()//2)-75)
        y = random.randint((-(wn.window_height()//2))+75, (wn.window_height()//2)-75)
        food.setpos(x, y)
    def group():
        if head.direction != "down":
            head.direction = "up"
    def godown():
        if head.direction != "up":
            head.direction = "down"
    def goleft():
        if head.direction != "right":
            head.direction = "left"
    def goright():
        if head.direction != "left":
            head.direction = "right"
    def move():
        y = head.ycor()
        x = head.xcor()
        if head.direction == "up":
            head.sety(y+20)
        if head.direction == "down":
            head.sety(y-20)
        if head.direction == "left":
            head.setx(x-20)
        if head.direction == "right":
            head.setx(x+20)
    
    wn.listen()
    wn.onkeypress(group, "w")
    wn.onkeypress(godown, "s")
    wn.onkeypress(goleft, "a")
    wn.onkeypress(goright, "d")
    segments = []
    
    while True:
        wn.update()
        if abs(food.xcor()) > ((wn.window_width()/2)-75) or abs(food.ycor()) > ((wn.window_height()/2)-75):
            update_food()
        if abs((wn.window_width()/2)-pen.xcor()) > 90 or abs((wn.window_height()/2)-pen.ycor()) > 90:
            update_score()
        if abs(head.xcor()) > ((wn.window_width()/2)-30) or abs(head.ycor()) > ((wn.window_height()/2)-30):
            time.sleep(1)
            head.setpos(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.setpos(10000, 10000)
            segments.clear()
            score = 0
            delay = 0.1
            update_score()
        if head.distance(food) < 20:
            update_food()
            
            new_segment = turtle.Turtle()
            new_segment.penup()
            new_segment.speed(0)
            new_segment.shape("square")
            colors = [(0,1,0), (1, 0, 0), (0, 0, 1)]
            if len(segments) == 0:
                new_segment.color(random.choice(colors))
            else:
                prev_color = segments[-1].pencolor()
                for color in colors:
                    if color == prev_color:
                        colors.remove(color)
                        break
                new_segment.color(random.choice(colors))
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            update_score()
        
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.setpos(10000, 10000)
                    del segment
                segments.clear()
                delay, score = 0.15, 0
                update_score()
        time.sleep(delay)

if __name__ == '__main__':
    main()