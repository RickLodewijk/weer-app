import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QTimer, Qt
from weather import get_weather_data  # Importeer de weerlogica
from datetime import datetime


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tijd & Weer Widget')

        # Stel de styling in via QSS
        self.setStyleSheet("""
            QWidget {
                background-color: lightblue;
            }
            QLabel {
                color: darkblue;
                font-size: 18px;
                font-family: 'Arial';
            }
        """)

        # Maak de lay-out
        layout = QVBoxLayout()

        # Maak een spacer item om de inhoud te centreren
        spacer = QSpacerItem(60, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Tijd label
        self.time_label = QLabel('Tijd: Laden...')  # Dit is een tijdelijke waarde
        self.time_label.setAlignment(Qt.AlignCenter)  # Horizontaal en verticaal centreren
        layout.addWidget(self.time_label)

        # Datum label
        self.date_label = QLabel('Datum: Laden...')  # Dit is een tijdelijke waarde
        self.date_label.setAlignment(Qt.AlignCenter)  # Horizontaal en verticaal centreren
        layout.addWidget(self.date_label)

        # Weer label
        self.weather_label = QLabel('Weer: Laden...') # Dit is een tijdelijke waarde
        self.weather_label.setAlignment(Qt.AlignCenter)  # Horizontaal en verticaal centreren
        layout.addWidget(self.weather_label)

        # Maak een spacer item onder de labels om de inhoud te centreren
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_bottom)

        # Stel de layout in voor het hoofdvenster
        self.setLayout(layout)

        # Stel de timer in voor het updaten van de tijd
        self.update_time()

        # Haal het weer meteen op bij het starten van de app
        self.update_weather()

        # Start de timer voor het updaten van de tijd en weer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(3600000)  # 3.600.000 milliseconden = 1 uur        


        # Timer voor het bijwerken van de tijd
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)  # Update tijd elke seconde

        # Timer voor het bijwerken van de datum
        self.date_timer = QTimer(self)
        self.date_timer.timeout.connect(self.update_date)
        self.date_timer.start(1000)  # Update datum elke seconde (optioneel)

    def update_time(self):
        now = datetime.now().strftime("%H:%M")
        self.time_label.setText(f"Tijd: {now}")

    def update_date(self):
        today = datetime.now().strftime("%d-%m-%Y")  # Formatteer de datum zoals dd-mm-yyyy
        self.date_label.setText(f"Datum: {today}")

    def update_weather(self):
        weather, temp = get_weather_data()

        # Update de weerinformatie in de GUI
        if temp is not None:
            self.weather_label.setText(f"Weer: {weather}, {temp}°C")
        else:
            self.weather_label.setText(weather)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Maak de weerapp
    window = WeatherApp()

    # Toon het venster
    window.resize(350, 250)  # Vergroot de venstergrootte zodat het past
    window.show()

    # Start de applicatie
    sys.exit(app.exec_())
