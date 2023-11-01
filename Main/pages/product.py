import flet as ft

from Main.service.connection.mysql_connection import display_product

column1 = ft.Column()


def product_page(page: ft.Page, main_column: ft.Column):
    global column1

    main_column.controls = [
        ft.Column(
            [
                column1,
                ft.Row()
            ],
            expand=True,
            scroll=ft.ScrollMode.ADAPTIVE
        )
    ]
    page.splash = None
    page.update()
    display_products(page)


def display_products(page: ft.Page):
    global column1
    data = display_product()
    container = ft.Row(
        wrap=True
    )
    if data.empty is False:
        for i in range(len(data)):
            container.controls.append(Records(page, i, data))
    else:
        container = ft.Container(
            content=ft.Text("No Products", weight=ft.FontWeight.BOLD, size=30),
            alignment=ft.alignment.center,
            height=500,
        )

    column1.controls = [
        container
    ]
    page.update()


class Records(ft.UserControl):

    def __init__(self, page, id_index, data):
        super().__init__()
        self.page = page
        self.index = id_index
        self.data = data

    def edit(self, e):
        from Main.pages.edit_product import edit_product_page
        edit_product_page(self.page, self.index)

    def delete(self, e):
        from Main.pages.delect_product import delete_product_page
        delete_product_page(self.page, self.data.loc[self.index].values[0])

    def build(self):
        data_val = self.data.loc[self.index].values

        image = ft.Container(
            image_src=f'/images/{data_val[5]}',
            width=350,
            height=140,
            image_fit=ft.ImageFit.COVER,
            animate_scale=ft.animation.Animation(400, ft.AnimationCurve.EASE),
            animate=ft.animation.Animation(400, ft.AnimationCurve.EASE),
        )

        def on_hover_(e):
            image.scale = 1.5 if e.data == "true" else 1.0
            image.height = 145 if e.data == "true" else 140
            image.update()
            e.control.scale = 1.1 if e.data == "true" else 1.0
            e.control.update()

        container = ft.Container(
            border_radius=9,
            bgcolor=ft.colors.with_opacity(0.3, '#FFFFFF'),
            blur=ft.Blur(5, 5, ft.BlurTileMode.MIRROR),
            content=ft.Column(
                [
                    image,
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Column(height=5),
                                    ft.Row([ft.Text(f"Name:  {data_val[2]}", size=20)]),
                                    ft.Row([ft.Text(f"Category:  {data_val[1]}", size=20)]),
                                    ft.Row([ft.Text(f"Quantity:  {data_val[3]}", size=20)]),
                                    ft.Row(
                                        [
                                            ft.Text(f"Price:  ₹{data_val[4]}", size=20),
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.PopupMenuButton(
                                                items=[
                                                    ft.PopupMenuItem(
                                                        text="Edit",
                                                        icon=ft.icons.EDIT_ROUNDED,
                                                        on_click=self.edit
                                                    ),
                                                    ft.PopupMenuItem(
                                                        text="Delete",
                                                        icon=ft.icons.DELETE_ROUNDED,
                                                        on_click=self.delete
                                                    ),
                                                ]
                                            )
                                        ],
                                        width=250,
                                        alignment=ft.MainAxisAlignment.END
                                    )
                                ]
                            )
                        ]
                    )

                ],
                width=250,
                height=350,
                alignment=ft.MainAxisAlignment.START,
            ),
            margin=ft.margin.only(left=20, top=10),
            padding=ft.padding.only(left=10, right=10, bottom=10),
            on_hover=on_hover_,
            animate_scale=ft.animation.Animation(600, ft.AnimationCurve.EASE),
        )

        return container
