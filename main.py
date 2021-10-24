# -*- coding: utf-8 -*-

import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QFileDialog, QMessageBox
from mainUi import Ui_MainWindow

VINIGER_SQUARE_RU = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя'[i:] +
                     'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'[:i] for i in range(33)]

VINIGER_SQUARE_ENG = ['abcdefghijklmnopqrstuvwxyz'[i:] +
                      'abcdefghijklmnopqrstuvwxyz'[:i] for i in range(26)]

POLIBIUS_ENG = 'abcdefghiklmnopqrstuvwxyz'

POLIBIUS_RU = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


class Cryptor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.decoding_w.hide()
        self.con = sqlite3.connect('crypt_tables.db')  # Соединение с бд
        self.coding = 'utf-8'  # Кодировка при открытии и сохранении файлов

        self.ru = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  # Русский алфавит: строчный и заглавный
                   'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
        self.eng = ['abcdefghijklmnopqrstuvwxyz',  # Английский алфавит: строчный и заглавный
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.fpath = ''  # Путь к выбранному файлу

        self.connections()  # Присоединяем сигналы к слотам

    def connections(self):
        """Функция присоединяет сигналы кнопок к слтоам-функциям"""
        self.action.triggered.connect(self.show_encoding)  # отображение кодировщика
        self.action_2.triggered.connect(self.show_decoding)  # отображение декодировщика
        self.action_3.triggered.connect(self.change_coding)  # открывает окно смены кодировки файлов
        self.action_4.triggered.connect(self.clean_all)  # Очищает все поля для ввода
        self.do_decrypt.clicked.connect(self.decrypt)  # апускает алгоритм декодировки
        self.do_encrypt.clicked.connect(self.encrypt)  # апускает алгоритм кодировки
        self.open_file.clicked.connect(self.file_opening)  # открывает окно выбора файла на декодировщике
        self.open_file_2.clicked.connect(self.file_opening_2)  # открывает окно выбора файла на кодировщике

    def show_encoding(self):
        """отображает виджет-шифровщик"""
        self.decoding_w.hide()
        self.encoding_w.show()

    def show_decoding(self):
        """Отображает виджет-дешифровщик"""
        self.encoding_w.hide()
        self.decoding_w.show()

    def change_coding(self):
        """Функция меняет кодировку по умолчанию"""
        coding, ok_pressed = QInputDialog.getText(self, 'Выбор кодировки файлов',
                                                  'Напишите желаемую кодировку')
        if ok_pressed:
            self.coding = coding
    
    def clean_all(self):
        self.file_name.clear()
        self.file_name_2.clear()
        self.source.clear()
        self.decrypted_text.clear()
        self.encrypted_text.clear()
        self.encrypted_text_2.clear()

    def file_opening(self):
        """Функция открывает файл и сохраняет путь к нему"""
        self.fpath = QFileDialog.getOpenFileName(self, 'Выбрать файл для шифрования', '')[0]
        try:
            if self.fpath == '':  # Если файл не выбрали, то возбуждается ошибка
                raise TypeError
            with open(self.fpath, encoding=self.coding) as file:
                # В окно ввода считываем текст из файла
                self.encrypted_text.setText(file.read())
                self.file_name.setText(self.fpath.split('/')[-1])  # Отображаем только название файла
        except UnicodeError:
            QMessageBox.critical(self, "Ошибка ", "Файл невозможно прочитать",
                                 QMessageBox.Ok)
        except TypeError:
            QMessageBox.critical(self, "Ошибка ", "Файл не выбран",
                                 QMessageBox.Ok)

    def file_opening_2(self):
        """Функция открывает файл и сохраняет путь к нему"""
        self.fpath = QFileDialog.getOpenFileName(self, 'Выбрать файл для шифрования', '')[0]
        try:
            if self.fpath == '':  # Если файл не выбрали, то возбуждается ошибка
                raise TypeError
            with open(self.fpath, encoding=self.coding) as file:
                # В окно ввода считываем текст из файла
                self.source.setText(file.read())
                self.file_name_2.setText(self.fpath.split('/')[-1])  # Отображаем только название файла
        except UnicodeError:
            QMessageBox.critical(self, "Ошибка ", "Файл невозможно прочитать",
                                 QMessageBox.Ok)
        except TypeError:
            QMessageBox.critical(self, "Ошибка ", "Файл не выбран",
                                 QMessageBox.Ok)

    def decrypt(self):
        """Функция дешифрует заданный текст по выбранному алгоритму и отображает его"""
        text = self.encrypted_text.toPlainText()  # Сохраняем весь текст из поля ввода в текстовую переменную
        # Шифруем по выбранному алгоритму
        if self.cipher.currentText() == 'Шифр Цезаря':
            self.decrypted_text.setPlainText(self.caesar_decrypt(text))
        elif self.cipher.currentText() == 'Атбаш':
            self.decrypted_text.setPlainText(self.atbash(text))
        elif self.cipher.currentText() == 'Шифр Вижинера':
            self.decrypted_text.setPlainText(self.viginer_decrypt(text))
        elif self.cipher.currentText() == 'Морзе':
            self.decrypted_text.setPlainText(self.morse_decrypt(text))
        elif self.cipher.currentText() == 'Шифр Полибия':
            self.decrypted_text.setPlainText(self.polibius_decrypt(text))
        # Если мы выбрали файл и активировали шифрование, то нас спрашивают, хотим ли мы изменить файл
        # Если нажать нет, то текст отобразится в выходном поле, а сам файл не изменится
        if self.file_name.text() != '' and self.encrypted_text.toPlainText() != '':
            file_path = self.fpath.replace('.', '_decrypted.')
            if QMessageBox.warning(self, "Подтверждение",
                                   "Вы точно хотите создать копию исходного файла?",
                                   QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
                try:
                    with open(file_path, mode='w', encoding=self.coding) as file:
                        print(self.decrypted_text.toPlainText(), end='', file=file)  # Запись в файл
                except FileNotFoundError:
                    QMessageBox.critical(self, "Ошибка ", "Файл не найден", QMessageBox.Ok)

    def encrypt(self):
        """Функция шифрует заданный текст по выбранному алгоритму и отображает его"""
        text = self.source.toPlainText()
        if self.cipher_2.currentText() == 'Шифр Цезаря':
            self.encrypted_text_2.setPlainText(self.caesar_encrypt(text))
        elif self.cipher_2.currentText() == 'Атбаш':
            self.encrypted_text_2.setPlainText(self.atbash(text))
        elif self.cipher_2.currentText() == 'Шифр Вижинера':
            self.encrypted_text_2.setPlainText(self.viginer_encrypt(text))
        elif self.cipher_2.currentText() == 'Морзе':
            self.encrypted_text_2.setPlainText(self.morse_encrypt(text))
        elif self.cipher_2.currentText() == 'Шифр Полибия':
            self.encrypted_text_2.setPlainText(self.polobius_encrypt(text))
        # Если мы выбрали файл и активировали шифрование, то нас спрашивают, хотим ли мы изменить файл
        # Если нажать нет, то текст отобразится в выходном поле, а сам файл не изменится
        if self.file_name_2.text() != '' and self.source.toPlainText() != '':
            file_path = self.fpath.replace('.', '_encrypted.')
            if QMessageBox.warning(self, "Подтверждение",
                                   "Вы точно хотите создать копию исходного файла?",
                                   QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
                try:
                    with open(file_path, mode='w', encoding=self.coding) as file:
                        print(self.encrypted_text_2.toPlainText().strip(), end='', file=file)  # Запись в файл
                except FileNotFoundError:
                    QMessageBox.critical(self, "Ошибка ", "Файл не найден", QMessageBox.Ok)

    def caesar_decrypt(self, plain_text):
        """Дешифровка по алгоритму Шифра Цезаря"""
        # Мы заменяем буквы алфавита со сдвигом на 3 буквы назад по алфавиту
        res = ''
        for i in plain_text.strip():
            if self.ru[0].find(i) != -1:
                res += self.ru[0][self.ru[0].find(i) - 3 % 32]
            elif self.ru[1].find(i) != -1:
                res += self.ru[1][self.ru[1].find(i) - 3 % 32]
            elif self.eng[0].find(i) != -1:
                res += self.eng[0][self.eng[0].find(i) - 3 % 25]
            elif self.eng[1].find(i) != -1:
                res += self.eng[1][self.eng[1].find(i) - 3 % 25]
            else:
                res += i
        return res.strip()

    def caesar_encrypt(self, plain_text):
        """Шифровка по алгоритму Шифра Цезаря"""
        # Мы заменяем буквы со сдвигом на 3 буквы вперёд по алфавиту
        res = ''
        for i in plain_text.strip():
            if self.ru[0].find(i) != -1:
                res += self.ru[0][(self.ru[0].find(i) + 3) % 33]
            elif self.ru[1].find(i) != -1:
                res += self.ru[1][(self.ru[1].find(i) + 3) % 33]
            elif self.eng[0].find(i) != -1:
                res += self.eng[0][(self.eng[0].find(i) + 3) % 26]
            elif self.eng[1].find(i) != -1:
                res += self.eng[1][(self.eng[1].find(i) + 3) % 26]
            else:
                res += i
        return res.strip()

    def atbash(self, plain_text):
        """Шифровка и дешифровка по алгоритму Атбаш"""
        # Т.к. этот алгоритм работает и на шифровку и на дешифровку,
        # то делать отдельные функции не надо
        # Мы заменяем буквы на буквы, зеркальные им в алфавите
        # К примеру русское "а" заменяется на руское "я",
        # "б" на "ю" и так далее
        res = ''
        for i in plain_text.strip():
            if self.ru[0].find(i) != -1:
                res += self.ru[0][32 - self.ru[0].find(i)]
            elif self.ru[1].find(i) != -1:
                res += self.ru[1][32 - self.ru[1].find(i)]
            elif self.eng[0].find(i) != -1:
                res += self.eng[0][25 - self.eng[0].find(i)]
            elif self.eng[1].find(i) != -1:
                res += self.eng[1][25 - self.eng[1].find(i)]
            else:
                res += i
        return res

    def viginer_encrypt(self, plain_text):
        """Шифрование по алгоритму Шифра Вижинера"""
        # Мы имеем 2 квадрата Вижинера состоящих из 33 (в русском и 26 в английском) строк по столько же столбцов
        # в каждой строке стоит алфавит сдвинутый на количество позиций, равных номеру строки.
        # При шифровании мы спускаемся на 1 строчку квадрата Вижинера ниже исходной и находим букву стоящую
        # в строке на месте исходной буквы в алфавите
        res = ''
        line_ru = 1
        line_eng = 1
        for i, letter in enumerate(plain_text.strip()):
            if letter in self.ru[0] or letter in self.ru[1]:
                if letter.isupper():
                    res += VINIGER_SQUARE_RU[line_ru][VINIGER_SQUARE_RU[0].find(letter.lower())].upper()
                else:
                    res += VINIGER_SQUARE_RU[line_ru][VINIGER_SQUARE_RU[0].find(letter.lower())]
                if line_ru >= 32:
                    line_ru = 0
                else:
                    line_ru += 1
            elif letter in self.eng[0] or letter in self.eng[1]:
                if letter.isupper():
                    res += VINIGER_SQUARE_ENG[line_eng][VINIGER_SQUARE_ENG[0].find(letter.lower())].upper()
                else:
                    res += VINIGER_SQUARE_ENG[line_eng][VINIGER_SQUARE_ENG[0].find(letter.lower())]
                if line_eng >= 25:
                    line_eng = 0
                else:
                    line_eng += 1
            else:
                res += letter
        return res

    def viginer_decrypt(self, plain_text):
        """Дешифрование по алгоритму Шифра Вижинера"""
        # Мы имеем 2 квадрата Вижинера состоящих из 33 (в русском и 26 в английском) строк по столько же столбцов
        # в каждой строке стоит алфавит сдвинутый на количество позиций, равных номеру строки.
        # При шифровании мы спускаемся на 1 строчку квадрата Вижинера ниже исходной и находим букву стоящую
        # в строке на месте исходной буквы в алфавите
        res = ''
        line_ru, line_eng = self.count_letters(plain_text.strip())
        for i, letter in enumerate(plain_text[::-1]):  # Мы берём перевёрнутую строку, потому что нам надо идти с конца
            if letter in self.ru[0] or letter in self.ru[1]:
                if letter.isupper():  # Заглавные буквы заменяем на заглавные, а строчные на строчные соответственно
                    res += VINIGER_SQUARE_RU[0][VINIGER_SQUARE_RU[line_ru].find(letter.lower())].upper()
                else:
                    res += VINIGER_SQUARE_RU[0][VINIGER_SQUARE_RU[line_ru].find(letter.lower())]
                # Если мы доходим до последней строчки квадрата, то возвращаемся в начало
                if line_ru <= 0:
                    line_ru = 32
                else:
                    line_ru -= 1
            elif letter in self.eng[0] or letter in self.eng[1]:
                if letter.isupper():  # Заглавные буквы заменяем на заглавные, а строчные на строчные соответственно
                    res += VINIGER_SQUARE_ENG[0][VINIGER_SQUARE_ENG[line_eng].find(letter.lower())].upper()
                else:
                    res += VINIGER_SQUARE_ENG[0][VINIGER_SQUARE_ENG[line_eng].find(letter.lower())]
                # Если мы доходим до последней строчки квадрата, то возвращаемся в начало
                if line_eng <= 0:
                    line_eng = 25
                else:
                    line_eng -= 1
            else:
                res += letter
        return res[::-1]

    def count_letters(self, text):
        """Функция подсчитывает количество русских и латинских букв"""
        ru_len, eng_len = 0, 0
        for i in text.strip():
            if i.lower() in self.ru[0]:
                ru_len += 1
            elif i.lower() in self.eng[0]:
                eng_len += 1
        return tuple([ru_len % 33, eng_len % 26])

    def morse_encrypt(self, plain_text):
        """Шифрование с помощью Шифра Морзе"""
        cur = self.con.cursor()  # Подключение курсора бд
        res = []
        language, ok_pressed = QInputDialog.getItem(self, 'Выберите основной язык файла',
                                                    'Какой язык преобладает в тексте?',
                                                    ['русский', 'английский'])
        if ok_pressed:
            for i in plain_text.strip().lower():
                if i == '"':  # Замена кавычек отдельна, т.к. при обработке выходит syntax error
                    res.append('.-..-.')
                else:
                    if language == 'русский':
                        # Получаем код морзе по символу из базы данных
                        code = cur.execute('SELECT code FROM morze_ru WHERE letter="{}"'.format(i)).fetchone()
                        if not code:  # Если на замену ничего нет, то сохраняем символ как есть
                            res.append(i)
                        else:
                            res.append(code[0])
                    elif language == 'английский':
                        code = cur.execute('SELECT code FROM morze_eng WHERE letter="{}"'.format(i)).fetchone()
                        if not code:  # Если на замену ничего нет, то сохраняем символ как есть
                            res.append(i)
                        else:
                            res.append(code[0])

        return '|'.join(res)

    def morse_decrypt(self, plain_text):
        """Дешифрование с использованием Шифра Морзе"""
        cur = self.con.cursor()  # Подключение курсора бд
        res = ''
        language, ok_pressed = QInputDialog.getItem(self, 'Выбор кодировки файлов',
                                                    'Напишите желаемую кодировку',
                                                    ['русская', 'английская'])
        if ok_pressed:
            for i in plain_text.split('|'):
                if i == '.-..-.':  # Замена апострофа отдельна, т.к. при обработке выходит syntax error
                    res += "'"
                else:
                    if language == 'русская':
                        letter = cur.execute("""SELECT letter FROM morze_ru'
                                             'WHERE code='{}'""".format(i)).fetchone()
                        if not letter:  # Если на замену ничего нет, то сохраняем символ как есть
                            res += i
                        else:
                            res += letter[0]
                    elif language == 'английская':
                        letter = cur.execute('SELECT letter FROM morze_eng'
                                             'WHERE code="{}"'.format(i)).fetchone()
                        if not letter:  # Если на замену ничего нет, то сохраняем символ как есть
                            res += i
                        else:
                            res += letter[0]

        return res

    def polobius_encrypt(self, plain_text):
        """Шифрование с помощью алгоритма Шифра Полибия"""
        # У нас есть таблица такого вида:
        #   | а б в г д е ж з
        # -------------------
        # а | а б в г д е ж з
        # б | и й к л м н о п
        # в | р с т у ф х ц ч
        # г | ш щ ъ ы ь э ю я
        # Каждая буква кодируется названием строки и столбца,
        # к примеру "л" это "бг".
        # Для латиницы таблица 5 на 5 и буква j отдельно
        res = []
        for i in plain_text:
            if i.lower() in self.eng[0]:  # Проверяем раскладку символа
                if i.isupper():  # Если буква заглавная, то прибавляем заглавную
                    # буква "j" кодируется отдельно, так как её нет места в таблице
                    if i == 'J':
                        res.append(i * 2)
                    else:
                        res.append(POLIBIUS_ENG[POLIBIUS_ENG.find(i.lower()) // 5].upper() +
                                   POLIBIUS_ENG[POLIBIUS_ENG.find(i.lower()) % 5].upper())
                else:  # Если строчная, то прибавляем строчную
                    if i == 'j':
                        res.append(i * 2)
                    else:
                        res.append(POLIBIUS_ENG[POLIBIUS_ENG.find(i) // 5] +
                                   POLIBIUS_ENG[POLIBIUS_ENG.find(i) % 5])
            elif i.lower() in self.ru[0]:
                if i.isupper():  # Если буква заглавная, то прибавляем заглавную
                    if i == 'Ё':
                        res.append(i)
                    else:
                        res.append(POLIBIUS_RU[POLIBIUS_RU.find(i.lower()) // 8].upper() +
                                   POLIBIUS_RU[POLIBIUS_RU.find(i.lower()) % 8].upper())
                else:  # Если строчная, то прибавляем строчную
                    if i == 'ё':
                        res.append(i)
                    else:
                        res.append(POLIBIUS_RU[POLIBIUS_RU.find(i) // 8] +
                                   POLIBIUS_RU[POLIBIUS_RU.find(i) % 8])
            else:  # Если это не буква, то просто прибавляем к общим символам
                res.append(i)
        return '|'.join(res)

    def polibius_decrypt(self, plain_text):
        """Дешифрование с помощью алгоритма Шифра Полибия"""
        text = plain_text.split('|')  # Получаем пары букв и различные незашифрованные символы
        res = ''
        for i in text:
            if i.isalpha() and len(i) == 2:  # Если это пара букв, то идём дальше
                # Если обе буквы в английском алфавите, то берём буквы из английского
                if i[0].lower() in self.eng[0] and i[1].lower() in self.eng[0]:
                    if i.isupper():
                        if i == 'JJ':  # Так как буква j кодируется отдельно, то проверяем её специальный код
                            res += 'J'
                        else:
                            # Прибавляем заглавную букву стоящую в определённом столбце и строке в мнимой таблице
                            res += POLIBIUS_ENG[POLIBIUS_ENG.find(i[0].lower()) * 5 +
                                                POLIBIUS_ENG.find(i[1].lower())].upper()
                    else:
                        if i == 'jj':  # Так как буква j кодируется отдельно, то проверяем её специальный код
                            res += 'j'
                        else:
                            # Прибавляем букву стоящую в определённом столбце и строке в мнимой таблице
                            res += POLIBIUS_ENG[POLIBIUS_ENG.find(i[0]) * 5 +
                                                POLIBIUS_ENG.find(i[1])]
                # Если обе буквы в русском алфавите, то берём буквы из английского
                if i[0].lower() in self.ru[0] and i[1].lower() in self.ru[0]:
                    if i.isupper():
                        # Прибавляем заглавную букву стоящую в определённом столбце и строке в мнимой таблице
                        res += POLIBIUS_RU[POLIBIUS_RU.find(i[0].lower()) * 8 +
                                           POLIBIUS_RU.find(i[1].lower())].upper()
                    else:
                        # Прибавляем букву стоящую в определённом столбце и строке в мнимой таблице
                        res += POLIBIUS_RU[POLIBIUS_RU.find(i[0].lower()) * 8 +
                                           POLIBIUS_RU.find(i[1].lower())]
            else:
                # Если это не буква, то её просто добавляем без изменений
                res += i
        return res


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Cryptor()
    c.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
