from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import Qt

Form, Window = uic.loadUiType("form.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle(" ")
window.show()

reg_ex = QRegExp("[0-9]*")
validator = QRegExpValidator(reg_ex)
form.lineEdit_2.setValidator(validator)
form.lineEdit_3.setValidator(validator)

reg_ex1 = QRegExp("([0-9]+[,])*")
validator1 = QRegExpValidator(reg_ex1)
form.lineEdit_4.setValidator(validator1)

#Вычисляющие функции
#Функция для вычисления факториала числа
def factorial(number):
    factorialNumber = 1
    for i in range(2, number + 1):
        factorialNumber *= i
    return factorialNumber

#Функция для вычисления n в степени m
def placementWithRepetition(numberN, numberM):
    return numberN**numberM

#Функция для вычисления произведения всех k
def k_multiplication(numberN,numberM):
    mult = 1
    k_sum = 0
    k_amount = 0
    str = form.lineEdit_4.text()
    if(str.find(",") == -1):
        mult = int(str)
        k_sum = int(str)
        k_amount = 1
    else:
        while(str!=""):
            k = int(str.partition(',')[0])
            mult = mult*k
            k_sum = k_sum + k
            str = str.partition(',')[2]
            k_amount +=1

    if (k_sum != numberM):
        return -1
    elif(k_amount != numberN):
        return -2
    elif(mult == 0):
        return -3
    else:
        return mult


#Вывод результата расчета функции или сообщения об ошибке после нажатия кнопки "Рассчитать"
def on_click():
    if(form.lineEdit_2.text()=="" or form.lineEdit_3.text()=="" or form.lineEdit_4.text()==""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Введите все значения.")
        msg.setWindowTitle("Ошибка")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        return
    else:
        numberM= int(form.lineEdit_3.text())
        numberN = int(form.lineEdit_2.text())

        if(k_multiplication(numberN,numberM)==-1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Сумма k не равна m.")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        elif(k_multiplication(numberN,numberM)==-2):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Количество значений k не равно n.")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        elif(k_multiplication(numberN,numberM)==-3):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Значение k не может быть нулевым.")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        else:
            number1 = factorial(numberN)
            number2 = placementWithRepetition(numberN, numberM)
            number3 = k_multiplication(numberN, numberM)
            result = number1/(number2*number3)
            form.lineEdit.setPlainText(str(result))
            return

form.pushButton.clicked.connect(on_click)

app.exec_()