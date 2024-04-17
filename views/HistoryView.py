from typing import Union
import mysql.connector

# Functie voor de homepagina van de applicatie
def HomeView(router_data: Union['Router', str, None] = None):
    class MainContent:
        def __init__(self):
            # Verbinding maken met de MySQL-database
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="run"
            )

            self.mycursor = self.mydb.cursor()
            # Het hoofdcontainer-element instellen
            self.body = {
                'width': 270,
                'height': 550,
                'border_radius': 35,
                'border': {'all': 5, 'color': "black"},
                'padding': {'left': 0.1, 'top': 0.1, 'right': 0.1, 'bottom': 0.1},
                'gradient': {
                    'begin': 'alignment.top_center',
                    'end': 'alignment.bottom_center',
                    'colors': ["#f9f9f9", "#f6f6f6", "#f9f9f9", "#f6f6f6"],
                },
                'clip_behavior': 'ClipBehavior.HARD_EDGE',
            }

            self.main_stack = []
            self.card_row = {'scroll': "hidden"}
            self.recent_activity_column = {'scroll': "hidden", 'expand': True}

            self.navbar()

        # Methode voor het maken van de navigatiebalk
        def navbar(self):
            items = []
            label = ["Username", "Email", "Password"]

            # Functie voor het maken van de inhoud van de navigatiebalk
            def create_content():
                contents = []
                for i in range(3):
                    contents.append({
                        'alignment': 'alignment.center',
                        'spacing': 0,
                        'controls': [
                            {'text': label[i], 'color': "black", 'weight': "bold", 'size': 11},
                        ],
                    })
                return {'controls': contents}

            # Container voor de navigatiebalk
            container = {
                'width': 900,
                'height': 75,
                'bgcolor': "#ffffff",
                'border_radius': {
                    'top_left': 0,
                    'top_right': 0,
                    'bottom_left': 35,
                    'bottom_right': 35
                },
                'margin': {'top': 425},
                'border': {
                    'top': {
                        'color': "black",
                        'width': 0.3
                    }
                },
                'content': create_content(),
            }

            items.append(container)

            self.recent_activity_column['controls'] = items

        # Methode voor het bouwen van de homepagina
        def build(self):
            items = [
                {
                    'controls': [
                        {'height': 5, 'color': "transparent"},
                        self.card_row,
                        {'height': 5, 'color': "transparent"},
                        self.recent_activity_column,
                    ],
                },
            ]
            self.main_stack = items
            self.body['content'] = self.main_stack
            return self.body

    content = MainContent()
    return content

# Functie voor de historiepagina van de applicatie
def HistoryView(router_data: Union['Router', str, None] = None):
    class HistoryContent:
        def __init__(self):
            # Verbinding maken met de MySQL-database
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="run"
            )

            self.mycursor = self.mydb.cursor()
            # Het hoofdcontainer-element instellen
            self.body = {
                'width': 270,
                'height': 550,
                'border_radius': 35,
                'border': {'all': 5, 'color': "black"},
                'padding': {'left': 0.1, 'top': 0.1, 'right': 0.1, 'bottom': 0.1},
                'gradient': {
                    'begin': 'alignment.top_center',
                    'end': 'alignment.bottom_center',
                    'colors': ["#f9f9f9", "#f6f6f6", "#f9f9f9", "#f6f6f6"],
                },
                'clip_behavior': 'ClipBehavior.HARD_EDGE',
            }

            self.main_stack = []
            self.history_column = {'scroll': "auto", 'expand': True}

            self.load_history()

        # Methode voor het laden van de renhistorie uit de database
        def load_history(self):
            # Query uitvoeren om de renhistorie op te halen uit de database
            self.mycursor.execute("SELECT distance, bpm FROM running_history")
            history_data = self.mycursor.fetchall()

            # UI-elementen aanmaken voor elke rij in de renhistorie
            for row in history_data:
                distance, bpm = row
                history_item = {'text': f"Afstand: {distance} km, BPM: {bpm}", 'color': "black"}
                self.history_column['controls'].append(history_item)

        # Methode voor het bouwen van de historiepagina
        def build(self):
            items = [
                {
                    'controls': [
                        {'height': 5, 'color': "transparent"},
                        self.history_column,
                    ],
                },
            ]
            self.main_stack = items
            self.body['content'] = self.main_stack
            return self.body

    content = HistoryContent()
    return content


