class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        num = self.question_number
        self.question_number += 1
        return input(f"Q{num + 1}: {self.question_list[num].text} (True/False) ")
