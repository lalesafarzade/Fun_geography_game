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

Currect_number=[]
correct_states=[]


for j in random_num:
    answer_state = screen.textinput(title=f"{len(Currect_number)}/50 correct" , prompt=f"What's the number of state {df.iloc[j,0]}")
    if answer_state=="exit":
        Currect_number.append(answer_state)
        correct_states.append(df.iloc[j,0])
        mes_exit=screen.textinput(title=f"{len(Currect_number)}/50 correct" , prompt=f"Do you want a screenshot of your attempt? y/n")
        if mes_exit=="y":
            incorrect_data=[i for i in all_states if i not in correct_states]
            pd.DataFrame(incorrect_data).to_csv("incorrect_state.csv")
        break

    elif answer_state!="exit":
        if int(answer_state)==df.iloc[j,4]:
            Currect_number.append(answer_state)
            correct_states.append(df.iloc[j,0])
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("brown4")
            t.goto(df.iloc[j,2]-10,df.iloc[j,3]-10)
            t.write(df.iloc[j,1])
        
        
if len(Currect_number)==50:
    congrat_=screen.textinput(title=f"{len(Currect_number)}/50 correct" , prompt=f"Congradulation! You nailed it! Do you want to know what state you missed? y/n ")

elif len(Currect_number)>=40:
    congrat_mes=screen.textinput(title=f"{len(Currect_number)}/50 correct" , prompt=f"Congradulation! You almost nailed it! Do you want to know what state you missed?y/n ")
    if congrat_mes=="y":
        incorrect_data=[i for i in all_states if not i in correct_states]
        pd.DataFrame(incorrect_data).to_csv("incorrect_state.csv")

else:
    message_=screen.textinput(title=f"{len(Currect_number)}/50 correct" , prompt=f"You have {len(Currect_number)} correct state ! Do you want to know what state you missed?y/n ")
    if message_=="y":
        incorrect_data=[i for i in all_states if not i in correct_states]
        pd.DataFrame(incorrect_data).to_csv("incorrect_state.csv")



screen.exitonclick()