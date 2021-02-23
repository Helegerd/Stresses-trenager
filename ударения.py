# Coding:utf-8
import sys
from random import shuffle
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QWidget, QGridLayout
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QObject
SONGS = 'ЁУЕЭОАЫЯИЮ'


class StressRus(QMainWindow, QWidget):
    '''игровое окно'''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Тренажёр ударений')
        self.setGeometry(0, 0, 800, 800)
        self.wordparts = []  # текущее слово
        self.rightpart = -1  # номер слога с ударением
        self.buttons = []  # кнопки 
        # координаты клика
        self.xPos = 0
        self.yPos = 0
        self.loadFile = 'слова_слоги_сущ.txt'  # файл со словами
        self.startbtn = QPushButton('Arial font', self)  # кнопка запуска тренировки
        self.startbtn.resize(400, 50)
        self.startbtn.move(200, 700)
        self.startbtn.setFont(QFont('Arial', 30))
        self.startbtn.setText('НАЧАТЬ')
        self.startbtn.clicked.connect(self.start_learning)
        
        self.nextbtn = QPushButton(self)  # кнопка для перехода к следующему слову
        self.nextbtn.resize(100, 50)
        self.nextbtn.move(650, 700)
        self.nextbtn.setText('ДАЛЕЕ')
        self.nextbtn.setFont(QFont('Arial font', 17))
        self.nextbtn.clicked.connect(self.nextword)
        self.nextbtn.hide()
        
        self.nounbtn = QPushButton(self)  # кнопка выбора существительных
        self.nounbtn.resize(400, 50)
        self.nounbtn.move(200, 50)
        self.nounbtn.setText('СУЩЕСТВИТЕЛЬНЫЕ')
        self.nounbtn.clicked.connect(self.choose_noun)
        
        self.adjbtn = QPushButton(self)  # кнопка выбора прилагательных
        self.adjbtn.resize(400, 50)
        self.adjbtn.move(200, 170)
        self.adjbtn.setText('ПРИЛАГАТЕЛЬНЫЕ')
        self.adjbtn.clicked.connect(self.choose_adj)
        
        self.verbbtn = QPushButton(self)  # кнопка выбора глаголов
        self.verbbtn.resize(400, 50)
        self.verbbtn.move(200, 290)
        self.verbbtn.setText('ГЛАГОЛЫ')
        self.verbbtn.clicked.connect(self.choose_verb)
        
        self.parbtn = QPushButton(self)  # кнопка выбора причастий
        self.parbtn.resize(400, 50)
        self.parbtn.move(200, 410)
        self.parbtn.setText('ПРИЧАСТИЯ')
        self.parbtn.clicked.connect(self.choose_par)
        
        self.advbtn = QPushButton(self)  # кнопка выбора наречий и деепричастий
        self.advbtn.resize(400, 50)
        self.advbtn.move(200, 530)
        self.advbtn.setText('НАРЕЧИЯ+ДЕЕПРИЧАСТИЯ')
        self.advbtn.clicked.connect(self.choose_adv)
        
        self.grid = QGridLayout()  # сетка вывода слогов
        self.setLayout(self.grid)
        
 
    def start_learning(self):
        '''основной цикл обучения'''
        self.nounbtn.hide()
        self.adjbtn.hide()
        self.verbbtn.hide()
        self.advbtn.hide()
        self.parbtn.hide()
        self.nextbtn.show()
        self.startbtn.setText('ГЛ МЕНЮ')
        self.startbtn.clicked.connect(self.go_to_main_menu)
        self.learning_is_going = True
        self.words = [] # список слов
        with open(self.loadFile, mode='r', encoding='utf-8') as f:  # забираем слова из файла
            self.words = f.readlines()
        shuffle(self.words)
        
    def go_to_main_menu(self):
        '''возврат в главное меню, к выбору частей речи'''
        self.nounbtn.show()
        self.adjbtn.show()
        self.verbbtn.show()
        self.advbtn.show()
        self.parbtn.show()
        self.startbtn.setText('НАЧАТЬ')
        self.startbtn.clicked.connect(self.start_learning)
        self.nextbtn.hide()
        self.learning_is_going = False
        for but in self.buttons:  # прячет предыдущие кнопки
            but.hide()
            but.destroy()
        
    def nextword(self):
        '''меняет слово на экране'''
        for but in self.buttons:  # прячет предыдущие кнопки
            but.hide()
            but.destroy()
        word = self.words[0]  # pop не так работает...
        self.words = self.words[1:] + [self.words[0]]
        self.wordparts = word.split()[1:]
        self.rightpart = int(word.split()[0])
        self.buttons = []
        for i in range(len(self.wordparts)):  # расставляет кнопки в ряд
            self.button = QPushButton(self)
            self.button.setFont(QFont('Arial', 25))
            self.button.setText(self.wordparts[i])
            self.buttons.append(self.button)
            self.button.resize(120, 60)
            self.buttons[i].clicked.connect(self.showtrueans)
            self.buttons[i].move(i * (800 // (1 +len(self.wordparts))) + 70, 100)
            self.buttons[i].show()
        
    def showtrueans(self):
        '''показывает правильный слог'''
        for i in range(len(self.wordparts)):
            if i == self.rightpart - 1:
                continue
            self.buttons[i].hide()
    
    def choose_noun(self):
        self.loadFile = 'слова_слоги_сущ.txt'
    
    def choose_adj(self):
        self.loadFile = 'слова_слоги_прил.txt'
    
    def choose_verb(self):
        self.loadFile = 'слова_слоги_глаг.txt'
    
    def choose_adv(self):
        self.loadFile = 'слова_слоги_нар.txt'
    
    def choose_par(self):
        self.loadFile = 'слова_слоги_прич.txt'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stress = StressRus()
    stress.show()
    sys.exit(app.exec_())