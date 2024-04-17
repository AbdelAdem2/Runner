import re
from typing import Union
# import flet as ft
import flet
from flet import *
from views.Router import Router, DataStrategyEnum
from State import global_state, State
import mysql.connector
import random
import time
import threading

def HomeView(router_data: Union[Router, str, None] = None):
    


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
                # padding=padding.only(left=15, top=25, right=15, bottom=10),
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
            self.start_button = self.start_button()
            self.register() 


            super().__init__()

        def create_register_button(self):

            items = []
            label = ["Username", "Email", "Password"]

            def create_content():
                contents = []
                for i in range(3):
                    contents.append(Column(
                        alignment=MainAxisAlignment.CENTER,
                        # alignment_cross=CrossAxisAlignment.CENTER,

                        spacing=0,
                        controls=[
                            Text(label[i], color="black", weight="bold", size=11),
                        ],
                    ))
                return Row(controls=contents)  
            return Container(
                width=900,
                height=75,
                bgcolor="#ffffff",
                border_radius=flet.BorderRadius(
                    top_left=0,
                    top_right=0,
                    bottom_left=35,
                    bottom_right=35
                ),
                margin=margin.only(top=232),
                border=flet.Border(
                    top=flet.BorderSide(
                        color=colors.BLACK,
                        width=0.3
                    )
                ),
                content=create_content(),
            )
        def start_button(self):
            return Container(
                width=55,
                height=55,
                bgcolor="#4169E1",  
                padding=10,
                border_radius=100,
                margin=margin.only(left=107),
                ink=True,
                on_click=self.bpm,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        Text("Start", color="black", weight="bold", size=11),
                    ],
                ),
                
                
                # on_hover=hover(
                #     bgcolor="#6495ED",
                #     transition=transition(duration=0.2),
                # ),
            )


        def create_text_fields(self):
            text_fields = []

            label = ["Username", "Email", "Password"]
            placeholders = ["Enter your username", "Enter your email", "Enter your password"]

            for i in range(3):
                text_field = TextField(
                    border_color="transparent",
                    bgcolor="transparent",
                    height=20,
                    width=200,
                    text_size=12,
                    content_padding=3,
                    cursor_color="white",
                    cursor_width=1,
                    color="black",
                    hint_style=TextStyle(
                        size=11,
                        color="gray",
                    ),
                    on_change=self.handle_text_field_change,
                )

                text_fields.append(text_field)

            return text_fields


        def register(self):
            items = []

            container = Container(
            width=260,
            height=55,
            bgcolor="#ffffff",
            padding=10,
            border_radius=5,  
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                spacing=0,
                controls=[
                Text("bpm", color="black", weight="bold", size=11),
                ],
            ),
            )
            self.container = container
            items.append(container)
            items.append(self.start_button)
            items.append(self.register_button) 

            self.recent_activity_column.controls = items

        def bpm(self, sender):
            print("bpm")
            while True:
                bpm = random.randint(60, 100)
                self.container.content = Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        Text(str(bpm), color="black", weight="bold", size=11),
                    ],
                )
                self.recent_activity_column.update()
                time.sleep(1)
      

        def handle_text_field_change(self, sender):
            self.update_register_button_color()

        def handle_register_click(self, sender):
            username, email, password = self.get_register_info()
            
            if self.validate_input(username, email, password):
                self.register_button.bgcolor = "#0000FF" 
                print("Registration successful!")
                self.page.go("/home")

                
                self.mycursor.execute("SELECT * FROM users WHERE name = %s OR email = %s", (username, email))
                if self.mycursor.fetchone() is not None:
                    print("Username or email already exists")
                    self.page.go("/home")

                else:
                    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                    val = (username, email, password)
                    self.mycursor.execute(sql, val)
                    self.mydb.commit()
                    email = 1
                    receiver_email = "pietermei29@gmail.com"

                    print(self.mycursor.rowcount, "record inserted.")

            else:
                self.page.go("/home")

                self.register_button.bgcolor = "#FF0000"  
                print("Registration failed. Please check your input.")

        def get_register_info(self):
            info = []
            for text_field in self.text_fields:
                info.append(text_field.value)
            return info

        def validate_input(self, username, email, password):
            if len(password) < 6:
                return False
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return False
            return True

        def update_register_button_color(self):
            username, email, password = self.get_register_info()
            if self.validate_input(username, email, password):
                print ("Valid input")
                self.register_button.bgcolor = "#0000FF"  
            else:
                print("Invalid input")
                self.register_button.bgcolor = "#FF0000"  

        def build(self):
            # bpm_value = self.bpm()
            items: list = [
                Column(controls=[
                    # Text(bpm_value, color="black", weight="bold", size=11),
                    Divider(height=5, color="transparent"),
                    self.card_row,
                    Divider(height=5, color="transparent"),
                    self.recent_activity_column,
                ]),
            ]
            self.main_stack.controls = items
            self.body.content = self.main_stack
            return self.body


    content = MainContent()
    return content


