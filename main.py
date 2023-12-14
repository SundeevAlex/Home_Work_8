from Classes import Question
from functions import statistic, get_questions

questions_date = [
    {
        "q": "How many days do we have in a week?",
        "d": "1",
        "a": "7"
    }, {
        "q": "How many letters are there in the English alphabet?",
        "d": "3",
        "a": "26"
    }, {
        "q": "How many sides are there in a triangle?",
        "d": "2",
        "a": "3"
    }, {
        "q": "How many years are there in one Millennium?",
        "d": "2",
        "a": "1000"
    }, {
        "q": "How many sides does hexagon have?",
        "d": "4",
        "a": "6"
    }
]


def main():
    questions = get_questions(questions_date)
    print("Игра начинается")
    for question in questions:
        print(question.build_question())
        question.user_answer = input('>')
        print(question.build_feedback())
    statistic(questions)


if __name__ == '__main__':
    main()
