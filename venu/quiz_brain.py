class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

    def next_q(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1

        user_answer = input(f"{self.question_num}. {current_question.text} (True/False)? ").strip().lower()
        correct_answer = str(current_question.answer).lower()

        if user_answer == correct_answer:
            self.score += 1
            print(f"You are right! Your score is: {self.score}/{self.question_num}")
        else:
            print(f"Not today! Your score is: {self.score}/{self.question_num}")

    def another_q(self):
        return self.question_num < len(self.question_list)
