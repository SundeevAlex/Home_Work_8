class Question:
    def __init__(self, question, difficult, answer):
        self.question = question
        self.difficult = int(difficult)
        self.answer = answer

        self.was_question = False
        self.user_answer = None

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.difficult * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if self.user_answer == self.answer:
            return True
        else:
            self.user_answer = None
            return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        self.was_question = True
        return f'\nВопрос: {self.question}\nСложность: {self.difficult}/5'

    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.get_points()} баллов'
        return f'Ответ неверный, верный ответ {self.answer}'
