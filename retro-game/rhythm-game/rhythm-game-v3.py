import tkinter as tk
import pygame
import random

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("your_song.mp3")  # Replace with your audio file

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
NOTE_SPEED = 5
NOTE_INTERVAL = 800
KEYS = ["a", "s", "d", "f"]
HIT_LINE_Y = WINDOW_HEIGHT - 100
LANE_WIDTH = WINDOW_WIDTH // len(KEYS)
PARTICLE_COUNT = 15

class RhythmGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rhythm Game")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        # Score and feedback
        self.score = 0
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 16), text=f"Score: {self.score}")
        self.feedback_text = self.canvas.create_text(WINDOW_WIDTH//2, HIT_LINE_Y - 40, text="", fill="yellow", font=("Arial", 20))

        # Hit line
        self.canvas.create_line(0, HIT_LINE_Y, WINDOW_WIDTH, HIT_LINE_Y, fill="white", width=2)

        # Bottom labels for lanes
        for i, key in enumerate(KEYS):
            x = i * LANE_WIDTH + LANE_WIDTH // 2
            self.canvas.create_text(x, HIT_LINE_Y + 30, text=key.upper(), fill="white", font=("Arial", 16))

        self.notes = []
        self.particles = []
        self.root.bind("<Key>", self.key_press)

        # Start music
        pygame.mixer.music.play()

        # Start spawning notes
        self.spawn_note()
        self.game_loop()

    def spawn_note(self):
        key = random.choice(KEYS)
        x_pos = KEYS.index(key) * LANE_WIDTH + LANE_WIDTH // 2
        note = self.canvas.create_rectangle(x_pos - 20, 0, x_pos + 20, 20, fill=random.choice(["cyan", "magenta", "yellow"]))
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
                self.create_particles(coords[0]+20, coords[1]+10)
                hit = True
                break
        if not hit:
            self.show_feedback("Miss!", "red")

    def show_feedback(self, text, color):
        self.canvas.itemconfig(self.feedback_text, text=text, fill=color)
        self.root.after(300, lambda: self.canvas.itemconfig(self.feedback_text, text=""))

    def create_particles(self, x, y):
        colors = ["red", "yellow", "cyan", "magenta", "white"]
        for _ in range(PARTICLE_COUNT):
            particle = {
                "x": x,
                "y": y,
                "dx": random.uniform(-3, 3),
                "dy": random.uniform(-3, 0),
                "color": random.choice(colors),
                "id": self.canvas.create_oval(x, y, x+5, y+5, fill=random.choice(colors), outline="")
            }
            self.particles.append(particle)

    def update_particles(self):
        for particle in self.particles[:]:
            particle["x"] += particle["dx"]
            particle["y"] += particle["dy"]
            self.canvas.move(particle["id"], particle["dx"], particle["dy"])
            particle["dy"] += 0.2  # gravity
            if particle["y"] > WINDOW_HEIGHT or particle["x"] < 0 or particle["x"] > WINDOW_WIDTH:
                self.canvas.delete(particle["id"])
                self.particles.remove(particle)

    def game_loop(self):
        # Move notes
        for note in self.notes:
            self.canvas.move(note["id"], 0, NOTE_SPEED)
            self.canvas.move(note["label"], 0, NOTE_SPEED)
            coords = self.canvas.coords(note["id"])
            if coords[3] >= WINDOW_HEIGHT:
                self.canvas.delete(note["id"])
                self.canvas.delete(note["label"])
                self.notes.remove(note)
                self.show_feedback("Miss!", "red")

        # Update particles
        self.update_particles()

        self.root.after(20, self.game_loop)

root = tk.Tk()
game = RhythmGame(root)
root.mainloop()
