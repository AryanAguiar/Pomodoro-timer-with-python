import tkinter as tk
from tkinter import messagebox
import pygame

pygame.mixer.init()

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.timer_running = False
        self.work = 25 * 60
        self.break_ = 5 * 60
        self.current_time = self.work
        self.is_work_time = True
        self.main_UI()

    def main_UI(self):
        self.root.title("Pomodoro Timer")
        self.root.geometry("450x200")
        self.root.configure(bg="grey20")
        self.root.resizable(False, False)

        self.time_var = tk.StringVar(value="25:00")

        self.time_label = tk.Label(self.root, textvariable=self.time_var, font=("Arial", 48), fg="white", bg="grey26", highlightthickness=2)
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.root, width=5, text="Start", command=self.start_work, borderwidth=1, font=("Arial", 20), bg="brown2", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=10, pady=20)

        self.break_button = tk.Button(self.root, width=5, text="Break", command=self.start_break, font=("Arial", 20), bg="brown2", fg="white")
        self.break_button.pack(side=tk.RIGHT, padx=10, pady=20)

        self.reset_button = tk.Button(self.root, width=5, text="Reset", command=self.reset_timer, font=("Arial", 20), bg="brown2", fg="white")
        self.reset_button.pack(side=tk.BOTTOM, pady=20)

    def start_work(self):
        if self.timer_running:
            messagebox.showwarning("Timer Running", "There is already a timer running.")

        else:
            self.timer_running = True
            self.is_work_time = True
            self.current_time = self.work
            self.update_timer()

    def start_break(self):
        if self.timer_running:
            messagebox.showwarning("Timer Running", "There is already a timer running.")
        else:
            self.timer_running = True
            self.is_work_time = False
            self.current_time = self.break_
            self.update_timer()

    def reset_timer(self):
        self.timer_running = False
        self.current_time = self.work if self.is_work_time else self.break_
        self.update_timer_display()

    def update_timer(self):
        if self.timer_running:
            minutes, seconds = divmod(self.current_time, 60)
            self.time_var.set(f"{minutes:02d}:{seconds:02d}")

            if self.current_time > 0:
                self.current_time -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.timer_running = False
                self.play_sound()
                if self.is_work_time:
                    messagebox.showinfo("Good Job!", "Work session complete! Click on the break button to start the break timer.")
                else:
                    messagebox.showinfo("Break Over", "Break session complete! Click on the work button to start the work timer.")

    def update_timer_display(self):
        minutes, seconds = divmod(self.current_time, 60)
        self.time_var.set(f"{minutes:02d}:{seconds:02d}")

    def play_sound(self):
        pygame.mixer.music.load("soundtest.mp3")
        pygame.mixer.music.play(loops=0)


if __name__ == "__main__":
    root = tk.Tk()
    timer = Pomodoro(root)
    root.mainloop()