import tkinter as tk


class BlindWithGui:
    def __init__(self, solution):
        self.solution = solution

    def execute(self, world, init_x, init_y):
        win = tk.Tk()
        win.title("Blind agent")

        canvas = tk.Canvas(win, width=200, height=200)
        canvas.pack()
        canvas.grid(row=5, column=5)
        # canvas.create_rectangle(50, 25, 150, 75, fill="blue")

        win.mainloop()

        for action in self.solution:
            if action == 'clean':
                world[init_x, init_y] = 'clean'
            if action == 'up':
                init_x -= 1
            if action == 'down':
                init_x += 1
            if action == 'left':
                init_y -= 1
            if action == 'right':
                init_y += 1
