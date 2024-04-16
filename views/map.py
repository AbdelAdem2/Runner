import mysql.connector

class RunningView:
    def __init__(self):
        self.running = False       # Variabele om de status van de runsessie bij te houden
        self.paused = False        # Variabele om de status van de pauze bij te houden
        self.heart_rate = 0        # Variabele om de hartslag bij te houden
        self.bpm = 0               # Variabele om de muziek BPM bij te houden
        self.distance = 0          # Variabele om de afstand bij te houden
        self.time_elapsed = 0      # Variabele om de verstreken tijd bij te houden
        self.average_speed = 0     # Variabele om de gemiddelde snelheid bij te houden

    def calculate_average_speed(self):
        """Berekent de gemiddelde snelheid tijdens de hardloopsessie."""
        if self.distance > 0 and self.time_elapsed > 0:
            time_elapsed_hours = self.time_elapsed / 3600  # Omrekenen van seconden naar uren
            self.average_speed = self.distance / time_elapsed_hours
        else:
            self.average_speed = 0

    def display_average_speed(self):
        """Toont de gemiddelde snelheid tijdens de hardloopsessie."""
        print("Average speed:", self.average_speed, "km/h")

    def start(self):
        """Start de running sessie."""
        if not self.running:
            self.running = True   # Zet de running status op True
            self.paused = False   # Zet de pause status op False
            # Start hartslagmeting en BPM-detectie

    def pause(self):
        """Pauzeert de running sessie."""
        if self.running:
            self.paused = True   # Zet de pause status op True
            # Pauzeer hartslagmeting en BPM-detectie

    def stop(self):
        """Stopt de running sessie."""
        if self.running:
            self.running = False   # Zet de running status op False
            self.paused = False    # Zet de pause status op False
            # Stop hartslagmeting en BPM-detectie

    def display(self):
        """Toont de hartslag en BPM op het scherm."""
        print("Heart rate:", self.heart_rate)
        print("Music BPM:", self.bpm)

    def display_distance(self):
        """Toont de afstand afgelegd tijdens de hardloopsessie."""
        print("Distance:", self.distance, "kilometers")
