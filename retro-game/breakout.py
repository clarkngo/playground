import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 20
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_WIDTH = WINDOW_WIDTH // BRICK_COLUMNS
BRICK_HEIGHT = 20

class BreakoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Breakout Game")

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        # Paddle
        self.paddle = self.canvas.create_rectangle(
            (WINDOW_WIDTH - PADDLE_WIDTH) // 2,
            WINDOW_HEIGHT - 40,
            (WINDOW_WIDTH + PADDLE_WIDTH) // 2,
            WINDOW_HEIGHT - 30,
            fill="blue"
        )

        # Ball
        self.ball = self.canvas.create_oval(
            WINDOW_WIDTH // 2 - BALL_SIZE // 2,
            WINDOW_HEIGHT // 2 - BALL_SIZE // 2,
            WINDOW_WIDTH // 2 + BALL_SIZE // 2,
            WINDOW_HEIGHT // 2 + BALL_SIZE // 2,
            fill="white"
        )
        self.ball_dx = 4
        self.ball_dy = -4

        # Bricks
        self.bricks = []
        for row in range(BRICK_ROWS):
            brick_row = []
            for col in range(BRICK_COLUMNS):
                x1 = col * BRICK_WIDTH
                y1 = row * BRICK_HEIGHT
                x2 = x1 + BRICK_WIDTH - 2
                y2 = y1 + BRICK_HEIGHT - 2
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                brick_row.append(brick)
            self.bricks.append(brick_row)

        # Keyboard bindings
        self.root.bind("<Left>", self.move_paddle_left)
        self.root.bind("<Right>", self.move_paddle_right)

        # Start the game loop
        self.game_loop()

    def move_paddle_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
        if self.canvas.coords(self.paddle)[0] < 0:
            self.canvas.coords(self.paddle, 0, self.canvas.coords(self.paddle)[1],
                               PADDLE_WIDTH, self.canvas.coords(self.paddle)[3])

    def move_paddle_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
        if self.canvas.coords(self.paddle)[2] > WINDOW_WIDTH:
            self.canvas.coords(self.paddle, WINDOW_WIDTH - PADDLE_WIDTH, self.canvas.coords(self.paddle)[1],
                               WINDOW_WIDTH, self.canvas.coords(self.paddle)[3])

    def game_loop(self):
        # Move the ball
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        ball_left, ball_top, ball_right, ball_bottom = ball_coords

        # Ball collision with walls
        if ball_left <= 0 or ball_right >= WINDOW_WIDTH:
            self.ball_dx = -self.ball_dx
        if ball_top <= 0:
            self.ball_dy = -self.ball_dy

        # Ball collision with paddle
        paddle_coords = self.canvas.coords(self.paddle)
        if (ball_bottom >= paddle_coords[1] and ball_bottom <= paddle_coords[3] and
            ball_right >= paddle_coords[0] and ball_left <= paddle_coords[2]):
            self.ball_dy = -self.ball_dy

        # Ball collision with bricks
        for row in self.bricks:
            for brick in row:
                if self.canvas.coords(brick):
                    brick_coords = self.canvas.coords(brick)
                    if (ball_right >= brick_coords[0] and ball_left <= brick_coords[2] and
                        ball_bottom >= brick_coords[1] and ball_top <= brick_coords[3]):
                        self.canvas.delete(brick)
                        self.ball_dy = -self.ball_dy

        # Ball falls below the paddle
        if ball_bottom >= WINDOW_HEIGHT:
            self.canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text="Game Over", fill="white", font=("Arial", 24))
            return  # Stop the game loop

        # Continue the game loop
        self.root.after(20, self.game_loop)

# Create the main window
root = tk.Tk()
game = BreakoutGame(root)
root.mainloop()
