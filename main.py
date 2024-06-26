from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)


questions = []

for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    questions.append(question)

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{len(questions)}")
