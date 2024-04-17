import mysql.connector
from views.UserControl import UserControl
from views.Container import Container
from views.Row import Row
from views.Column import Column
from views.Text import Text
from views.Stack import Stack
from views.Divider import Divider
from views.Border import BorderSide, Border
from views.BorderRadius import BorderRadius
from views.alignment import alignment
from views.gradient import LinearGradient
from views.ClipBehavior import ClipBehavior
from views.Padding import padding
from typing import Union

# Functie voor de homepagina van de applicatie
def HomeView(router_data: Union[Router, str, None] = None):
    
    class MainContent(UserControl):
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
            self.body = Container(
                width=270,
                height=550,
                border_radius=35,
                border=Border(all=5, color="black"),
                padding=padding(left=0.1, top=0.1, right=0.1, bottom=0.1),
                gradient=LinearGradient(
                    begin=alignment.top_center,
                    end=alignment.bottom_center,
                    colors=["#f9f9f9", "#f6f6f6", "#f9f9f9", "#f6f6f6"],
                ),
                clip_behavior=ClipBehavior.HARD_EDGE,
            )

            self.main_stack = Stack()
            self.card_row = Row(scroll="hidden")
            self.recent_activity_column = Column(scroll="hidden", expand=True)

            self.navbar()
            super().__init__()

        # Methode voor het maken van de navigatiebalk
        def navbar(self):
            items = []
            label = ["Username", "Email", "Password"]

            # Functie voor het maken van de inhoud van de navigatiebalk
            def create_content():
                contents = []
                for i in range(3):
                    contents.append(Column(
                        alignment=alignment.center,
                        spacing=0,
                        controls=[
                            Text(label[i], color="black", weight="bold", size=11),
                        ],
                    ))
                return Row(controls=contents)  

            # Container voor de navigatiebalk
            container = Container(
                width=900,
                height=75,
                bgcolor="#ffffff",
                border_radius=BorderRadius(
                    top_left=0,
                    top_right=0,
                    bottom_left=35,
                    bottom_right=35
                ),
                margin=margin(top=425),
                border=Border(
                    top=BorderSide(
                        color="black",
                        width=0.3
                    )
                ),
                content=create_content(),
            )

            items.append(container)

            self.recent_activity_column.controls = items

        # Methode voor het bouwen van de homepagina
        def build(self):
            items = [
                Column(
                    controls=[
                        Divider(height=5, color="transparent"),
                        self.card_row,
                        Divider(height=5, color="transparent"),
                        self.recent_activity_column,
                    ],
                ),
            ]
            self.main_stack.controls = items
            self.body.content = self.main_stack
            return self.body

    content = MainContent()
    return content

# Functie voor de historiepagina van de applicatie
def HistoryView(router_data: Union[Router, str, None] = None):
    class HistoryContent(UserControl):
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
            self.body = Container(
                width=270,
                height=550,
                border_radius=35,
                border=Border(all=5, color="black"),
                padding=padding(left=0.1, top=0.1, right=0.1, bottom=0.1),
                gradient=LinearGradient(
                    begin=alignment.top_center,
                    end=alignment.bottom_center,
                    colors=["#f9f9f9", "#f6f6f6", "#f9f9f9", "#f6f6f6"],
                ),
                clip_behavior=ClipBehavior.HARD_EDGE,
            )

            self.main_stack = Stack()
            self.history_column = Column(scroll="auto", expand=True)

            self.load_history()
            super().__init__()

        # Methode voor het laden van de renhistorie uit de database
        def load_history(self):
            # Query uitvoeren om de renhistorie op te halen uit de database
            self.mycursor.execute("SELECT distance, bpm FROM running_history")
            history_data = self.mycursor.fetchall()

            # UI-elementen aanmaken voor elke rij in de renhistorie
            for row in history_data:
                distance, bpm = row
                history_item = Text(f"Afstand: {distance} km, BPM: {bpm}", color="black")
                self.history_column.add_control(history_item)

        # Methode voor het bouwen van de historiepagina
        def build(self):
            items = [
                Column(
                    controls=[
                        Divider(height=5, color="transparent"),
                        self.history_column,
                    ],
                ),
            ]
            self.main_stack.controls = items
            self.body.content = self.main_stack
            return self.body

    content = HistoryContent()
    return content
