import turtle
import pandas as pd
import os
import random

screen=turtle.Screen()
screen.title("U.S.Screenshot Game")
image=os.path.join("images","us_map.gif")

screen.addshape(image)
turtle.shape(image)

#def get_mouse_click_coor(x,y):
    #print(x,y)
    
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

state_csv= os.path.join("Resources","us_states.csv")
df= pd.read_csv(state_csv)
all_states=df.States.to_list()

random_num=random.sample(range(len(all_states)),len(all_states))
    
for i in range(len(all_states)):
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(df.iloc[i,2],df.iloc[i,3])
    t.write(str(i+1))

guessed_states=[]

for j in random_num:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct" , prompt=f"what's the number of state {df.iloc[j,0]}")
    if answer_state=="exit".title():
        break

    if int(answer_state)==df.iloc[j,4]:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("white")
        t.goto(df.iloc[j,2]-10,df.iloc[j,3]-10)
        t.write(df.iloc[j,1])




screen.exitonclick()