import random
from Classes import Question



def get_questions(questions_date):
    questions = []
    for question in questions_date:
        questions.append(Question(question["q"], question["d"], question["a"]))
    random.shuffle(questions)
    return questions


def statistic(questions):
    score = 0
    right_answers = 0
    for question in questions:
        if question.user_answer:
            score += question.get_points()
            right_answers += 1
    print(f'\nВот и все!\nОтвечено на {right_answers} вопроса из {len(questions)}\nНабрано баллов: {score}')
