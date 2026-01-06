import tkinter as tk
import pygame
import random

# Initialize pygame mixer
pygame.mixer.init()

# Load sound
pygame.mixer.music.load("your_song.mp3")  # Replace with your audio file

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
NOTE_SPEED = 5
NOTE_INTERVAL = 800  # milliseconds
KEYS = ["a", "s", "d", "f"]
HIT_LINE_Y = WINDOW_HEIGHT - 50

class RhythmGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rhythm Game")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        # Score and labels
        self.score = 0
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 16), text=f"Score: {self.score}")
        self.feedback_text = self.canvas.create_text(WINDOW_WIDTH//2, HIT_LINE_Y - 30, text="", fill="yellow", font=("Arial", 20))

        # Hit line
        self.canvas.create_line(0, HIT_LINE_Y, WINDOW_WIDTH, HIT_LINE_Y, fill="white", width=2)

        self.notes = []
        self.root.bind("<Key>", self.key_press)

        # Start music
        pygame.mixer.music.play()

        # Start spawning notes
        self.spawn_note()
        self.game_loop()

    def spawn_note(self):
        key = random.choice(KEYS)
        x_pos = KEYS.index(key) * (WINDOW_WIDTH // len(KEYS)) + 50
        note = self.canvas.create_rectangle(x_pos - 20, 0, x_pos + 20, 20, fill="cyan")
        label = self.canvas.create_text(x_pos, 10, text=key.upper(), fill="white", font=("Arial", 12))
        self.notes.append({"id": note, "label": label, "key": key})
        self.root.after(NOTE_INTERVAL, self.spawn_note)

    def key_press(self, event):
        hit = False
        for note in self.notes:
            coords = self.canvas.coords(note["id"])
            if note["key"] == event.char and HIT_LINE_Y - 20 <= coords[1] <= HIT_LINE_Y + 20:
                # Hit effect
                self.canvas.delete(note["id"])
                self.canvas.delete(note["label"])
                self.notes.remove(note)
                self.score += 100
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                self.show_feedback("Perfect!", "green")
                hit = True
                break
        if not hit:
            self.show_feedback("Miss!", "red")

    def show_feedback(self, text, color):
        self.canvas.itemconfig(self.feedback_text, text=text, fill=color)
        # Remove feedback after 300ms
        self.root.after(300, lambda: self.canvas.itemconfig(self.feedback_text, text=""))

    def game_loop(self):
        for note in self.notes:
            self.canvas.move(note["id"], 0, NOTE_SPEED)
            self.canvas.move(note["label"], 0, NOTE_SPEED)
            coords = self.canvas.coords(note["id"])
            if coords[3] >= WINDOW_HEIGHT:
                self.canvas.delete(note["id"])
                self.canvas.delete(note["label"])
                self.notes.remove(note)
                self.show_feedback("Miss!", "red")
        self.root.after(20, self.game_loop)

root = tk.Tk()
game = RhythmGame(root)
root.mainloop()
