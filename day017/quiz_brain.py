class QuizBrain:
    def __init__(self, qusetion_list):
        self.question_number = 0
        self.question_list = qusetion_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_number = self.question_number + 1
        answer = input(f"\nQ.{current_number} {current_question.text} (True/False)?: ").lower()
        self.question_number += 1
        correct_answer = (current_question.answer).lower()
        self.check_answer(answer,correct_answer)
        print(f"Your current score is: {self.score}/{current_number}")
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer.capitalize()}")
        
    def completed(self):
        print()
        print("*" * 50)
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}")
        print("*" * 50)
        print()