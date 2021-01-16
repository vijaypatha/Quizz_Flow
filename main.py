from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question_answer = Question(question_text, question_answer)
    question_bank.append(new_question_answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score is: {quiz.score}/{len(question_bank)}")
