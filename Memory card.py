from PyQt5.QtWidgets import QApplication

app = QApplication([])


from random import choice, shuffle
from time import sleep
from Memory_card_2 import *
from Memory_card_3 import *

window.show()
app.exec_()

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0

q1 = Question ("Когда я взял в плен детей?", "1939", "1941", "1886", "1901")
q2 = Question ("Когда я сел за то что я взял детей в плен?", "2000", "1941", "2012", "1912")
q3 = Question ("Сколько лет я сидел?", "5", "9", "8", "12")
q4 = Question ("2+2?", "4", "6", "22", "2+2")
q5 = Question ("пон?", "Ясно", "пон", "Да", "Я вас понял сударь")
q6 = Question ("Пабачи ор иксбокссирисикисбокс", "Пабачи", "икс", "иксбокссирисикисбокс", "ор")
q7 = Question ("Сколько негров я купил?", "5", "10", "негр", "да")
q8 = Question ("Ты Тайлер Жордан?", "Да негр", "Так появился он Тайлер Жордан", "нет", "")
q9 = Question ("Ты?", "я?", "Ты", "негр", "Пиз...")
q10 =Question ("Бананчики", "Бананчики", "Бананчики", "Бананчики", "Бананчики")

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
question = [q1, q2, q3, q4, q5, q6 ,q7, q8, q9, q10]

def new_question():
    global cur_q
    cur_q = choice(question)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильна!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Наступне запитання')
btn_next.clicked.connect(click_ok)

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)

def menu_generation():
    menu_win.show()
    window.hide()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_back.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())
    question.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)

window.show()
app.exec_()