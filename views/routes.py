from views.Router import Router, DataStrategyEnum
from views.index_view import IndexView
from views.profile_view import ProfileView
from views.settings_view import SettingsView
from views.data_view import DataView
from views.home_view import HomeView
from views.info_view import InfoView



router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": IndexView,
  "/home": HomeView,
  "/info": InfoView,

}
from views.Router import View

class RunningView(View):
    def __init__(self):
        super().__init__()
        self.running = False  # Variabele om de status van de runsessie bij te houden
        self.paused = False   # Variabele om de status van de pauze bij te houden
        self.heart_rate = 0   # Variabele om de hartslag bij te houden
        self.bpm = 0          # Variabele om de muziek BPM bij te houden

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
