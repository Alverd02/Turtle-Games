import turtle
from Score import Score
from Lives import Lives
import pandas

window = turtle.Screen()
window.title("U.S Sates Game")
window.bgpic("blank_states_img.gif")
window.tracer(0)

data = pandas.read_csv("50_states.csv")
states_names = data["state"].to_list()
states_names_lower = [i.lower() for i in states_names]

states_x = data["x"].to_list()
states_y = data["y"].to_list()

score = Score()
lives = Lives()
guessed_states = []

play = True
while play:
    window.update()
    score.write_score()
    if not len(lives.lives) == 0:
        guess_state = window.textinput(title="Guess the State", prompt="What's another state's name?")

    if guess_state.lower() in states_names_lower:
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        guess_index = states_names_lower.index(guess_state.lower())
        name.goto(states_x[guess_index], states_y[guess_index])
        name.write(states_names[guess_index], move=False, align='center', font=('Arial', 8, 'normal'))
        guessed_state = states_names_lower.pop(guess_index)
        states_names.pop(guess_index)
        states_x.pop(guess_index)
        states_y.pop(guess_index)
        guessed_states.append(guessed_state)
        score.score += 1
        score.clear()
        print(score.score)
    elif guess_state.lower() in guessed_states:
        continue

    else:
        if len(lives.lives) != 0:
            lives.fail()
        else:
            score.lose()
            break

    if score.score == 50:
        score.win()
        break

window.exitonclick()