from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from core.manager import ARISManager
from voice.input import VoiceInput
import sys

class JarvisGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = ARISManager()
        self.voice_in = VoiceInput()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ARIS- AI Voice Assistant")
        self.setGeometry(200, 100, 700, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #101820;
                color: #00FFF7;
            }
            QTextEdit, QLineEdit {
                background-color: #181F2A;
                color: #00FFF7;
                border: 1px solid #00FFF7;
                border-radius: 8px;
            }
            QPushButton {
                background-color: #00FFF7;
                color: #101820;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00B8A9;
            }
            QLabel#titleLabel {
                color: #00FFF7;
                font-size: 32px;
                font-weight: bold;
                letter-spacing: 2px;
            }
        """)

        main_layout = QVBoxLayout()
        title = QLabel("ARIS - AI Voice Assistant")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        self.status_label = QLabel("Status: Online")
        self.status_label.setFont(QFont("Consolas", 12))
        main_layout.addWidget(self.status_label)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Consolas", 12))
        main_layout.addWidget(self.text_area, stretch=1)

        input_layout = QHBoxLayout()
        self.input_line = QLineEdit()
        self.input_line.setFont(QFont("Consolas", 12))
        self.input_line.setPlaceholderText("Type your command here...")
        self.input_line.returnPressed.connect(self.send_command)
        input_layout.addWidget(self.input_line)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_command)
        input_layout.addWidget(self.send_button)

        self.voice_button = QPushButton("🎤 Speak")
        self.voice_button.clicked.connect(self.voice_command)
        input_layout.addWidget(self.voice_button)

        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)

    def send_command(self):
        user_input = self.input_line.text()
        if user_input:
            self.append_text(f"You: {user_input}")
            intent, entities = self.manager.nlu.parse(user_input)
            response = self.manager.route(intent, entities, user_input)
            self.append_text(f"ARIS: {response}")
            self.input_line.clear()

    def voice_command(self):
        self.status_label.setText("Status: Listening...")
        self.repaint()
        spoken_text = self.voice_in.listen()
        if spoken_text:
            self.append_text(f"You (voice): {spoken_text}")
            intent, entities = self.manager.nlu.parse(spoken_text)
            response = self.manager.route(intent, entities, spoken_text)
            self.append_text(f"ARIS: {response}")
        else:
            self.append_text("ARIS: Sorry, I didn't catch that.")
        self.status_label.setText("Status: Online")

    def append_text(self, text):
        self.text_area.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = JarvisGUI()
    gui.show()
    sys.exit(app.exec_())