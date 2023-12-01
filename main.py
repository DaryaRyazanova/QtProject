import sys
import sqlite3

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QTableWidgetItem
from reg_ui import Ui_MainWindow
from login_ui import Ui_MainWindow2
from successful_registration import Ui_Form
from main_ui import Ui_Form2
from dialog_ui import Ui_Dialog


class PasswordError(Exception):
    pass


class NoPasswordError(PasswordError):  # Вызывается, если пароль не введен
    pass


class PasswordLenError(PasswordError):  # Вызывается, если длина пароля не более 8 символов
    pass


class EmailError(Exception):
    pass


class NoEmailError(EmailError):  # Вызывается, если почта не введена
    pass


class EmailFormatError(EmailError):  # Вызывается, если формат почты неверный
    pass


class InvalidFormat(EmailError):  # Вызывается, если окончание почты не '.com' и не '.ru'
    pass


class PhoneError(Exception):
    pass


class NoPhoneError(PhoneError):  # Вызывается, если номер телефона не введен
    pass


class PhoneFormatError(PhoneError):  # Вызывается, если формат номера неверный
    pass


class PhoneLenError(PhoneError):  # Вызывается, если длина номера (без +7 и 8) не равна десяти
    pass


class RegistrationWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Окно регистрации')
        self.second_form = SuccessfulRegistration()
        self.login_form = LoginWidget()
        self.visibility_button.clicked.connect(self.change_visibility)  # При нажатии меняется видимость пароля
        self.copy_button.clicked.connect(self.copy)  # При нажатии пароль копируется в буфер обмена
        self.generation_button.clicked.connect(self.generation)  # При нажатии генерируется пароль
        self.reg_Button.clicked.connect(self.run)  # При нажатии проводится проверка всех введенных данных и,
        # если данные корректны, они отсылаются в базу данных и если в базе этих данных не было, то выводится окно
        # с надписью "Вы успешно зарегистрированы!"
        self.log_in_Button.clicked.connect(self.show_login_window)  # При нажатии открывается окно входа
        self.log_in_Button.clicked.connect(self.close)

    def change_visibility(self):  # Метод изменения видимости пароля
        if not self.visibility_button.isChecked():
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def copy(self):  # Метод копирования пароля в буфер обмена
        QApplication.clipboard().setText(self.password.text())

    def generation(self):  # Метод генерации пароля
        symbols = ascii_lowercase + ascii_uppercase + digits
        length, password = 15, ''
        for i in range(length):
            password += choice(symbols)
        self.password.setText(password)

    # noinspection PyMethodMayBeStatic
    def check_phone_number(self, n):  # Метод проверки корректности номера телефона
        n = ''.join(n.split())
        if (n.count('(') > 1 or n.count(')') > 1 or (n.count('(') != n.count(')')) or
                n.find('(') > n.find(')')):
            return PhoneFormatError
        else:
            if '(' in n:
                n = ''.join(n.split('('))
                n = ''.join(n.split(')'))
            if not (n[:1] == '8' or n[:2] == '+7'):
                return PhoneFormatError
            else:
                if '--' in n or '-' == n[-1:]:
                    return PhoneFormatError
                else:
                    n = ''.join(n.split('-'))
                    if n[:1] == '8':
                        n = n[1:]
                    else:
                        n = n[2:]
                    if not (n.isdigit() and len(n) == 10):
                        return PhoneLenError
                    else:
                        return f'+7{n}'

    # noinspection PyMethodMayBeStatic
    def check_email(self, email):  # Метод проверки корректности электронной почты
        if '@' in email:
            email = email.split('@')
        else:
            return EmailFormatError
        symbols = ascii_lowercase + ascii_uppercase + digits + '''!#$%&'*+-/=?^_`{|}~.'''
        for elem in email[0]:
            if elem not in symbols:
                return EmailFormatError
        if email[0][0] == '.' or email[0][-1] == '.' or '..' in email[0]:
            return EmailFormatError
        if email[1].split('.')[1] != 'ru' and email[1].split('.')[1] != 'com':
            return InvalidFormat

    def show_login_window(self):  # Метод вызова окна входа
        self.login_form.show()

    def run(self):  # Метод, вызываемый при нажатии кнопки 'Зарегистрироваться'
        number = self.phone_number.text()  # Проверка на корректность номера телефона и вывод ошибок
        try:
            if not number:
                raise NoPhoneError('Введите пароль')
            elif self.check_phone_number(number) == PhoneFormatError:
                raise PhoneFormatError('Неверный формат')
            elif self.check_phone_number(number) == PhoneLenError:
                raise PhoneFormatError('Неверное количество цифр')
            else:
                self.phone_error_Label.setText('')
        except NoPhoneError:
            self.phone_error_Label.setText('Введите номер телефона')
        except PhoneFormatError:
            self.phone_error_Label.setText('Неверный формат')
        except PhoneLenError:
            self.phone_error_Label.setText('Неверное количество цифр')

        password = self.password.text()  # Проверка на корректность пароля и вывод ошибок
        try:
            if not password:
                raise NoPasswordError
            elif len(password) < 9:
                raise PasswordLenError
            else:
                self.password_error_Label.setText('')
        except NoPasswordError:
            self.password_error_Label.setText('Введите пароль')
        except PasswordLenError:
            self.password_error_Label.setText('Длина пароля должна превышать 8 символов')

        email = self.email.text()  # Проверка на корректность электронной почты и вывод ошибок
        try:
            if not email:
                raise NoEmailError
            elif self.check_email(email) == EmailFormatError:
                raise EmailFormatError
            elif self.check_email(email) == InvalidFormat:
                raise InvalidFormat
            else:
                self.email_error_Label.setText('')
        except NoEmailError:
            self.email_error_Label.setText('Введите электронную почту')
        except EmailFormatError:
            self.email_error_Label.setText('Неверный формат')
        except InvalidFormat:
            self.email_error_Label.setText('Формат вашей электронной почты не поддерживается')

        if (not self.password_error_Label.text() and not self.email_error_Label.text() and
                not self.phone_error_Label.text()):  # Проверка есть ли ошибки
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            try:  # Если данных в базе нет, то сработает try, а если есть - except
                cursor.execute('BEGIN')
                cursor.execute('INSERT INTO users (phone_number, email, password) VALUES (?, ?, ?)',
                               (self.check_phone_number(number), email, password))
                cursor.execute('COMMIT')
                self.second_form.show()
                self.password.setText('')
                self.phone_number.setText('')
                self.email.setText('')
                self.registration_error_Label.setText('')
            except sqlite3.IntegrityError:
                cursor.execute('ROLLBACK')
                self.registration_error_Label.setText(
                    '''Эти данные уже есть в базе. Нажмите на кнопку 'Войти' и введите их''')
            connection.close()


