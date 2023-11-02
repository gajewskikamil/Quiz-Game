from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qa in question_data:
    question_bank.append(Question(qa["text"], qa["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()

