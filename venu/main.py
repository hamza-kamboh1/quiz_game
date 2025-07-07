from data import question_data
from question_model import Question
import random
from quiz_brain import QuizBrain



question_bank = []
for item in range(len(question_data)):
    # test = input("Enter")
    reveal  =  question_data[item]
    a_text = reveal["text"]
    b_answer = reveal["answer"]
    test_q = Question(a_text, b_answer)
    question_bank.append(test_q)

q_can = QuizBrain(question_bank)
q_can.next_q()
print(q_can.score)


while q_can.another_q():
    q_can.next_q()
    print("Thanks for playing")
    print("Your final score is: ", q_can.score)
    print( "You got: ", q_can.score,"correct", "out of", len(question_data), "questions")