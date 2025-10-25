import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(900, 150, 250, 300)
        self.setWindowTitle("Приветствие")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
        hello_label = QLabel(self)
        hello_label.setText("Привет, друзья!")
        hello_label.move(80, 15)

        image = r"C:\Users\timachk\Desktop\hi.png"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(0, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


class MainWindo(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс для второго окна."""
        self.setGeometry(300, 150, 270, 700)  # другое положение
        self.setWindowTitle("Профиль пользователя")
        self.setUpMainWindo()
        self.show()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        images = [
            r"C:\Users\timachk\Desktop\we.png"
        ]
        x_position = 0
        y_position = 0  # начальная позиция для изображений

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    label.move(x_position, y_position)
                    x_position += 125 # увеличиваем позицию для следующего изображения по x
                    y_position += 10 # увеличиваем позицию для следующего изображения по y
            except FileNotFoundError:
                print(f"Файл {image} не найден")
            except Exception as e:
                print(f"Ошибка при загрузке изображения {image}: {e}")

    def setUpMainWindo(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText("Савиных Яна")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(15, 270)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 300)
        about_label = QLabel(self)
        about_label.setText("Я студентка 2 курса МАИ, 3 института, кафедры 317.")
        about_label.setWordWrap(True)
        about_label.move(15, 330)


        skills_label = QLabel(self)
        skills_label.setText("Навыки")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 360)
        languages_label = QLabel(self)
        languages_label.setText("Python | С# | умею готовить")
        languages_label.move(15, 390)
        experience_label = QLabel(self)
        experience_label.setText("Опыт работы")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 420)
        developer_label = QLabel(self)
        developer_label.setText("Староста 236 группы, президент Камбоджи")
        developer_label.move(15, 450)
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Сентрябрь 2024 - Август 3567")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 470)
        driver_label = QLabel(self)
# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window1 = MainWindo()
    sys.exit(app.exec())
