import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg=THEME_COLOR)
        
        # score label
        self.score_label = tk.Label(
            text="score: 0", 
            font = ("Arial", 20), 
            fg = "white", 
            bg = THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # question area
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, 
            width = 280,
            text="Statrting text", 
            font = ("Arial", 20, "italic"), 
            fill = THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady= 30)

        # False button
        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_btn = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        # True button
        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_btn = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.update_score()
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.q_text)
            
        else: 
            self.update_score()
            percent = (self.quiz.score/self.quiz.question_number)*100
            self.canvas.itemconfig(self.question_text, text=f"No more questions\nYou guessed {percent:.0f}%")

            self.true_btn.config(state = "disabled")
            self.false_btn.config(state = "disabled")

    def true_pressed(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)

    def false_pressed(self):
        is_true = self.quiz.check_answer("Flase")
        self.give_feedback(is_true)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        
    
    def update_score(self):
        self.score_label.config(text=f'score: {self.quiz.score}/{self.quiz.question_number}')
