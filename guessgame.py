import random
import Tkinter as tk
window = tk.Tk()

maxNO = 10
score = 0
rounds = 0

def buttonClick():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNO:
            result = random.randrange(1, maxNO)
            if guess == result:
                score = score + 1
            rounds = rounds + 1
        else:
            result = "enter not valid"
    except:
        result = "enter not vavid"
    resultLabel.config(text = result)
    scoreLabel.config(text = str(score) + "/" + str(rounds))
    guessBox.delete(0, tk.END)

guessLabel = tk.Label(window, text = "enter a number from 1 to " + str(maxNO))
guessBox = tk.Entry(window)
resultLabel = tk.Label(window)
scoreLabel = tk.Label(window)
button = tk.Button(window, text = "guess", command = buttonClick)
guessLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()

window.mainloop()
