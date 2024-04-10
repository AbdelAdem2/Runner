import re
from typing import Union
# import flet as ft
import flet
from flet import *
from views.Router import Router, DataStrategyEnum
from State import global_state, State
import mysql.connector

def InfoView(router_data: Union[Router, str, None] = None):
    


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
                padding=padding.only(left=0.1, top=0.1, right=0.1, bottom=0.1),
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




        def navbar(self):
            items = []
            label = ["Home", "Email", "Password", "Password"]

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

            container = Container(
                width=900,
                height=75,
                bgcolor="#ffffff",
                border_radius=flet.BorderRadius(
                    top_left=0,
                    top_right=0,
                    bottom_left=35,
                    bottom_right=35
                ),
                margin=margin.only(top=425),
                border=flet.Border(
                    top=flet.BorderSide(
                        color=colors.BLACK,
                        width=0.3
                    )
                ),
                content=create_content(),
            )

            items.append(container)

            self.recent_activity_column.controls = items


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




    content = MainContent()
    return content


