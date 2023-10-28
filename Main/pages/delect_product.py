import flet as ft

from Main.functions.snack_bar import snack_bar1
from Main.pages.product import display_products
from Main.service.connection.mysql_connection import delete_product


def delete_product_page(page: ft.Page, index):
    def on_close(e):
        alter.open = False
        page.update()

    def ok(e):
        delete_product(int(index))
        on_close('e')
        snack_bar1(page, "Updated Deleted!")
        display_products(page)

    alter = ft.AlertDialog(
        title=ft.Text("Make Sure!"),
        content=ft.Text("This product will be deleted forever."),
        actions=[
            ft.TextButton(
                text="Ok",
                on_click=ok,
            ),
            ft.TextButton(
                text="Cancel",
                on_click=on_close,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = alter
    alter.open = True
    page.update()
