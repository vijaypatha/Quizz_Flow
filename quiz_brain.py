# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # current question is equal to a list of question [0]. I'm adding self to link the object to the class
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect")

# class QuizBrain:
#     def __init__(self, question_list_obj):
#         self.question_list = question_list_obj
#         #based on the question_model question object has two attributes: text and answer
#         self.question_number = 0
#         self.score = 0
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
#         self.check_answer(user_answer, current_question.answer)
#
#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             print("You got it right!")
#             self.score += 1
#         else:
#             print('You got it wrong!')
#
#     def still_has_questions(self):
#         if self.question_number < len(self.question_list):
#             return True
#         else:
#             return False
