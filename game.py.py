import random
from tkinter import *
from tkinter import messagebox

player1 = "X"
player2 = "O"
current_player = player1
move = 0
game_over = False
p1 = 0
p2 = 0


def add_points():
    global p1, p2
    if current_player == player1:
        p1 += 1
    elif current_player == player2:
        p2 += 1


def switch_player(player):
    global current_player
    if player == player1:
        current_player = player2
    elif player == player2:
        current_player = player1


def check_winner():
    global game_over
    if button00["text"] == button01["text"] == button02["text"] == current_player:
        button00.config(bg="green")
        button01.config(bg="green")
        button02.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button10["text"] == button11["text"] == button12["text"] == current_player:
        button10.config(bg="green")
        button11.config(bg="green")
        button12.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button20["text"] == button21["text"] == button22["text"] == current_player:
        button20.config(bg="green")
        button21.config(bg="green")
        button22.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button00["text"] == button10["text"] == button20["text"] == current_player:
        button00.config(bg="green")
        button10.config(bg="green")
        button20.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button01["text"] == button11["text"] == button21["text"] == current_player:
        button01.config(bg="green")
        button11.config(bg="green")
        button21.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button02["text"] == button12["text"] == button22["text"] == current_player:
        button02.config(bg="green")
        button12.config(bg="green")
        button22.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button02["text"] == button11["text"] == button20["text"] == current_player:
        button02.config(bg="green")
        button11.config(bg="green")
        button20.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    if button00["text"] == button11["text"] == button22["text"] == current_player:
        button00.config(bg="green")
        button11.config(bg="green")
        button22.config(bg="green")
        add_points()
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True

    elif move == 9 and game_over == False:
        label1.config(text="Player1:" + str(p1))
        label2.config(text="Player2:" + str(p2))
        game_over = True


def game_ov():
    global game_over

    if game_over:
        reset()


def update_grid(button):
    global move
    if button["text"] == "" and current_player == player1:
        button["text"] = player1
        move += 1
        check_winner()
        game_ov()
        switch_player(current_player)

    elif button["text"] == "" and current_player == player2:
        button["text"] = player2
        move += 1
        check_winner()
        game_ov()
        switch_player(current_player)


def random_move():
    buttons = [button00, button01, button02, button10, button11, button12, button20, button21, button22]
    filled = False

    while not filled:
        randnum = random.randint(0, 8)
        if buttons[randnum]["text"] == "":
            buttons[randnum].config(text=current_player)
            filled = True
            break



def reset():
    global game_over, move

    button00.config(text="", bg="SystemButtonFace")
    button01.config(text="", bg="SystemButtonFace")
    button02.config(text="", bg="SystemButtonFace")

    button10.config(text="", bg="SystemButtonFace")
    button11.config(text="", bg="SystemButtonFace")
    button12.config(text="", bg="SystemButtonFace")

    button20.config(text="", bg="SystemButtonFace")
    button21.config(text="", bg="SystemButtonFace")
    button22.config(text="", bg="SystemButtonFace")

    game_over = False
    move = 0


def main():
    pass

def dummy():
    Label(display, text="Infinite Loop!", font="Arial, 25").grid()


def core():
    global display, button00, button01, button02, button10, button11, button12, button20, button21, button22, label1, label2, move
    display = Tk()
    display.title('Midnight Tic-Tac-Toe')
    display.resizable(False, False)

    menu = Menu(display)
    display.config(menu=menu)
    options = Menu(menu)
    menu.add_cascade(label="Options", menu=options)
    options.add_command(label="Reset", command=reset)
    label1 = Label(display, text="Player1:" + str(p1), font=("Helvetica, 16"))
    label1.grid(row=4, column=0)
    label2 = Label(display, text="Player2:" + str(p2), font=("Helvetica, 16"))
    label2.grid(row=4, column=1)

    button00 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button00))
    button01 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button01))
    button02 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button02))

    button10 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button10))
    button11 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button11))
    button12 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button12))

    button20 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button20))
    button21 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button21))
    button22 = Button(display, text="", font=("Helvetica", 22), width=6, height=3,
                      command=lambda: update_grid(button22))

    button00.grid(row=0, column=0)
    button01.grid(row=0, column=1)
    button02.grid(row=0, column=2)

    button10.grid(row=1, column=0)
    button11.grid(row=1, column=1)
    button12.grid(row=1, column=2)

    button20.grid(row=2, column=0)
    button21.grid(row=2, column=1)
    button22.grid(row=2, column=2)

    for i in range(300):
        random_move()
        move += 1
        check_winner()
        game_ov()
        switch_player(current_player)

    display.mainloop()


core()
# main()

