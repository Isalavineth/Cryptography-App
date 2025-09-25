import sys
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt


class CryptographyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cypher App")
        self.title_label = QLabel("Cypher App", self)
        self.description_label = QLabel("Encrypt and Decrypt files instantly", self)
        self.footer_label = QLabel("v1.0", self)
        self.encrypt_description_label = QLabel("Lock files with a key", self)
        self.decrypt_description_label = QLabel("Unlock files quickly", self)
        self.encrypt_button = QPushButton("Encrypt", self)
        self.decrypt_button = QPushButton("Decrypt", self)
        self.key_label = QLabel("Key", self)
        self.key_input = QLineEdit(self)
        self.input_label = QLabel(self)
        self.plain_input = QLineEdit(self)
        self.cypher_input = QLineEdit(self)
        self.save_button = QPushButton("Save Key", self)
        self.import_button = QPushButton("Import Key", self)
        self.encrypt_text_button = QPushButton("Encrypt Text", self)
        self.decrypt_text_button = QPushButton("Decrypt Text", self)
        self.select_file_button = QPushButton("Select File", self)
        self.back_button = QPushButton("Back", self)
        # Execute initUI()
        self.init_UI()

        # QPushButton connections
        self.back_button.clicked.connect(self.show_main_menu)
        self.encrypt_button.clicked.connect(self.encrypt_menu)
        self.decrypt_button.clicked.connect(self.decrypt_menu)
        self.save_button.clicked.connect(self.save_key)
        self.encrypt_text_button.clicked.connect(self.encrypt_text)
        self.decrypt_text_button.clicked.connect(self.decrypt_text)
        self.import_button.clicked.connect(self.import_key)
        self.select_file_button.clicked.connect(self.import_file)

    def init_UI(self):
        self.setFixedSize(500, 600)
        self.key = Fernet.generate_key()  # Generate Fernet Key

        # Main Menu

        self.title_label.setGeometry(0, 0, 500, 100)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.description_label.setGeometry(0, 50, 500, 80)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setObjectName("description_label")

        self.encrypt_description_label.setGeometry(50, 370, 150, 40)
        self.encrypt_description_label.setAlignment(Qt.AlignCenter)
        self.encrypt_description_label.setObjectName("enc_desc")

        self.decrypt_description_label.setGeometry(300, 370, 150, 40)
        self.decrypt_description_label.setAlignment(Qt.AlignCenter)
        self.decrypt_description_label.setObjectName("dec_desc")

        self.footer_label.setGeometry(0, 540, 500, 80)
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setObjectName("footer_label")

        self.encrypt_button.setGeometry(50, 270, 150, 80)
        self.encrypt_button.setObjectName("encrypt_button")

        self.decrypt_button.setGeometry(300, 270, 150, 80)
        self.decrypt_button.setObjectName("decrypt_button")

        # Encryption Menu

        self.plain_input.setGeometry(50, 340, 400, 50)
        self.plain_input.setObjectName("plain_input")
        self.plain_input.setPlaceholderText("Click select file")
        self.plain_input.setAlignment(Qt.AlignCenter)
        self.plain_input.setReadOnly(True)

        # Decryption Menu

        self.cypher_input.setGeometry(50, 340, 400, 50)
        self.cypher_input.setObjectName("cypher_input")
        self.cypher_input.setPlaceholderText("Click select file")
        self.cypher_input.setAlignment(Qt.AlignCenter)
        self.cypher_input.setReadOnly(True)

        # Common Items

        self.key_label.setGeometry(0, 100, 500, 50)
        self.key_label.setAlignment(Qt.AlignCenter)
        self.key_label.setObjectName("key_label")

        self.key_input.setGeometry(50, 150, 400, 50)
        self.key_input.setObjectName("key_input")
        self.key_input.setAlignment(Qt.AlignCenter)
        self.key_input.setReadOnly(True)

        self.save_button.setGeometry(200, 220, 100, 40)
        self.save_button.setObjectName("save_button")

        self.import_button.setGeometry(200, 220, 100, 40)
        self.import_button.setObjectName("import_button")

        self.input_label.setText("Select file below")
        self.input_label.setGeometry(0, 270, 500, 50)
        self.input_label.setObjectName("input_label")
        self.input_label.setAlignment(Qt.AlignCenter)

        self.encrypt_text_button.setGeometry(300, 500, 150, 70)
        self.encrypt_text_button.setObjectName("encrypt_text")

        self.decrypt_text_button.setGeometry(300, 500, 150, 70)
        self.decrypt_text_button.setObjectName("decrypt_text")

        self.back_button.setGeometry(50, 500, 150, 70)
        self.back_button.setObjectName("back_button")

        self.select_file_button.setGeometry(185, 410, 130, 40)
        self.select_file_button.setObjectName("select_button")

        # Items to Show in Main Menu
        self.title_label.show()
        self.encrypt_button.show()
        self.decrypt_button.show()

        # Items to hide in Main Menu
        self.key_label.hide()
        self.key_input.hide()
        self.save_button.hide()
        self.import_button.hide()
        self.input_label.hide()
        self.plain_input.hide()
        self.cypher_input.hide()
        self.encrypt_text_button.hide()
        self.decrypt_text_button.hide()
        self.back_button.hide()
        self.cypher_input.hide()
        self.select_file_button.hide()

        # Make QLineEdits empty
        self.key_input.setText("")
        self.plain_input.setText("")
        self.cypher_input.setText("")

        # Style Sheet
        self.setStyleSheet("""
            QWidget {
                background-color: qradialgradient(cx:0.5, cy:0.5, radius: 0.8, fx:0.5, fy:0.5,
                                      stop:0 #0A2E0A,  
                                      stop:0.2 #003300, 
                                      stop:0.4 #005500, 
                                      stop:0.6 #004400, 
                                      stop:0.8 #002200, 
                                      stop:1 #001100); 
                color: white;
                font-family: monospace;
            }
            QLabel#title_label {
                font-size: 30px;
                background-color: transparent;
                font-family: JetBrains mono;
                font-weight: bold;
            }
            QPushButton#encrypt_button {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                                  stop:0 #007700, 
                                                  stop:1 #00BB00);
                border-radius: 15px;
                font-size: 20px;
            }
            QPushButton#decrypt_button {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                                  stop:0 #00AA00, 
                                                  stop:1 #00EE00);
                border-radius: 15px;
                font-size: 20px;
            }
            QPushButton#encrypt_button:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                                  stop:0 #00AA00, 
                                                  stop:1 #00EE00);
            }
            QPushButton#decrypt_button:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                                  stop:0 #007700,
                                                  stop:1 #00BB00);
            }
            QLabel#key_label {
                background-color: transparent;
                font-size: 20px;
                font-weight: bold;
            }
            QLineEdit#key_input {
                background-color: rgb(37, 57, 0);
                color; black;
                border-radius: 15px;
            }
            QLabel#input_label {
                background-color: transparent;
                font-size: 20px;
                font-weight: bold;
            }
            QLineEdit#plain_input {
                background-color: rgb(37, 57, 0);
                color: white;
                border-radius: 15px;
                font-size: 13px;
            }
            QLineEdit#cypher_input {
                background-color: rgb(37, 57, 0);
                color: white;
                border-radius: 15px;
                font-size: 13px;
            }
            QPushButton#encrypt_text {
                background-color: rgb(8, 203, 0);
                border-radius: 15px;
                font-size: 15px;
            }
            QPushButton#encrypt_text:hover {
                background-color: rgba(8, 203, 0, 0.7);
            }
            QPushButton#decrypt_text {
                background-color: rgb(8, 203, 0);
                border-radius: 15px;
                font-size: 15px;
            }
            QPushButton#decrypt_text:hover {
                background-color: rgba(8, 203, 0, 0.7);
            }
            QPushButton#back_button {
                background-color: rgb(8, 203, 0);
                border-radius: 15px;
                font-size: 15px;
            } 
            QPushButton#back_button:hover {
                background-color: rgba(8, 203, 0, 0.7);
            }  
            QPushButton#save_button {
                background-color: rgb(8, 203, 0);
                border-radius: 15px;
                font-size: 15px;
            }
            QPushButton#select_button {
                background-color: rgb(8, 203, 0);
                border-radius: 15px;
                font-size: 15px;
            }
            QPushButton#select_button:hover {
                background-color: rgba(8, 203, 0, 0.7);
            }
            QPushButton#save_button:hover {
                background-color: rgba(8, 203, 0, 0.7);
            }
            QPushButton#import_button {
                background-color: rgb(8, 203, 0);
                border-radius: 15px;
                font-size: 15px;
            }
            QPushButton#import_button:hover {
                background-color: rgba(8, 203, 0, 0.7);
            }
            QLabel#description_label {
                background-color: transparent;
                font-size: 12px;
                font-weight: bold;
            }
            QLabel#footer_label {
                background-color: transparent;
                background-color: transparent;
            }
            QLabel#enc_desc {
                background-color: transparent;
            }
            QLabel#dec_desc {
                background-color: transparent;
            }
        """)

    # Show Main Menu
    def show_main_menu(self):
        # Items to show in Main Menu
        self.title_label.show()
        self.description_label.show()
        self.encrypt_description_label.show()
        self.decrypt_description_label.show()
        self.footer_label.show()
        self.encrypt_button.show()
        self.decrypt_button.show()

        # Items to hide in Main Menu
        self.key_label.hide()
        self.key_input.hide()
        self.save_button.hide()
        self.import_button.hide()
        self.input_label.hide()
        self.plain_input.hide()
        self.cypher_input.hide()
        self.encrypt_text_button.hide()
        self.decrypt_text_button.hide()
        self.back_button.hide()
        self.select_file_button.hide()

        # Make QLIneEdits empty
        self.key_input.setText("")
        self.plain_input.setText("")
        self.cypher_input.setText("")

    # Show Encryption Menu
    def encrypt_menu(self):
        self.key_input.setText(self.key.decode()) # Show the key in a QLineEdit

        # Items to show in Encryption Menu
        self.key_label.show()
        self.key_input.show()
        self.save_button.show()
        self.input_label.show()
        self.plain_input.show()
        self.encrypt_text_button.show()
        self.back_button.show()
        self.select_file_button.show()

        # Items to hide in Encryption Menu
        self.encrypt_button.hide()
        self.decrypt_button.hide()
        self.description_label.hide()
        self.encrypt_description_label.hide()
        self.decrypt_description_label.hide()

    # Save symmetric key in key.key file
    def save_key(self):
        with open("key.key", "wb") as file:
            file.write(self.key)
        print("saved text")

    # Encrypt the content of the selected file
    def encrypt_text(self):
        with open(self.file_path, "rb") as file:
            content = file.read()
            encrypt = Fernet(self.key).encrypt(content)

        with open(self.file_path, "wb") as file:
            file.write(encrypt)

        self.plain_input.setText("File content encrypted successfully")
        self.encrypt_text_button.hide()

    # Show Decryption Menu
    def decrypt_menu(self):
        self.key_input.setPlaceholderText("Enter key here or click import")

        # Items to show in Decrypt Menu
        self.key_label.show()
        self.key_input.show()
        self.import_button.show()
        self.input_label.show()
        self.cypher_input.show()
        self.decrypt_text_button.show()
        self.back_button.show()
        self.select_file_button.show()

        # Items to hide in Decrypt Menu
        self.encrypt_button.hide()
        self.decrypt_button.hide()
        self.description_label.hide()
        self.encrypt_description_label.hide()
        self.decrypt_description_label.hide()

    # Decrypt the content of the selected file
    def decrypt_text(self):
        with open(self.file_path, "rb") as file:
            content = file.read()
            decrypt = Fernet(self.key).decrypt(content)

        with open(self.file_path, "wb") as file:
            file.write(decrypt)

        self.cypher_input.setText("File content decrypted successfully")
        self.decrypt_text_button.hide()

    # Import the encryption key saved in key.key
    def import_key(self):
        with open("key.key", "rb") as file:
            self.key = file.read()

        self.key_input.setText(self.key.decode())

    # Import the selected file
    def import_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select File",
                                                        "All Files (*);;Text Files (*txt);;Python Files (*.py)")

        if self.file_path:
            self.plain_input.setText(f"Selected: {self.file_path}")
            self.cypher_input.setText(f"Selected: {self.file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cryptography_app = CryptographyApp()
    cryptography_app.show()
    sys.exit(app.exec_())
