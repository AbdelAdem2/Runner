import re
from typing import Union
# import flet as ft
import flet
from flet import *
from views.Router import Router, DataStrategyEnum
from State import global_state, State
import mysql.connector

def LoginView(router_data: Union[Router, str, None] = None):
    


    class MainContent(UserControl):
        def __init__(self):
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="run"
            )

            self.mycursor = self.mydb.cursor()
            self.body = Container(
                width=270,
                height=550,
                border_radius=35,
                border=border.all(5, colors.BLACK),
                padding=padding.only(left=15, top=25, right=15, bottom=10),
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

            self.register_button = self.create_register_button()
            self.text_fields = self.input_field() 
            self.input_container() 
            super().__init__()

        def create_register_button(self):
            return Container(
                width=260,
                height=55,
                bgcolor="#4169E1",  
                padding=10,
                border_radius=5,
                disabled=True,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        Text("Login", color="black", weight="bold", size=11),
                    ],
                ),
                on_click=self.handle_register_click,
                # on_hover=hover(
                #     bgcolor="#6495ED",
                #     transition=transition(duration=0.2),
                # ),
            )

        def input_field(self):
            text_fields = []

            label = ["Email", "Password"]
            placeholders = ["Enter your username", "Enter your email", "Enter your password"]

            for i in range(2):
                text_field = TextField(
                    label=label[i],
                    password=(i == 1),
                    can_reveal_password=True,
                    width=250,
                    height=40,
                    border_radius=5,
                    color="black",
                    on_change=self.handle_text_field_change,
                )
                
                text_fields.append(text_field)

            return text_fields

        def input_container(self):
            label = ["Email", "Password"]

            items = []

            for i in range(2):
                container = Container(
                    border_radius=5,
                    content=Column(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            Text(color="black", weight="bold", size=11),
                            self.text_fields[i]
                        ],
                    ),
                )
                items.append(container)

            items.append(self.register_button) 

            self.recent_activity_column.controls = items


            

        def handle_text_field_change(self, sender):
            self.update_register_button_color()

        def handle_register_click(self, sender):
            email, password = self.get_register_info()
            if self.validate_input(email, password):
                # self.register_button.bgcolor = "#0000FF" 
                print("Valid input")
                self.mycursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
                myresult = self.mycursor.fetchall()
                if len(myresult) == 1:
                    print("Valid!")
                    self.page.go("/home")
                else:
                    print("Invalid")
                    alert = Text("Geen geldige email en of wachtwoord", color="black", weight="bold", size=11)
                    self.recent_activity_column.controls.append(alert)
                    self.recent_activity_column.update()


            else:
                print("Invalid input")

        def get_register_info(self):
            info = []
            for text_field in self.text_fields:
                info.append(text_field.value)
            return info

        def validate_input(self, email, password):
            if len(password) < 6:
                return False
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return False
            return True

        def update_register_button_color(self):
            email, password = self.get_register_info()
            if self.validate_input(email, password):
                print ("Valid input")
                self.register_button.bgcolor = "#1E90FF"
                self.register_button.disabled = False
            else:
                print("Invalid input")
                self.register_button.bgcolor = "#4169E1" 
            self.recent_activity_column.update() 
                              
        def build(self):
            items: list = [
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


    # def main(page: Page):
    #     # page settings
    #     page.horizontal_alignment = CrossAxisAlignment.CENTER
    #     page.vertical_alignment = MainAxisAlignment.CENTER
    #     # page.padding = padding.only(right=100)
    #     page.bgcolor = "#212328"

    #     # create instances
    #     main = MainContent()

    #     # add controls
    #     page.add(
    #         Stack(
    #             width=270,
    #             height=550,
    #             clip_behavior=ClipBehavior.HARD_EDGE,
    #             controls=[main],
    #         )
    #     )

    #     # refresh page
    #     page.update()

    content = MainContent()
    return content


