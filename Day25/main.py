import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break       
    if answer_state in state_list:
        guessed_states.append(answer_state)
        correct += 1
        t = turtle.Turtle()
        state_location = data[data["state"] == answer_state]
        print(state_location)
        t.penup()
        t.hideturtle()
        t.setposition(int(state_location["x"]), int(state_location["y"]))
        t.write(answer_state)