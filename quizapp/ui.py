import tkinter as tk
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:

    def __init__(self, brain: QuizBrain):
        self.brain = brain
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            fill=THEME_COLOR,
            text="Question Text", 
            font=("Arial", 20, "italic")
        )
        
        image_true = tk.PhotoImage(file="images/true.png")
        self.button_true = tk.Button(
            image=image_true, 
            highlightthickness=0,
            command=self.answer_true
        )
        self.button_true.grid(row=2, column=0)
        
        image_false = tk.PhotoImage(file="images/false.png")
        self.button_false = tk.Button(
            image=image_false, 
            highlightthickness=0,
            command=self.answer_false
        )
        self.button_false.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def answer_true(self):
        scored_up = self.brain.check_answer("true")
        self.feedback(scored_up)
        self.disable_buttons()
        self.window.after(1000, self.next)

    def answer_false(self):
        scored_up = self.brain.check_answer("false")
        self.feedback(scored_up)
        self.disable_buttons()
        self.window.after(1000, self.next)

    def next(self):
        self.update_score()
        self.get_next_question()

    def feedback(self, scored_up):
        if scored_up:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.enable_buttons()
        if self.brain.has_more_questions():
            question_text = self.brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            message = f"Your final score was {self.brain.score}/{len(self.brain.questions_list)}"
            messagebox.showinfo(title="Quiz Results", message=message)
            self.disable_buttons()
            self.canvas.itemconfig(self.question_text, text="Quiz Completed!")

    def disable_buttons(self):
        self.button_false.config(state="disabled")
        self.button_true.config(state="disabled")

    def enable_buttons(self):
        self.button_false.config(state="normal")
        self.button_true.config(state="normal")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.brain.score}")
