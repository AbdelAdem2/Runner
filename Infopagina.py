import flet as flet
from flet import *

class MainContent(UserControl):
    def __init__(self):
        self.body = Container(
            width=270,
            height=550,
            border_radius=35,
            border=border.all(5, colors.BLACK),
            gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=["#f9f9f9", "#f6f6f6", "#f9f9f9", "#f6f6f6"],
            ),
            clip_behavior=ClipBehavior.HARD_EDGE,
        )

        super().__init__()

    def build(self):
        items: list = [
            Image(
                src="Images/Hardlopers.jpg",  # Placeholder URL
                width=270,
                height=200,
             
            ),
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Image(
                        src="Images/Hardlopers.jpg",  # Placeholder URL for logo 1
                        width=50,
                        height=50,
                    ),
                    Image(
                        src="Images/Hardlopers.jpg",  # Placeholder URL for logo 2
                        width=50,
                        height=50,
                    ),
                    Image(
                        src="Images/Hardlopers.jpg",  # Placeholder URL for logo 3
                        width=50,
                        height=50,
                    ),
                    Image(
                        src="Images/Hardlopers.jpg",  # Placeholder URL for logo 4
                        width=50,
                        height=50,
                    ),
                ],
            ),
            Divider(height=5, color="transparent"),
            Divider(height=5, color="transparent"),
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Text("Footer content here", color="black", size=12),
                ],
            ),
        ]
        self.body.content = items
        return self.body

def main(page: Page):
    # page settings
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "#212328"

    # create instances
    main = MainContent()

    # add controls
    page.add(
        Stack(
            width=270,
            height=550,
            clip_behavior=ClipBehavior.HARD_EDGE,
            controls=[main],
        )
    )

    # refresh page
    page.update()

if __name__ == "__main__":
    flet.app(target=main)
