import html

class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        self.current_question = question
        return f"Q.{self.question_number}: {html.unescape(question.text)}"
    
    def get_current_question(self):
        return self.current_question

    def get_current_question_text(self):
        return self.current_question.text

    def get_current_answer(self):
        return self.current_question.answer

    def has_more_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
