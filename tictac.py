import os
import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TicTac(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMaximumSize(600, 750)
        self.setMinimumSize(600, 750)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon("C:\\Users\\USER\\Downloads\\tictac.ico"))

        # to determine whose turn
        self.user_order = 0

        # style sheet settings
        first_settings = """
            border: 0px;
        """

        self.btn_x_settings = """
            border: 0px;
            font-size: 120px;
            color: blue;
            """
        self.btn_o_settings = """
            border: 0px;
            font-size: 120px;
            color: red;
            """

        # shadow effect
        white_window = QWidget(self)
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(20)
        shadow_effect.setColor(QColor(0, 0, 0, 50))
        shadow_effect.setOffset(0, 0)
        white_window.setGeometry(45, 30, 510, 497)
        white_window.setStyleSheet(
            "background-color: white; border-radius: 8px; border: 2px solid black;"
        )
        white_window.setGraphicsEffect(shadow_effect)

        # shadow effect for winner
        white_window_for_who_won = QWidget(self)
        shadow_effect_for_who_won = QGraphicsDropShadowEffect(self)
        shadow_effect_for_who_won.setBlurRadius(20)
        shadow_effect_for_who_won.setColor(QColor(0, 0, 0, 50))
        shadow_effect_for_who_won.setOffset(0, 0)
        white_window_for_who_won.setGeometry(45, 551, 270, 57)
        white_window_for_who_won.setStyleSheet(
            "background-color: white; border-radius: 8px; border: 2px solid black;"
        )
        white_window_for_who_won.setGraphicsEffect(shadow_effect)

        # are you sure you want to leave game messageBox
        self.msg_quit = QMessageBox(self)
        self.msg_quit.setFont(QFont("Poor Richard"))
        self.msg_quit.setIcon(QMessageBox.Question)
        self.msg_quit.setStyleSheet(
            """
        QMessageBox QPushButton {
            color: #ffffff;
            background-color: #3498db;
            border: 1px solid #2980b9;
            font-size: 20;
            padding: 5px 10px;
            border-radius: 3px;
        }
        QPushButton { min-width: 100px;
                    font-size: 20px;
                    font-weight: bold;
                    
        }
        QMessageBox QPushButton:hover {
            background-color: #4fa3df;
        }
        """
        )
        self.msg_quit.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg_quit.setFont(QFont("Calibri", 30))

        # background photo
        self.qlabel = QLabel(self)
        self.photo = QPixmap("C:\\Users\\USER\\OneDrive\\Desktop\\a.jpg")
        self.qlabel.setPixmap(self.photo)
        self.qlabel.setGeometry(49, 35, 504, 485)

        self.who_won_lbl = QLabel(self)
        self.who_won_lbl.setGeometry(60, 554, 250, 50)
        self.who_won_lbl.setStyleSheet(
            """
        font: 40px;
        color: blue;
        """
        )

        # < ---------------------------------------------- BUTTONS ---------------------------------------------- >
        self.button1 = QPushButton(self)
        self.button1.setGeometry(70, 45, 120, 120)
        self.button1.setStyleSheet(first_settings)

        self.button2 = QPushButton(self)
        self.button2.setGeometry(240, 45, 120, 120)
        self.button2.setStyleSheet(first_settings)

        self.button3 = QPushButton(self)
        self.button3.setGeometry(405, 45, 120, 120)
        self.button3.setStyleSheet(first_settings)

        self.button4 = QPushButton(self)
        self.button4.setGeometry(70, 210, 120, 120)
        self.button4.setStyleSheet(first_settings)

        self.button5 = QPushButton(self)
        self.button5.setGeometry(240, 210, 120, 120)
        self.button5.setStyleSheet(first_settings)

        self.button6 = QPushButton(self)
        self.button6.setGeometry(405, 210, 120, 120)
        self.button6.setStyleSheet(first_settings)

        self.button7 = QPushButton(self)
        self.button7.setGeometry(70, 375, 120, 120)
        self.button7.setStyleSheet(first_settings)

        self.button8 = QPushButton(self)
        self.button8.setGeometry(240, 375, 120, 120)
        self.button8.setStyleSheet(first_settings)

        self.button9 = QPushButton(self)
        self.button9.setGeometry(405, 375, 120, 120)
        self.button9.setStyleSheet(first_settings)

        self.buttons_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]

        # < ---------------------------------------------- CONNECT BUTTONS ---------------------------------------------- >

        self.button1.clicked.connect(lambda: self.button_actions(0))
        self.button2.clicked.connect(lambda: self.button_actions(1))
        self.button3.clicked.connect(lambda: self.button_actions(2))
        self.button4.clicked.connect(lambda: self.button_actions(3))
        self.button5.clicked.connect(lambda: self.button_actions(4))
        self.button6.clicked.connect(lambda: self.button_actions(5))
        self.button7.clicked.connect(lambda: self.button_actions(6))
        self.button8.clicked.connect(lambda: self.button_actions(7))
        self.button9.clicked.connect(lambda: self.button_actions(8))

        # < ---------------------------------------------- OPTION BUTTONS ---------------------------------------------- >

        # to restart game
        self.button_restart = QPushButton("New game", self)
        self.button_restart.setGeometry(335, 550, 220, 60)
        self.button_restart.setStyleSheet(
            """
            QPushButton {
                background-color: #42b72a;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 25px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #62b851;
            }

            QPushButton:pressed {
                background-color: #05991e;
            }
            """
        )
        # to quit game
        self.button_quit = QPushButton("Quit game", self)
        self.button_quit.setGeometry(45, 625, 510, 60)
        self.button_quit.setStyleSheet(
            """
            QPushButton {
                background-color: #d90f0f;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 25px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #de3333;
            }

            QPushButton:pressed {
                background-color: #990505;
            }
            """
        )

        # connect buttons
        self.button_restart.clicked.connect(lambda: self.restart_button())
        self.button_quit.clicked.connect(lambda: self.quit_game())

    # method to determine winner
    def who_won(self):
        is_it_draw = True
        new_green_style = """
            border: 0px;
            font-size: 120px;
            color: #02f702;
            """
        new_o_style = """
        font: 40px;
        color: red;
        """

        new_x_style = "color: blue;font: 40px;"

        btn1 = self.button1.text()
        btn2 = self.button2.text()
        btn3 = self.button3.text()
        btn4 = self.button4.text()
        btn5 = self.button5.text()
        btn6 = self.button6.text()
        btn7 = self.button7.text()
        btn8 = self.button8.text()
        btn9 = self.button9.text()

        if btn1 == btn2 and btn2 == btn3 and btn1 == "x":
            self.button1.setStyleSheet(new_green_style)
            self.button2.setStyleSheet(new_green_style)
            self.button3.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")
        elif btn1 == btn2 and btn2 == btn3 and btn1 == "o":
            self.button1.setStyleSheet(new_green_style)
            self.button2.setStyleSheet(new_green_style)
            self.button3.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif btn4 == btn5 and btn5 == btn6 and btn4 == "x":
            self.button4.setStyleSheet(new_green_style)
            self.button5.setStyleSheet(new_green_style)
            self.button6.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif btn4 == btn5 and btn5 == btn6 and btn4 == "o":
            self.button4.setStyleSheet(new_green_style)
            self.button5.setStyleSheet(new_green_style)
            self.button6.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif (btn7 == btn8 and btn8 == btn9) and btn7 == "x":
            self.button7.setStyleSheet(new_green_style)
            self.button8.setStyleSheet(new_green_style)
            self.button9.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif (btn7 == btn8 and btn8 == btn9) and btn7 == "o":
            self.button7.setStyleSheet(new_green_style)
            self.button8.setStyleSheet(new_green_style)
            self.button9.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif (btn1 == btn4 and btn4 == btn7) and btn1 == "x":
            self.button1.setStyleSheet(new_green_style)
            self.button4.setStyleSheet(new_green_style)
            self.button7.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif (btn1 == btn4 and btn4 == btn7) and btn1 == "o":
            self.button1.setStyleSheet(new_green_style)
            self.button4.setStyleSheet(new_green_style)
            self.button7.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif (btn5 == btn2 and btn2 == btn8) and btn2 == "x":
            self.button5.setStyleSheet(new_green_style)
            self.button2.setStyleSheet(new_green_style)
            self.button8.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif (btn5 == btn2 and btn2 == btn8) and btn2 == "o":
            self.button5.setStyleSheet(new_green_style)
            self.button2.setStyleSheet(new_green_style)
            self.button8.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif (btn3 == btn6 and btn6 == btn9) and btn3 == "x":
            self.button6.setStyleSheet(new_green_style)
            self.button9.setStyleSheet(new_green_style)
            self.button3.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif (btn3 == btn6 and btn6 == btn9) and btn3 == "o":
            self.button6.setStyleSheet(new_green_style)
            self.button9.setStyleSheet(new_green_style)
            self.button3.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif (btn1 == btn5 and btn5 == btn9) and btn1 == "x":
            self.button1.setStyleSheet(new_green_style)
            self.button5.setStyleSheet(new_green_style)
            self.button9.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif (btn1 == btn5 and btn5 == btn9) and btn1 == "o":
            self.button1.setStyleSheet(new_green_style)
            self.button5.setStyleSheet(new_green_style)
            self.button9.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)

        elif (btn3 == btn5 and btn3 == btn7) and btn3 == "x":
            self.button5.setStyleSheet(new_green_style)
            self.button7.setStyleSheet(new_green_style)
            self.button3.setStyleSheet(new_green_style)
            self.who_won_lbl.setStyleSheet(new_x_style)
            self.who_won_lbl.setText("x player won!")

        elif (btn3 == btn5 and btn3 == btn7) and btn3 == "o":
            self.button5.setStyleSheet(new_green_style)
            self.button7.setStyleSheet(new_green_style)
            self.button3.setStyleSheet(new_green_style)
            self.who_won_lbl.setText("o player won!")
            self.who_won_lbl.setStyleSheet(new_o_style)
        elif not (
            len(btn1) > 1
            and len(btn2) > 1
            and len(btn3) > 1
            and len(btn4) > 1
            and len(btn5) > 1
            and len(btn6) > 1
            and len(btn7) > 1
            and len(btn8) > 1
            and len(btn9) > 1
        ):
            for i in self.buttons_list:
                if len(i.text()) > 0:
                    continue
                else:
                    is_it_draw = False
                    break

            if is_it_draw:
                self.who_won_lbl.setText("     Draw")
                self.who_won_lbl.setStyleSheet(
                    """
                font: 42px;
                color: #42b72a;
                font-weight: bold;
                """
                )

        # if any player wins, disable all buttons
        if (
            self.who_won_lbl.text() == "o player won!"
            or self.who_won_lbl.text() == "x player won!"
        ):
            for buttons in self.buttons_list:
                buttons.setDisabled(True)

    # method to determine player's turn
    def check_user(self):
        if self.user_order % 2 == 0:
            self.user_order += 1
            return 1
        else:
            self.user_order += 1
            return 2

    # < ------------------------------------------------------ BUTTONS ACTIONS ------------------------------------------------------ >
    def button_actions(self, button_num):
        user_type = self.check_user()
        if user_type == 1:
            self.buttons_list[button_num].setText("x")
            self.buttons_list[button_num].setDisabled(True)
            self.buttons_list[button_num].setStyleSheet(self.btn_x_settings)
            self.who_won_lbl.setText("    o Turn")
            self.who_won_lbl.setStyleSheet("color: red;font: 45px;")

        elif user_type == 2:
            self.buttons_list[button_num].setText("o")
            self.buttons_list[button_num].setDisabled(True)
            self.buttons_list[button_num].setStyleSheet(self.btn_o_settings)
            self.who_won_lbl.setText("    x Turn")
            self.who_won_lbl.setStyleSheet("color: blue;font: 45px;")

        self.who_won()

    # method to restart game
    def restart_button(self):
        self.user_order = 0
        self.who_won_lbl.setText("")

        for buttons in self.buttons_list:
            buttons.setDisabled(False)
            buttons.setText("")

    # method to quit game
    def quit_game(self):
        self.msg_quit.setText("Are you sure you want to quit game?")
        result = self.msg_quit.exec_()

        if result == QMessageBox.Yes:
            exit()


# main
if __name__ == "__main__":
    os.system("cls")
    app = QApplication(sys.argv)
    program = TicTac()
    program.show()
    sys.exit(app.exec_())
