import pygame
import time
import threading

# Initialiseer pygame
pygame.init()

# Laad de muziek die je wilt afspelen
pygame.mixer.music.load("music/bass.wav")

# Functie om muziek af te spelen met een bepaalde snelheid (BPM)
def play_music(bpm):
    pygame.mixer.music.set_tempo(bpm)
    # Pas het volume van de muziek aan op basis van de BPM
     pygame.mixer.music.set_volume(volume)
     volume = min(bpm / 200.0, 1.0)  # Adjust this formula as needed
    pygame.mixer.music.play()

# Functie om de BPM te berekenen op basis van hartslaggegevens
def calculate_bpm(heart_rate):
    # Hier zou je logica moeten zijn om de BPM te berekenen op basis van de hartslaggegevens
    return heart_rate

# Simuleer hartslaggegevens (voor testdoeleinden)
def simulate_heart_rate():
    heart_rate = 60
    while True:
        # Hier zou je code moeten zijn om de werkelijke hartslaggegevens te ontvangen+
        # In deze simulatie wordt de hartslag elke seconde met 10 verhoogd
        heart_rate += 10
        print("Hartslag: {} BPM".format(heart_rate))
        # Bereken de BPM en speel de muziek af op de bijbehorende snelheid
        bpm = calculate_bpm(heart_rate)
        play_music(bpm)
        time.sleep(1)

# Start een thread om hartslaggegevens te simuleren
heart_rate_thread = threading.Thread(target=simulate_heart_rate)
heart_rate_thread.start()