class LoginWidget(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Окно входа')
        self.visibility_button.clicked.connect(self.change_visibility)
        self.reg_Button.clicked.connect(self.show_reg_window)
        self.reg_Button.clicked.connect(self.close)
        self.log_in_Button.clicked.connect(self.run)

    def change_visibility(self):  # Метод изменения видимости пароля
        if not self.visibility_button.isChecked():
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def show_reg_window(self):  # Вызывает окно регистрации
        self.reg_form = RegistrationWidget()
        self.reg_form.show()

    def run(self):
        number = self.phone_number.text()
        password = self.password.text()
        try:  # Проверка, введены ли данные
            if not number:
                raise NoPhoneError
            else:
                self.phone_error_Label.setText('')
            if not password:
                raise NoPasswordError
            else:
                self.password_error_Label.setText('')
        except NoPhoneError:
            self.phone_error_Label.setText('Введите номер телефона')
        except NoPasswordError:
            self.password_error_Label.setText('Введите пароль')

        if not self.password_error_Label.text() and not self.phone_error_Label.text():
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()

            for el in users:
                if el[1] == number:
                    if el[3] == password:
                        self.id_ = cursor.execute('''SELECT id FROM users WHERE phone_number=?''',
                                                  (number,)).fetchall()
                        self.id_ = self.id_[0][0]
                        connection = sqlite3.connect('database.db')
                        cursor = connection.cursor()
                        cursor.execute('BEGIN')  # Создание таблицы паролей пользователя
                        cursor.execute('''
                                        CREATE TABLE IF NOT EXISTS {}(
                                        id INTEGER PRIMARY KEY,
                                        login TEXT NOT NULL,
                                        password TEXT NOT NULL,
                                        site INTEGER
                                        )
                                        '''.format('user' + str(self.id_)))
                        cursor.execute('COMMIT')
                        connection.close()
                        self.password.setText('')
                        self.phone_number.setText('')
                        self.login_error_Label.setText('')
                        self.main_form = MainWidget(self.id_)
                        self.main_form.show()  # Открытие основной формы с паролями
                        break
                    else:
                        self.password_error_Label.setText('Неверный пароль')
                        break
            else:
                self.login_error_Label.setText(
                    '''Ваших данных нет в базе. Нажмите на кнопку 'Зарегистрироваться' и введите их''')


class SuccessfulRegistration(QWidget, Ui_Form):  # Окно успешной регистрации
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Успешная регистрация!')
        self.OK_Button.clicked.connect(self.close)


class MainWidget(QMainWindow, Ui_Form2):  # Окно с паролями
    def __init__(self, id_):
        super().__init__()
        self.id_ = id_
        self.setupUi(self)
        self.setWindowTitle('Менеджер паролей')
        self.add_Button.clicked.connect(self.show_dialog_window)  # Окно добавления пароля
        self.dialog_form = DialogWindow(self.id_)
        self.pushButton.clicked.connect(self.update)
        self.update()
        self.tableWidget.show()

    def update(self):  # Обновление данных таблицы
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        result1 = cur.execute("SELECT * FROM {}".format('user' + str(self.id_))).fetchall()
        self.tableWidget.setRowCount(len(result1))
        try:
            self.tableWidget.setColumnCount(len(result1[0]) - 1)
        except IndexError:
            pass
        self.tableWidget.setHorizontalHeaderLabels(
            ['login', 'password', 'site'])
        for i, elem in enumerate(result1):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        con = sqlite3.connect('database.db')
        cursor = con.cursor()
        cursor.execute('BEGIN')
        cursor.execute("SELECT login, password, site FROM {}".format('user' + str(self.id_)))
        data = cursor.fetchall()
        cursor.execute('COMMIT')
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(i, j, item)
        con.close()

    def show_dialog_window(self):
        self.dialog_form.show()


class DialogWindow(QMainWindow, Ui_Dialog):  # Окно добавления пароля
    def __init__(self, id_):
        super().__init__()
        self.setupUi(self)
        self.id_ = id_
        self.setWindowTitle('Добавление пароля')
        self.ok_pushButton.clicked.connect(self.run)
        self.close_pushButton.clicked.connect(self.close)
        self.error_label.setText('')

    def run(self):
        if self.login_lineEdit.text() and self.password_lineEdit.text():
            con = sqlite3.connect('database.db')
            cursor = con.cursor()  # Добавление пароля в таблицу
            cursor.execute('INSERT INTO {}(login, password, site) VALUES (?, ?, ?)'.format('user' + str(self.id_)),
                           (self.login_lineEdit.text(), self.password_lineEdit.text(),
                            self.site_lineEdit.text()))
            con.commit()
            self.close()
            self.error_label.setText('')
        else:
            self.error_label.setText('Введите данные')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
