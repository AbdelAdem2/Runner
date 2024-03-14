import flet
from flet import *

class MainContent(UserControl):
    def __init__(self):
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
        self.recent_activity_column = Column(scroll="hidden", expand=True)

        super().__init__()

    def build(self):
        items: list = [
            Column(
                controls=[
                    Divider(height=5, color="transparent"),
                    self.recent_activity_column,
                ],
            ),
        ]
        self.main_stack.controls = items
        self.body.content = self.main_stack
        return self.body

def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#212328"

    main = MainContent()

    page.add(
        Stack(
            width=270,
            height=550,
            clip_behavior=ClipBehavior.HARD_EDGE,
            controls=[main],
        )
    )

    page.update()

if __name__ == "__main__":
    flet.app(target=main)
