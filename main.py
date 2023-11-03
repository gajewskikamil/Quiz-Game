from data import level
from question_model import Question
from quiz_brain import QuizBrain

user_level = ""
while user_level not in level:
    user_level = input("Chose Quiz difficulty (easy, medium, hard)")
question_bank = []
for qa in level[user_level]:
    question_bank.append(Question(qa["question"], qa["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
