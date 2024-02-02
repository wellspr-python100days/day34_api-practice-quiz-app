from question_model import Question
from quiz_brain import QuizBrain
from data import get_questions
from ui import UI

question_bank = []

questions = get_questions()

for entry in questions:
    text = entry['question']
    answer = entry['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

brain = QuizBrain(question_bank)

ui = UI(brain)

print("You've completed the quiz.")

print(f"Your final score was {brain.score}/{len(brain.questions_list)}")