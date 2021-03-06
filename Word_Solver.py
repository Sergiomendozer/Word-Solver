from tkinter import *
from tkinter import Button
from PIL import ImageTk, Image
import random

# root= tk.Tk()
root = Tk()
root.title("Word Solver")
root.geometry("800x400")
root.configure(bg="#1ceae8")

class Window_Functions:
    # Center's window
    app_width = 800
    app_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (app_width / 2)
    y_coordinate = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x_coordinate)}+{int(y_coordinate)}")


word = "Agent Anger Award Beach Beans Brick Birth Block Bacon Bagel Board Brain Bingo Bread Break Brown Buyer Candy Cause Chain Chair Chest Chief Child China Claim Coast Court Cover Cream Crime Crowd Crown Dirty Daily Dairy Dance Death Depth Draft Dream Demon Devil Drink Drive Earth Enemy Entry Event Faith Fault Field Fight Final Focus Force Frame Frank Front Fruit Grant Group Guide Heart Henry Horse Hotel House Image Index Input Japan Jones Judge Knife Layer Lewis Light Lunch Major March Match Metal Model Money Month Mouth Music Night Noise North Novel Nurse Other Owner Panel Party Phase Phone Piece Pilot Pitch Place Plane Plant Plate Point Pound Power Price Pride Prize Radio Range Ratio Reply Right River Round Route Rugby Scale Scope Score Shape Share Shift Shirt Shock Sight Simon Smile Smith Smoke Sound South Space Spite Sport Squad Stage Start State Steam Steel Stock Stone Store Study Stuff Style Sugar Table  Thing Touch Tower Track Trade Train Trend Trial Trust Truth Uncle Unity Value Video Voice Waste Watch Water While White Whole Woman World Youth Zebra Jumpy Ducks Abort Cable Games Grape Greek Gipsy Holes Habit Miles Maybe Mayor Media Movie Safer Sauce Rocks Raids Risky Under Unzip Vegas"
# makes the list of words into a list
list_of_words = list(word.split(" "))
# picks a random word
chosen_word = random.choice(list_of_words)
print (chosen_word)
wrong_guesses_list = " "
partial_word = "_ _ _ _ _"

def a_new_game():
    global list_of_words, wrong_guesses_list,partial_word,chosen_word
    chosen_word = random.choice(list_of_words)
    print (chosen_word)
    wrong_guesses_list = " "
    partial_word = "_ _ _ _ _"
    congrats.configure(text = "")
    word_to_guess.config(text = partial_word)

def is_word_guessed():
    global wrong_guesses,chosen_word,partial_word
    check = (
        chosen_word[0]
        + " "
        + chosen_word[1]
        + " "
        + chosen_word[2]
        + " "
        + chosen_word[3]
        + " "
        + chosen_word[4]
    )
    if partial_word == check:
       congrats.configure(text = "Congrats you guessed the word!, play a new game",font=("Helvetica", 18),fg = "#B900FF")

def submit ():
    global chosen_word, partial_word,wrong_guesses_list
    guess=str(entry_box.get())
    entry_box.config(text = "")
    entry_box.delete(0, 'end')
    n =wrong_guesses_list.find(guess[0])
    if (
        guess[0] == chosen_word[0]
        or guess[0].upper() == chosen_word[0]
        or guess[0] == chosen_word[0].upper()
    ):
        partial_word = partial_word.split()
        partial_word[0] = chosen_word[0]
        partial_word = " ".join([str(element) for element in partial_word])
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
        is_word_guessed()
    elif (
        guess[0] == chosen_word[1]
        or guess[0].upper() == chosen_word[1]
        or guess[0] == chosen_word[1].upper()
    ):
        partial_word = partial_word.split()
        partial_word[1] = chosen_word[1]
        partial_word = " ".join([str(element) for element in partial_word])
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
        is_word_guessed()
    elif (
        guess[0] == chosen_word[2]
        or guess[0].upper() == chosen_word[2]
        or guess[0] == chosen_word[2].upper()
    ):
        partial_word = partial_word.split()
        partial_word[2] = chosen_word[2]
        partial_word = " ".join([str(element) for element in partial_word])
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
        is_word_guessed()
    elif (
        guess[0] == chosen_word[3]
        or guess[0].upper() == chosen_word[3]
        or guess[0] == chosen_word[3].upper()
    ):
        partial_word = partial_word.split()
        partial_word[3] = chosen_word[3]
        partial_word = " ".join([str(element) for element in partial_word])
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
        is_word_guessed()
    elif (
        guess[0] == chosen_word[4]
        or guess[0].upper() == chosen_word[4]
        or guess[0] == chosen_word[4].upper()
    ):
        partial_word = partial_word.split()
        partial_word[4] = chosen_word[4]
        partial_word = " ".join([str(element) for element in partial_word])
        word_to_guess.config(text = partial_word,font=("Helvetica", 25), justify=CENTER)
        is_word_guessed()
    elif(n == -1):
        wrong_guesses_list = wrong_guesses_list + (guess[0])
        wrong_guess.config(text = "Wrong Guesses:" + wrong_guesses_list, font=("Helvetica", 25),fg = "#FF0101",justify=CENTER)
        is_word_guessed()


#?Front end labels and buttons
wrong_guess = Label(root, text = "Wrong Guesses:" + "", font=("Helvetica", 25),fg = "#FF0101",bg="#1ceae8",justify=CENTER)

word_to_guess= Label(root, text = partial_word,font=("Helvetica", 25),bg="#1ceae8",justify=CENTER)

congrats= Label(root, text = "",font=("Helvetica", 25),bg="#1ceae8", justify=CENTER)

entry_box = Entry(root, text = "", width = 5,font=("Helvetica", 25) )

submit = Button(root, text = "Submit",font=("Helvetica", 18),bg="#B900FF", command=submit )

new_game = Button(root, text = "New Game",font=("Helvetica", 18),bg="#FF0101", command=a_new_game )

# Read the Image
image = Image.open("images/WS_icon_display.png")
# Resize the image using resize() method
resize_image = image.resize((210, 130))# resize(sides, height)
icon = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(image=icon)
label1.image = icon

#positions
label1.pack()
wrong_guess.pack()
word_to_guess.pack()
entry_box.pack()
submit.pack ()
congrats.pack()
new_game.pack()

root.mainloop()