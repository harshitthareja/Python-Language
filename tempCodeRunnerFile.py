import tkinter as tk
from tkinter import messagebox
class KBCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.geometry("800x600")
        self.root.config(bg="black")

        self.questions = [
            ("What is the capital of France?", "Paris", "London", "Berlin", "Madrid", "A"),
            ("What is 2 + 2?", "3", "4", "5", "6", "B"),
            ("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "B"),
            # Add more questions as needed
        ]

        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 20), bg="black", fg="white", wraplength=700)
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 16), width=20, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=10)
            self.options.append(btn)

        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 16), command=self.next_question)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question[0])
        for i in range(4):
            self.options[i].config(text=question[i+1])

    def check_answer(self, idx):
        correct_answer = self.questions[self.current_question][5]
        selected_answer = chr(ord('A') + idx)
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "That's the correct answer!")
        else:
            messagebox.showinfo("Incorrect", "Sorry, that's the wrong answer.")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Game Over", f"Your final score is: {self.score}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KBCApp(root)
    root.mainloop()