import flet as ft

from Main.assets.loc_file_path import local_assets_path
from Main.functions.theme import start_theme
from Main.pages.add_product import add_product_page
from Main.pages.sales_add import sales_product
from Main.service.connection.mysql_connection import database_checker

old_data = None


def main(page: ft.Page):
    page.window_min_width = 700
    page.window_min_height = 550

    page.window_maximized = True

    page.title = "Inventory Management"

    page.window_center()

    start_theme(page)

    main_column = ft.Column(expand=True)

    add_product = ft.FloatingActionButton(
        icon=ft.icons.ADD_ROUNDED,
        tooltip="Add Product",
        on_click=lambda _: add_product_page(page),
    )

    add_sales = ft.FloatingActionButton(
        icon=ft.icons.ADD_ROUNDED,
        tooltip="New Sales",
        on_click=lambda _: sales_product(page),
    )

    def on_option_click(e):
        page.splash = ft.ProgressBar()
        global old_data

        if e != 5:
            main_column.clean()
            page.update()
            if old_data == 0:
                container.image_src = "/images/background-2.png"
                home.icon = None
            elif old_data == 1:
                page.remove(add_product)
                product.icon = None
            elif old_data == 2:
                page.remove(add_sales)
                sales.icon = None

        old_data = e
        page.update()

        if e == 0:
            container.image_src = "/images/background-1.png"
            home.icon = ft.icons.HOME_ROUNDED
            page.splash = None
        elif e == 1:
            product.icon = ft.icons.SHOPPING_BASKET_ROUNDED
            from Main.pages.product import product_page
            product_page(page, main_column)
            page.add(add_product)
        elif e == 2:
            pass
            sales.icon = ft.icons.ATTACH_MONEY_ROUNDED
            from Main.pages.sales import sales_page
            sales_page(page, main_column)
            page.add(add_sales)

        page.update()

    home = ft.TextButton(
        text='Home',
        data=0,
        on_click=lambda e: on_option_click(e.control.data)
    )

    product = ft.TextButton(
        text="Products",
        data=1,
        on_click=lambda e: on_option_click(e.control.data),
    )

    sales = ft.TextButton(
        text="Sale",
        data=2,
        on_click=lambda e: on_option_click(e.control.data)
    )

    row_menu_list = [
        home,
        product,
        sales,
    ]

    appbar = ft.Container(
        border_radius=9,
        bgcolor=ft.colors.with_opacity(0.5, '#FFFFFF'),
        blur=ft.Blur(5, 5, ft.BlurTileMode.MIRROR),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Row(width=10),
                                    ft.Text(
                                        value="Inventory Management",
                                        weight=ft.FontWeight.BOLD,
                                        size=15,
                                    )
                                ]
                            ),
                            margin=5,
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.START,
                    scroll=ft.ScrollMode.ADAPTIVE,
                ),
                ft.Row(row_menu_list),
                ft.Row(width=50),
            ],
            alignment=ft.MainAxisAlignment.END,
            height=50
        ),
        margin=ft.margin.only(left=10, top=5, right=10),

    )

    container = ft.Container(
        image_fit=ft.ImageFit.COVER,
        image_src="/images/background-2.png",
        margin=-10,
        expand=True,
        content=ft.Column(
            [
                appbar,
                main_column
            ],
        )
    )

    page.add(container)
    page.update()
    on_option_click(0)


def update():
    global old_data
    old_data = None


if __name__ == '__main__':
    database_checker()
    ft.app(
        target=main,
        assets_dir=local_assets_path
    )
