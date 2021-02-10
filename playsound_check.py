# from playsound import playsound
# playsound('/Users/alisakolot/Documents/50_pages/day_1/sounds/Basso.wav')

# Import Module
import pygame
import tkinter as tkr

# Create window
player = tkr.Tk()

# Edit Window
player.title("audio")
player.geometry("205x340")

# Get Song
file = "blue_sprinkles.mp3"

# Action Event
def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()

# Register Buttons
button1 = tkr.Button(player, width = 5, height = 3, text = "Play", command=Play)
button1.pack(fill='x')

button2 = tkr.Button(player, width = 5, height = 3, text = "Stop", command=ExitPlayer)
button2.pack(fill='x')

# Song Name
label1 = tkr.LabelFrame(player, text="Song Name")
label1.pack(fill = "both", expand = "yes")
contents1 = tkr.Label(label1, text = file)
contents1.pack()

# Activate
player.mainloop()