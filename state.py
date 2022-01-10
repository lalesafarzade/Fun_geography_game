import turtle
import pandas as pd
import os

screen=turtle.Screen()
screen.title("U.S.Screenshot Game")
image=os.path.join("images","map.gif")

screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()







screen.exitonclick()